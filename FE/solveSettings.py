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
        self.ui.shelter_res_checkbox.toggled.connect(self.toggle_all_shelter_res_checkboxes)
        self.ui.shelter_stat_checkbox.toggled.connect(self.toggle_all_shelter_stat_checkboxes)

        # Setup layouts for community and shelter scroll areas
        self.community_layout = QVBoxLayout()
        self.ui.scrollArea_2.setWidget(QWidget())  # Set an empty widget to scrollArea_2
        self.ui.scrollArea_2.widget().setLayout(self.community_layout)
        self.ui.scrollArea_2.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: transparent;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: transparent; }
        QLabel { color: black;
        background-color: transparent;}""")

        self.shelter_layout = QVBoxLayout()
        self.ui.scrollArea.setWidget(QWidget())  # Set an empty widget to scrollArea
        self.ui.scrollArea.widget().setLayout(self.shelter_layout)
        self.ui.scrollArea.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: transparent;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: transparent; }
        QLabel { color: black;
        background-color: transparent;}""")

        # Call these methods to load and display data
        self.load_and_display_community_data()  # Load community data
        self.load_and_display_shelter_data()    # Load shelter data
        self.read_shelter_res_data() # Read shelter res data
        self.read_shelter_stat_data() # Read shelter stat data

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
            name_label.setStyleSheet("color: black; background-color: white;")
            self.community_layout.addWidget(name_label)    
    def get_names_from_shelter_excel(self, file_path = "shelData.xlsx"):
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
            name_label.setStyleSheet("color: black; background-color: white;")
            self.shelter_layout.addWidget(name_label)

    def toggle_all_shelter_res_checkboxes(self, checked):
        self.ui.shelter_res_flood_checkbox.setChecked(checked)
        self.ui.shelter_res_typhoon_checkbox.setChecked(checked)
        self.ui.shelter_res_earthquake_checkbox.setChecked(checked)
        # self.ui.shelter_res_volcanic_checkbox.setChecked(checked)
    
    def update_shelter_res_checkbox(self):
        all_checked = (
            self.ui.shelter_res_flood_checkbox.isChecked() and
            self.ui.shelter_res_typhoon_checkbox.isChecked() and
            self.ui.shelter_res_earthquake_checkbox.isChecked()
        )
        self.ui.shelter_res_checkbox.setChecked(all_checked)
    
    def read_shelter_res_data(self, file_path="shelData.xlsx"):
        try:
            data = pd.read_excel(file_path, usecols=["ResToFlood", "ResToTyphoon", "ResToEarthquake"])
            self.ui.shelter_res_flood_checkbox.setChecked(bool(data["ResToFlood"].iloc[0]))
            self.ui.shelter_res_typhoon_checkbox.setChecked(bool(data["ResToTyphoon"].iloc[0]))
            self.ui.shelter_res_earthquake_checkbox.setChecked(bool(data["ResToEarthquake"].iloc[0]))

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File {file_path} not found.")
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"Missing expected column in the Excel file: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
    
    def toggle_all_shelter_stat_checkboxes(self, checked):
        self.ui.shelter_stat_built_checkbox.setChecked(checked)
        self.ui.shelter_stat_pbuilt_checkbox.setChecked(checked)
        self.ui.shelter_stat_dmg_checkbox.setChecked(checked)
        self.ui.shelter_stat_empty_lot_checkbox.setChecked(checked)

    def update_shelter_stat_checkbox(self):
        all_checked = (
            self.ui.shelter_stat_built_checkbox.isChecked() and
            self.ui.shelter_stat_pbuilt_checkbox.isChecked() and
            self.ui.shelter_stat_dmg_checkbox.isChecked() and
            self.ui.shelter_stat_empty_lot_checkbox.isChecked()
        )
        self.ui.shelter_stat_checkbox.setChecked(all_checked)

    def read_shelter_stat_data(self, file_path="shelData.xlsx"):
        try:
            data = pd.read_excel(file_path, usecols=["Status"])
            if data.empty or "Status" not in data.columns:
                raise ValueError("Column 'Status' not found in the Excel file.")

            status = data["Status"].dropna().unique()

            self.ui.shelter_stat_built_checkbox.setChecked("Built" in status)
            self.ui.shelter_stat_pbuilt_checkbox.setChecked("Partially Built" in status)
            self.ui.shelter_stat_dmg_checkbox.setChecked("Damaged" in status)
            self.ui.shelter_stat_empty_lot_checkbox.setChecked("Empty Lot" in status)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File {file_path} not found.")
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"Missing expected column in the Excel file: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")