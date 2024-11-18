import sys
from PySide6.QtWidgets import QDialog, QLabel, QMessageBox, QVBoxLayout, QWidget
from ui_solveSettings import Ui_solveSettings
from entityManagementComm import EntityManagementComm
from entityManagementShelter import EntityManagementShelter
from modelSettings import ModelSettings
from plot_routes import run_pathfinding
from solvingProgress import SolvingProgress
import pandas as pd

class SolveSettingsDialog(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_solveSettings()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)

        self.ui.write_community_btn.clicked.connect(self.open_entitymanagement_dialog)
        self.ui.write_shelter_btn.clicked.connect(self.open_entitymanagement_shelter_dialog)
        self.ui.solveSet_adc_set_btn.clicked.connect(self.open_model_advanced_settings_dialog)
        self.ui.solveSet_solve_btn.clicked.connect(self.open_solving_progress_dialog)

        # Setup layouts for community and shelter scroll areas
        self.community_layout = QVBoxLayout()
        self.ui.scrollArea_2.setWidget(QWidget())  # Set an empty widget to scrollArea_2
        self.ui.scrollArea_2.widget().setLayout(self.community_layout)

        self.shelter_layout = QVBoxLayout()
        self.ui.scrollArea.setWidget(QWidget())  # Set an empty widget to scrollArea
        self.ui.scrollArea.widget().setLayout(self.shelter_layout)

        # Call these methods to load and display data
        self.load_and_display_community_data()  # Load community data
        self.load_and_display_shelter_data()    # Load shelter data

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
    
    def get_names_from_community_excel(self, file_path = "commData.xlsx"):
        try:
            data = pd.read_excel(file_path)
            if "Name" not in data.columns:
                raise ValueError("Column 'Name' not found in the Excel file.")
            return data["Name"].tolist()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
            return []
    
    def load_and_display_community_data(self):
        names = self.get_names_from_community_excel()
        if not names:
            return
        
        # clear scroll area before populating
        for i in reversed(range(self.community_layout.count())):
            widget_to_remove = self.community_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        for name in names:
            name_label = QLabel(name)
            name_label.setStyleSheet("background-color: transparent; background: transparent;")
            self.community_layout.addWidget(name_label)    
    def get_names_from_shelter_excel(self, file_path = "shelterData.xlsx"):
        try:
            data = pd.read_excel(file_path)
            if "Name" not in data.columns:
                raise ValueError("Column 'Name' not found in the Excel file.")
            return data["Name"].tolist()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
            return []
    
    def load_and_display_shelter_data(self):
        names = self.get_names_from_shelter_excel()
        if not names:
            return
        
        # clear scroll area before populating
        for i in reversed(range(self.shelter_layout.count())):
            widget_to_remove = self.shelter_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        for name in names:
            name_label = QLabel(name)
            self.shelter_layout.addWidget(name_label)