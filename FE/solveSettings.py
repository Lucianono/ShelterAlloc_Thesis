import sys
from PySide6.QtWidgets import QDialog, QLabel
from ui_solveSettings import Ui_solveSettings
from entityManagementComm import EntityManagementComm
from entityManagementShelter import EntityManagementShelter
from modelSettings import ModelSettings
from plot_routes import run_pathfinding
from solvingProgress import SolvingProgress

class SolveSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_solveSettings()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)

        self.ui.write_community_btn.clicked.connect(self.open_entitymanagement_dialog)
        self.ui.write_shelter_btn.clicked.connect(self.open_entitymanagement_shelter_dialog)
        self.ui.solveSet_adc_set_btn.clicked.connect(self.open_model_advanced_settings_dialog)
        self.ui.solveSet_solve_btn.clicked.connect(self.open_solving_progress_dialog)

    def open_entitymanagement_dialog(self):
        self.entityManagementComm_Window = EntityManagementComm()
        self.entityManagementComm_Window.show()

    def open_entitymanagement_shelter_dialog(self):
        self.entityManagementShelter_Window = EntityManagementShelter()
        self.entityManagementShelter_Window.show()
    
    def open_model_advanced_settings_dialog(self):
        self.modelSettings_Window = ModelSettings()
        self.modelSettings_Window.show()

    def open_solving_progress_dialog(self):
        self.solvingProgress_Window = SolvingProgress()
        self.solvingProgress_Window.show()
