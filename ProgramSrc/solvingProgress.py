import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QTextEdit
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl, QThread
from ui_solvingprogress import Ui_solvingProgress
from shelterAllocationReport import ShelterAllocationReport
import pandas as pd
import os
from functools import partial
from pathfinder import PathfindingWorker
from optimizedRouting import run_optimization
from DataSetsModel import DataSets

class SolvingProgress(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_solvingProgress()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)
        self.setModal(True)
        self.setWindowTitle("Solving Progress")
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS", "logo.png")))

        self.ui.solving_prog_cancel_btn.clicked.connect(self.cancel_pathfinding)
        self.ui.solvingModel_progressBar.setRange(0, 100)
        self.isCancelled = False
        
        self.worker_thread = QThread()
        self.worker = None
        self.ui.solvingModel_progressBar.setValue(0)
        self.start_pathfinding()

    def start_pathfinding(self):

        self.worker = PathfindingWorker("modelCommData.xlsx", "modelShelData.xlsx")
        self.worker.moveToThread(self.worker_thread)
        self.ui.solvingModel_progressBar.setValue(25)

        # Connect signals
        self.worker.progress.connect(self.update_log)
        self.worker.finished.connect(self.on_finished)
        self.worker.feasibility_warning.connect(self.feasibility_warning_prompt)

        # Start the worker
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker_thread.start()

    def cancel_pathfinding(self):
        self.ui.textEdit.append("Cancelling...")
        self.isCancelled = True
        if self.worker : 
            self.worker.cancel()  

    def update_log(self, message):
        self.ui.textEdit.append(message)

    def on_finished(self):
        self.ui.solving_prog_cancel_btn.setText("CLOSE")
        self.ui.solving_prog_cancel_btn.clicked.connect(self.close)

        if not self.isCancelled:
            self.ui.textEdit.append("Pathfinding Complete!")
            self.ui.solvingModel_progressBar.setValue(50)
            self.worker_thread.quit()
            self.ui.solvingModel_progressBar.setValue(100)
            run_optimization()
            self.report_Window = ShelterAllocationReport()
            self.report_Window.show()

    def feasibility_warning_prompt(self) :
        response = QMessageBox.question(self, "Warning", "No feasible solution may exist. Continue anyway?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.No:
            self.cancel_pathfinding()
    
        

    