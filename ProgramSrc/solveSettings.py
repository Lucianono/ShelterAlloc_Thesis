import sys
from PySide6.QtWidgets import QDialog, QLabel, QMessageBox, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
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

        self.shelter_status_layout = QVBoxLayout()
        self.ui.scrollArea_5.setWidget(QWidget())  # Set an empty widget to scrollArea_5
        self.ui.scrollArea_5.widget().setLayout(self.shelter_status_layout)
        self.ui.scrollArea_5.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: transparent;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: transparent; }
        QLabel { color: black;
        background-color: transparent;}""")

        self.shelter_resistance_layout = QVBoxLayout()
        self.ui.scrollArea_4.setWidget(QWidget())  # Set an empty widget to scrollArea_4
        self.ui.scrollArea_4.widget().setLayout(self.shelter_resistance_layout)
        self.ui.scrollArea_4.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: transparent;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: transparent; }
        QLabel { color: black;
        background-color: transparent;}""")

        # Call these methods to load and display data
        self.load_and_display_community_data()  # Load community data
        self.load_and_display_shelter_data()    # Load shelter data
        self.init_shelter_status_switches()     # Initialize shelter status switches
        self.init_shelter_resistance_switches() # Initialize shelter resistance switches

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
        try:
            self.filter_shelter_data()

            self.solvingProgress_Window = SolvingProgress()
            self.solvingProgress_Window.show()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
    
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

    def init_shelter_status_switches(self):
        self.create_switch("Built", self.shelter_status_layout)
        self.create_switch("Partially Built", self.shelter_status_layout)
        self.create_switch("Damaged", self.shelter_status_layout)
        self.create_switch("Empty Lot", self.shelter_status_layout)

    def init_shelter_resistance_switches(self):
        self.create_switch("Flood", self.shelter_resistance_layout)
        self.create_switch("Typhoon", self.shelter_resistance_layout)
        self.create_switch("Earthquake", self.shelter_resistance_layout)
        # self.create_switch("Volcanic Eruption", self.shelter_resistance_layout)

    def create_switch(self, label_text, layout):
        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setAlignment(Qt.AlignLeft)
        row_layout.setContentsMargins(0, 0, 0, 0)  # Spaces
        row_layout.setSpacing(10)  # Space between label and switch

        # Create label
        label = QLabel(label_text)
        label.setStyleSheet("""
            font-weight: bold;
            font-size: 16px;""")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # Create switch
        switch = QPushButton()
        switch.setCheckable(True)
        switch.setFixedSize(40, 20)  # Switch size
        switch.setStyleSheet("""
            QPushButton {
                background-color: #ccc;
                border-radius: 10px;
            }
            QPushButton::indicator {
                width: 0;  /* Hide default indicator */
            }
        """)

        # Create knob
        knob = QPushButton(switch)
        knob.setFixedSize(16, 16)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 8px;
            }
        """)
        knob.move(2, 2)

        # Create animation
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)

        # Toggle function
        def toggle_switch():
            if switch.isChecked():
                animation.setStartValue(QRect(2, 2, 16, 16))
                animation.setEndValue(QRect(22, 2, 16, 16))
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        border-radius: 10px;
                    }
                """)
            else:
                animation.setStartValue(QRect(22, 2, 16, 16))
                animation.setEndValue(QRect(2, 2, 16, 16))
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #ccc;
                        border-radius: 10px;
                    }
                """)
            animation.start()

        switch.clicked.connect(toggle_switch)

        # Add label and switch to the row layout
        row_layout.addWidget(label)
        row_layout.addWidget(switch)
        layout.addWidget(row_widget)


    def toggle_switch_animation(self, switch, knob):
        if switch.isChecked():
            # Move knob to the right
            self.animation.setStartValue(QRect(2, 2, 16, 16))
            self.animation.setEndValue(QRect(22, 2, 16, 16))
            switch.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    border-radius: 10px;
                }
            """)
        else:
            # Move knob to the left
            self.animation.setStartValue(QRect(22, 2, 16, 16))
            self.animation.setEndValue(QRect(2, 2, 16, 16))  # Reset to left side
            switch.setStyleSheet("""
                QPushButton {
                    background-color: #ccc;
                    border-radius: 10px;
                }
            """)
        self.animation.start()
    
    def update_shelter_res_checkbox(self):
        all_checked = (
            self.ui.shelter_res_flood_checkbox.isChecked() and
            self.ui.shelter_res_typhoon_checkbox.isChecked() and
            self.ui.shelter_res_earthquake_checkbox.isChecked()
        )
        self.ui.shelter_res_checkbox.setChecked(all_checked)

    def update_shelter_stat_checkbox(self):
        all_checked = (
            self.ui.shelter_stat_built_checkbox.isChecked() and
            self.ui.shelter_stat_pbuilt_checkbox.isChecked() and
            self.ui.shelter_stat_dmg_checkbox.isChecked() and
            self.ui.shelter_stat_empty_lot_checkbox.isChecked()
        )
        self.ui.shelter_stat_checkbox.setChecked(all_checked)
    def filter_shelter_data(self, file_path="shelData.xlsx"):
        try:
            data = pd.read_excel(file_path)

            required_columns = ["ResToFlood", "ResToTyphoon", "ResToEarthquake", "Status"]
            for column in required_columns:
                if column not in data.columns:
                    raise ValueError(f"Missing expected column: {column}")

            res_conditions = []
            if self.ui.shelter_res_flood_checkbox.isChecked():
                res_conditions.append(data["ResToFlood"] == True)
            if self.ui.shelter_res_typhoon_checkbox.isChecked():
                res_conditions.append(data["ResToTyphoon"] == True)
            if self.ui.shelter_res_earthquake_checkbox.isChecked():
                res_conditions.append(data["ResToEarthquake"] == True)

            if res_conditions:
                res_filter = pd.concat(res_conditions, axis=1).any(axis=1)
            else:
                res_filter = pd.Series([True] * len(data))

            status_conditions = []
            if self.ui.shelter_stat_built_checkbox.isChecked():
                status_conditions.append(data["Status"] == "Built")
            if self.ui.shelter_stat_pbuilt_checkbox.isChecked():
                status_conditions.append(data["Status"] == "Partially Built")
            if self.ui.shelter_stat_dmg_checkbox.isChecked():
                status_conditions.append(data["Status"] == "Damaged")
            if self.ui.shelter_stat_empty_lot_checkbox.isChecked():
                status_conditions.append(data["Status"] == "Empty Lot")

            if status_conditions:
                status_filter = pd.concat(status_conditions, axis=1).any(axis=1)
            else:
                status_filter = pd.Series([True] * len(data))

            # Apply both filters
            filtered_data = data[res_filter & status_filter]

            # Print the filtered rows
            print(filtered_data)

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File {file_path} not found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")