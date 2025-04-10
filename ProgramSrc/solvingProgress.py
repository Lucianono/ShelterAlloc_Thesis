import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QTextEdit
from PySide6.QtGui import QIcon, QCursor, QKeyEvent
from PySide6.QtCore import Qt, QUrl, QThread
from ui_solvingprogress import Ui_solvingProgress
from shelterAllocationReport import ShelterAllocationReport
from BNTModelPenalized import BNTModelSimulation
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
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui.solving_prog_cancel_btn.clicked.connect(self.cancel_pathfinding)
        self.ui.solvingModel_progressBar.setRange(0, 100)
        self.isCancelled = False
        
        self.worker_thread = QThread()
        self.worker = None
        self.model = None
        self.ui.solvingModel_progressBar.setValue(0)
        self.start_pathfinding()

    def start_pathfinding(self):

        self.worker = PathfindingWorker("modelCommData.xlsx", "modelShelData.xlsx")
        self.worker.moveToThread(self.worker_thread)
        self.ui.solvingModel_progressBar.setValue(25)

        # Connect signals
        self.worker.progress.connect(self.update_log)
        self.worker.finished.connect(self.on_finished_pathfinding)
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
            self.worker_thread.quit()
            self.worker_thread.wait()
        if self.model : 
            self.model.cancel()  
            self.model_thread.quit()
            self.model_thread.wait()
            self.model_thread.deleteLater()
        self.on_finished()

    def on_finished_pathfinding(self):
        self.ui.solvingModel_progressBar.setValue(50)
        
        if not self.isCancelled:
            if not self.feasibilityCheck():
                self.feasibility_warning_prompt()
            self.run_genetic_algorithm()
        else :
            self.on_finished()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()  # Prevent the dialog from closing
        else:
            super().keyPressEvent(event)

    def update_log(self, message):
        self.ui.textEdit.append(message)

    def on_finished(self):
        self.ui.solving_prog_cancel_btn.setText("CLOSE")
        self.ui.solving_prog_cancel_btn.clicked.connect(self.close)
        self.ui.solvingModel_progressBar.setValue(100)

        if not self.isCancelled:
            self.ui.textEdit.append("Algorithm Complete!")
            self.worker_thread.quit()
            run_optimization()
            self.report_Window = ShelterAllocationReport()
            self.report_Window.show()

    def feasibility_warning_prompt(self) :
        response = QMessageBox.question(self, "Warning", "No feasible solution may exist. Continue anyway?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.No:
            self.cancel_pathfinding()
    
        

    

    def run_genetic_algorithm(self):
        
        community_file_path = os.path.join(sys._MEIPASS, "commData.xlsx")
        shelter_file_path = os.path.join(sys._MEIPASS, "shelData.xlsx")
        distance_file_path = os.path.join(sys._MEIPASS, "distance_matrix.xlsx")

        if not os.path.exists(community_file_path) or not os.path.exists(shelter_file_path) or not os.path.exists(distance_file_path):
            self.update_log("Error: Required input files are missing.")
            return

        try:

            self.model = BNTModelSimulation()
            self.model_thread = QThread()

            self.model.moveToThread(self.model_thread)  # Move model to separate thread

            # Connect signals
            self.model.progress_msg.connect(self.update_log)
            self.model.finished.connect(self.on_finished)

            # Corrected: Use a lambda to avoid running the function in the main thread
            self.model_thread.started.connect(self.model.run)
            self.model_thread.finished.connect(self.model.deleteLater)
            self.model_thread.start()


        except Exception as e:
            self.update_log(f"An unexpected error occurred: {e}")


    # =======================
    # FEFASIBILITY CHECKS
    def feasibilityCheck(self):

        datasets = DataSets()
        Community = datasets.get_community_data()
        Shelters = datasets.get_shelter_data()

        Model_parameters = pd.read_excel( os.path.join(sys._MEIPASS, "modelParam.xlsx"), header=0 ).iloc[0]
        area_per_individual = Model_parameters['AreaPerIndiv']

        # check if there exists distance <= max distance 
        failing_communities = []
        for community in Community:
            if not any(d <= community["maxdistance"] for d in community["distances"].values()):
                failing_communities.append(community["name"])
        
        if failing_communities:
            print(f"{failing_communities} has maximum distance that is impossible to allocate. No shelters is close enough.")
            return False

        # check if there exists population <= shelter area * areaPerIndiv
        failing_communities = []
        for community in Community:
            if not (
                any(shelter["area1"] >= community["population"] * area_per_individual for shelter in Shelters) or
                any(shelter["area2"] >= community["population"] * area_per_individual for shelter in Shelters)
            ):
                failing_communities.append(community["name"])
        
        if failing_communities:
            print(f"{failing_communities} has affected population that is impossible to allocate. No shelters is large enough.")
            return False

        # check if total population is theoretically possible to allocate on largest  shelters
        total_population = sum(community['population'] for community in Community)
        top_area2_sum = sum(shelter['area2'] for shelter in Shelters)

        if total_population * area_per_individual > top_area2_sum:
            print(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
            return False
    
        # if no cases are violated return true
        return True

    
