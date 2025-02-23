import sys
from PySide6.QtWidgets import QDialog, QLabel, QMessageBox, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSizePolicy, QCheckBox, QToolTip, QApplication
from PySide6.QtCore import Signal, Qt, QPropertyAnimation, QRect, QEasingCurve
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtGui import QFont
from ui_solveSettings import Ui_solveSettings
from entityManagementComm import EntityManagementComm
from entityManagementShelter import EntityManagementShelter
from modelSettings import ModelSettings
from solvingProgress import SolvingProgress
import pandas as pd
import os

class SolveSettingsDialog(QDialog):

    changes_saved_comm = Signal()
    changes_saved_shel = Signal()

    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_solveSettings()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)
        self.animation = None  # Initialize the animation object
        self.setWindowTitle("Solve Settings")
        self.setModal(True)
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS", "logo.png")))
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui.write_community_btn.clicked.connect(self.open_entitymanagement_dialog)
        self.ui.write_shelter_btn.clicked.connect(self.open_entitymanagement_shelter_dialog)
        self.ui.solveSet_adc_set_btn.clicked.connect(self.open_model_advanced_settings_dialog)
        self.ui.solveSet_solve_btn.clicked.connect(self.open_solving_progress_dialog)
        
        # Setup layouts for community and shelter scroll areas
        self.community_layout = QVBoxLayout()
        self.ui.scrollArea_2.setWidget(QWidget())  # Set an empty widget to scrollArea_2
        self.ui.scrollArea_2.widget().setLayout(self.community_layout)
        self.ui.scrollArea_2.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: #fff;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: #fff; }
        QLabel { color: black;
        background-color: transparent;}""")

        self.shelter_layout = QVBoxLayout()
        self.ui.scrollArea.setWidget(QWidget())  # Set an empty widget to scrollArea
        self.ui.scrollArea.widget().setLayout(self.shelter_layout)
        self.ui.scrollArea.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: #fff;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: #fff; }
        QLabel { color: black;
        background-color: transparent;}""")

        self.shelter_status_layout = QVBoxLayout()
        self.ui.scrollArea_5.setWidget(QWidget())  # Set an empty widget to scrollArea_5
        self.ui.scrollArea_5.widget().setLayout(self.shelter_status_layout)
        self.ui.scrollArea_5.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: #fff;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: #fff; }
        QLabel { color: black;
        background-color: transparent;}""")

        self.shelter_resistance_layout = QVBoxLayout()
        self.ui.scrollArea_4.setWidget(QWidget())  # Set an empty widget to scrollArea_4
        self.ui.scrollArea_4.widget().setLayout(self.shelter_resistance_layout)
        self.ui.scrollArea_4.setStyleSheet("""QScrollArea { border: 1px solid gray;
        background-color: #fff;
        padding: 5px;
        border-radius: 20px; }
        QWidget { background-color: #fff; }
        QLabel { color: black;
        background-color: transparent;}""")

        
        # Initialize shelter status switches
        self.init_shelter_status_switches()
        self.replace_checkbox_with_switch_ss()

        # Initialize shelter resistance switches
        self.init_shelter_resistance_switches()
        self.replace_checkbox_with_switch_sr()

        # Call these methods to load and display data
        self.load_and_display_community_data()
        self.filter_shelter_data()
        
    def open_entitymanagement_dialog(self):
        self.entityManagementComm_Window = EntityManagementComm()
        self.entityManagementComm_Window.changes_saved.connect(self.load_and_display_community_data)
        self.entityManagementComm_Window.show()

    def open_entitymanagement_shelter_dialog(self):
        self.entityManagementShelter_Window = EntityManagementShelter()
        self.entityManagementShelter_Window.changes_saved.connect(self.filter_shelter_data)
        self.entityManagementShelter_Window.changes_saved.connect(self.changes_saved_shel.emit)
        self.entityManagementShelter_Window.show()
    
    def open_model_advanced_settings_dialog(self):
        self.modelSettings_Window = ModelSettings()
        self.modelSettings_Window.show()

    def open_solving_progress_dialog(self):
        try:
            filtered_comm_data = self.load_and_display_community_data()
            filtered_shel_data = self.filter_shelter_data()

            if filtered_comm_data.empty or filtered_shel_data.empty:
                QMessageBox.warning(self, "Warning", "No community or shelter selected.")
                return
            

            file_path = os.path.join(self.save_dir, "modelCommData.xlsx")
            if file_path:
                try:
                    filtered_comm_data.to_excel(file_path, index=False)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            else:
                QMessageBox.warning(self, "Warning", "Save canceled.")

            file_path = os.path.join(self.save_dir, "modelShelData.xlsx")
            if file_path:
                try:
                    filtered_shel_data.to_excel(file_path, index=False)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            else:
                QMessageBox.warning(self, "Warning", "Save canceled.")

            self.solvingProgress_Window = SolvingProgress()
            self.solvingProgress_Window.show()
            self.close()

        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
        
    def load_and_display_community_data(self):

        try:
            # Load the community data
            data = pd.read_excel(os.path.join(self.save_dir,"commData.xlsx"))

            # Filter rows where 'Active' column is True
            active_data = data[data["Active"] == True]
            
            # clear scroll area before populating
            for i in reversed(range(self.community_layout.count())):
                widget_to_remove = self.community_layout.itemAt(i).widget()
                if widget_to_remove:
                    widget_to_remove.deleteLater()

            # Display only active names
            for name in active_data["Name"]:
                name_label = QLabel(name)
                name_label.setStyleSheet("color: black; background-color: white;")
                self.community_layout.addWidget(name_label)

            self.changes_saved_comm.emit()

            return active_data

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

    def init_shelter_status_switches(self):
        self.shelter_status_switches = {}
        for label in ["Built", "Partially Built", "Damaged", "Empty Lot"]:
            switch = self.create_switch(label, self.shelter_status_layout,True)
            switch.clicked.connect(self.filter_shelter_data)
            self.shelter_status_switches[label] = switch

    def init_shelter_resistance_switches(self):
        self.shelter_resistance_switches = {}
        for label in ["Flood", "Typhoon", "Earthquake"]:
            switch = self.create_switch(label, self.shelter_resistance_layout,False)
            switch.clicked.connect(self.filter_shelter_data)
            self.shelter_resistance_switches[label] = switch

    def create_switch(self, label_text, layout, is_active=False):
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
        switch.setChecked(is_active)
        switch.setFixedSize(40, 20)  # Switch size
        switch.setStyleSheet(
            "QPushButton { background-color: #4CAF50; border-radius: 10px; }" 
            if switch.isChecked() else 
            "QPushButton { background-color: #ccc; border-radius: 10px; }"
        )

        # Create knob
        knob = QPushButton(switch)
        knob.setObjectName("knob")
        knob.setFixedSize(16, 16)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 8px;
            }
        """)
        knob.move(22 if is_active else 2, 2)
        switch.knob = knob

        
        # Delegate knob clicks to the switch
        def knob_mouse_press(event):
            switch.click()  # Simulate a click on the switch
            super(knob.__class__, knob).mousePressEvent(event)

        knob.mousePressEvent = knob_mouse_press

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
        return switch # Return the switch object


    def toggle_switch_animation(self, switch, knob):
        # Ensure self.animation is properly initialized
        self.animation = QPropertyAnimation(knob, b"geometry")
        self.animation.setDuration(200)  # Set the duration once when initializing

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

    def filter_shelter_data(self):
        try:
            file_path="shelData.xlsx"

            data = pd.read_excel(os.path.join(self.save_dir,file_path))

            # Retrieve switch states
            built_switch_state = self.shelter_status_switches["Built"].isChecked()
            partially_built_switch_state = self.shelter_status_switches["Partially Built"].isChecked()
            damaged_switch_state = self.shelter_status_switches["Damaged"].isChecked()
            empty_lot_switch_state = self.shelter_status_switches["Empty Lot"].isChecked()

            # Retrieve switch states
            flood_switch_state = self.shelter_resistance_switches["Flood"].isChecked()
            typhoon_switch_state = self.shelter_resistance_switches["Typhoon"].isChecked()
            earthquake_switch_state = self.shelter_resistance_switches["Earthquake"].isChecked()

            data = data[data["Active"] == True]

            # Apply filters based on switch states
            if not built_switch_state:
                data = data[data["Status"] != "Built"]
            if not partially_built_switch_state:
                data = data[data["Status"] != "Partially Built"]
            if not damaged_switch_state:
                data = data[data["Status"] != "Damaged"]
            if not empty_lot_switch_state:
                data = data[data["Status"] != "Empty Lot"]

            # Apply filters based on switch states
            if flood_switch_state:
                data = data[data["ResToFlood"] == True]
            if typhoon_switch_state:
                data = data[data["ResToTyphoon"] == True]
            if earthquake_switch_state:
                data = data[data["ResToEarthquake"] == True]

            # Reflect filtered data in the UI
            self.update_shelter_scroll_area(data)

            return data

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to filter file: {e}")


    def update_shelter_scroll_area(self, filtered_data):
        try:
            # Clear existing widgets in the scroll area
            for i in reversed(range(self.shelter_layout.count())):
                widget_to_remove = self.shelter_layout.itemAt(i).widget()
                if widget_to_remove:
                    widget_to_remove.deleteLater()

            # Populate with filtered shelters
            for name in filtered_data["Name"]:
                name_label = QLabel(name)
                name_label.setStyleSheet("color: black; background-color: white;")
                self.shelter_layout.addWidget(name_label)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update shelter display: {e}")

    def replace_checkbox_with_switch_sr(self):
        frame_12 = self.ui.frame_12
        frame_11 = self.ui.frame_11

        sr_switch = frame_12.layout()
        if sr_switch:
            for i in reversed(range(sr_switch.count())):
                widget = sr_switch.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
        
        sr_switch = self.create_title_switch("Shelter Resistance", frame_12.layout())
        # shelter_resistance_switch = self.create_title_switch("Shelter Resistance", sr_switch)

        # sr_switch = frame_12.layout()
        sr_switch.toggled.connect(lambda: self.toggle_all_shelter_resistance_switches(sr_switch.isChecked()))

        frame_12.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        frame_11.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def replace_checkbox_with_switch_ss(self):
        frame_8 = self.ui.frame_8
        frame_7 = self.ui.frame_7

        ss_switch = frame_8.layout()
        if ss_switch:
            for i in reversed(range(ss_switch.count())):
                widget = ss_switch.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
        ss_switch = self.create_title_switch("Shelter Status", frame_8.layout())
        # shelter_status_switch = self.create_title_switch("Shelter Status", ss_switch)

        # ss_switch = frame_8.layout()
        ss_switch.toggled.connect(lambda: self.toggle_all_shelter_status_switches(ss_switch.isChecked()))

        frame_8.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        frame_7.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def create_title_switch(self, label_text, layout, is_active=False):
        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setAlignment(Qt.AlignLeft)
        row_layout.setContentsMargins(0, 0, 0, 0)  # Spaces
        row_layout.setSpacing(10)  # Space between label and switch

        # Create label
        label = QLabel(label_text)
        label.setStyleSheet("""
            font-weight: bold;
            font-size: 18px;
            text-decoration: underline;""")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # Create switch
        switch = QPushButton()
        switch.setCheckable(True)
        switch.setFixedSize(40, 20)  # Switch size
        switch.setStyleSheet(
            "QPushButton { background-color: #4CAF50; border-radius: 10px; }" 
            if switch.isChecked() else 
            "QPushButton { background-color: #ccc; border-radius: 10px; }"
        )

        # Create knob
        knob = QPushButton(switch)
        knob.setFixedSize(16, 16)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 8px;
            }
        """)
        knob.move(22 if is_active else 2, 2)

        
        # Delegate knob clicks to the switch
        def knob_mouse_press(event):
            switch.click()  # Simulate a click on the switch
            super(knob.__class__, knob).mousePressEvent(event)

        knob.mousePressEvent = knob_mouse_press

        # Create animation
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)

        # Toggle function
        def toggle_title_switch():
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

        switch.clicked.connect(toggle_title_switch)

        # Add label and switch to the row layout
        row_layout.addWidget(label)
        row_layout.addWidget(switch)
        layout.addWidget(row_widget)
        return switch # Return the switch object


    def toggle_title_switch_animation(self, switch, knob):
        # Create a unique animation for each switch
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)  # Set the duration once when initializing

        if switch.isChecked():
            # Move knob to the right
            animation.setStartValue(QRect(2, 2, 16, 16))
            animation.setEndValue(QRect(22, 2, 16, 16))
            switch.setStyleSheet("""QPushButton { background-color: #4CAF50; border-radius: 10px; }""")
        else:
            # Move knob to the left
            animation.setStartValue(QRect(22, 2, 16, 16))
            animation.setEndValue(QRect(2, 2, 16, 16))
            switch.setStyleSheet("""QPushButton { background-color: #ccc; border-radius: 10px; }""")

        animation.start()

    def toggle_all_shelter_resistance_switches(self, state):
        # Toggle Flood, Typhoon, Earthquake switches based on the state of Shelter Resistance switch
        flood_switch = self.shelter_resistance_switches["Flood"]
        typhoon_switch = self.shelter_resistance_switches["Typhoon"]
        earthquake_switch = self.shelter_resistance_switches["Earthquake"]

        if state:
            # If the Shelter Resistance switch is turned on, turn on all other switches
            if not flood_switch.isChecked() : 
                flood_switch.click()
            if not typhoon_switch.isChecked() : 
                typhoon_switch.click()
            if not earthquake_switch.isChecked() : 
                earthquake_switch.click()
        else:
            # If the Shelter Resistance switch is turned off, turn off all other switches
            if flood_switch.isChecked() : 
                flood_switch.click()
            if typhoon_switch.isChecked() : 
                typhoon_switch.click()
            if earthquake_switch.isChecked() : 
                earthquake_switch.click()


    def toggle_all_shelter_status_switches(self, state):
        # Toggle Built, Partially Built, Damaged, Empty Lot switches based on the state of Shelter Status switch
        built_switch = self.shelter_status_switches["Built"]
        partially_built_switch = self.shelter_status_switches["Partially Built"]
        damaged_switch = self.shelter_status_switches["Damaged"]
        empty_lot_switch = self.shelter_status_switches["Empty Lot"]

        if state:
            # If the Shelter Resistance switch is turned on, turn on all other switches
            if not built_switch.isChecked() : 
                built_switch.click()
            if not partially_built_switch.isChecked() : 
                partially_built_switch.click()
            if not damaged_switch.isChecked() : 
                damaged_switch.click()
            if not empty_lot_switch.isChecked() : 
                empty_lot_switch.click()
        else:
            # If the Shelter Resistance switch is turned off, turn off all other switches
            if built_switch.isChecked() : 
                built_switch.click()
            if partially_built_switch.isChecked() : 
                partially_built_switch.click()
            if damaged_switch.isChecked() : 
                damaged_switch.click()
            if empty_lot_switch.isChecked() : 
                empty_lot_switch.click()

    