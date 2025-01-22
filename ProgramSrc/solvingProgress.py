import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QTextEdit
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl, QThread
from ui_solvingprogress import Ui_solvingProgress
import pandas as pd
import os
from functools import partial
from pathfinder import PathfindingWorker
from optimizedRouting import run_optimization

class SolvingProgress(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_solvingProgress()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)

        self.ui.solving_prog_cancel_btn.clicked.connect(lambda : self.cancel_pathfinding(self))
        self.ui.solvingModel_progressBar.setRange(0, 100)
        

        self.worker_thread = QThread()
        self.worker = None
        self.ui.solvingModel_progressBar.setValue(0)
        self.start_pathfinding()
        

    def start_pathfinding(self):
        self.worker = PathfindingWorker("commData.xlsx", "shelData.xlsx")
        self.worker.moveToThread(self.worker_thread)
        self.ui.solvingModel_progressBar.setValue(25)

        # Connect signals
        self.worker.progress.connect(self.update_log)
        self.worker.finished.connect(self.on_finished)

        # Start the worker
        self.worker_thread.started.connect(lambda : self.worker.run(self))
        self.worker_thread.start()

    def cancel_pathfinding(self,dialog):
        if self.worker:
            self.worker.cancel()
            self.ui.textEdit.append("Pathfinding cancelled.")
            dialog.close()

    def update_log(self, message):
        self.ui.textEdit.append(message)

    def on_finished(self):
        self.ui.textEdit.append("Pathfinding Complete!")
        self.ui.solvingModel_progressBar.setValue(50)
        self.worker_thread.quit()
        # run_optimization()
        self.ui.solvingModel_progressBar.setValue(100)
        
