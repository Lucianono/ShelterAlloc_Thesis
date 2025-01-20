from PySide6.QtWidgets import QLabel, QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtGui import QAction, QColor, QIcon, QCursor, QPixmap
from PySide6.QtCore import Qt, QUrl, QTimer, QSize, QRect, QPropertyAnimation
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from functools import partial
from ui_dashboard import Ui_MainWindow
from solveSettings import SolveSettingsDialog
from entityManagementComm import EntityManagementComm
from entityManagementShelter import EntityManagementShelter
from folium.plugins import MousePosition
import pandas as pd
import os
import sys
import folium
import io
import networkx as nx
import osmnx as ox

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dashboard")

        self.is_adding_community = False
        self.is_adding_shelter = False

        self.stackedWidget.hide()
        
        self.add_community_btn.clicked.connect(self.handle_add_community)
        self.add_shelter_btn.clicked.connect(self.handle_add_shelter)


        self.load_comm_data()
        self.load_shel_data()

        
        #for value in self.data.iloc[:, 0]:
         #   button = self.findChild(QPushButton, f"barangay_{value}_btn")
          #  if button:
           #     button.clicked.connect(lambda checked, value=value: self.handle_button_click(value))

        #self.barangay_a_btn.clicked.connect(self.unhide_stacked_widget)

        self.initial_map_file_path = os.path.join(os.getcwd(), "map.html")
        self.optimized_map_file_path = os.path.join(os.getcwd(), "optimized-routes-map.html")
        self.last_modified_time = os.path.getmtime(self.optimized_map_file_path) if os.path.exists(self.optimized_map_file_path) else None

        if os.path.exists(self.optimized_map_file_path):
            self.webEngineView.setUrl(QUrl.fromLocalFile(self.optimized_map_file_path))
        else:
            self.webEngineView.setUrl(QUrl.fromLocalFile(self.initial_map_file_path))

        self.map_update_timer = QTimer(self)
        self.map_update_timer.timeout.connect(self.check_for_optimized_map_update)
        self.map_update_timer.start(1000)  # Check every second

        self.file_path = None
        self.advanced_settings_com.clicked.connect(self.open_entitymanagement_dialog)
        self.advanced_settings_shel.clicked.connect(self.open_entitymanagement_shelter_dialog)
        self.solve_btn.clicked.connect(self.open_solve_settings_dialog)
        
        self.mc_cancel_changes_btn.clicked.connect(self.open_solve_settings_dialog)
        self.mc_cancel_changes_btn_2.clicked.connect(self.open_solve_settings_dialog)
        self.mc_save_changes_btn.clicked.connect(self.open_solve_settings_dialog)
        self.mc_save_changes_btn_2.clicked.connect(self.open_solve_settings_dialog)

        
        # swap checkboxes to switches
        self.switch_1 = self.add_switch(self.checkBox_15)
        self.switch_2 = self.add_switch(self.checkBox_16)

        self.menu = QMenu(self)
        self.show()

        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

    def open_entitymanagement_dialog(self):
        self.entityManagementComm_Window = EntityManagementComm()
        self.entityManagementComm_Window.changes_saved.connect(self.load_comm_data)
        self.entityManagementComm_Window.show()

    def open_entitymanagement_shelter_dialog(self):
        self.entityManagementShelter_Window = EntityManagementShelter()
        self.entityManagementShelter_Window.changes_saved.connect(self.load_shel_data)
        self.entityManagementShelter_Window.show()

    def open_solve_settings_dialog(self):
        self.solveSettings_Window = SolveSettingsDialog()
        self.solveSettings_Window.show()

    def check_for_optimized_map_update(self):
        # Check if the optimized-routes-map.html exists
        if os.path.exists(self.optimized_map_file_path):
            # Get the last modified time of the optimized map
            current_modified_time = os.path.getmtime(self.optimized_map_file_path)

            # Check if the optimized map is newer than the initial map
            initial_map_modified_time = os.path.getmtime(self.initial_map_file_path)
            if (
                self.last_modified_time is None or 
                (current_modified_time != self.last_modified_time and current_modified_time > initial_map_modified_time)
            ):
                self.last_modified_time = current_modified_time

                # Switch the displayed map to optimized-routes-map.html
                self.webEngineView.setUrl(QUrl.fromLocalFile(self.optimized_map_file_path))
                print(f"Map updated to optimized routes: {self.optimized_map_file_path}")

    def unhide_stacked_widget(self):
        self.stackedWidget.show()

    def load_comm_data(self):
        layout = self.verticalLayout_18.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Properly delete the widget

        self.data = pd.read_excel(os.path.join(os.getcwd(), "commData.xlsx"), header=0)
        
        try:
            file_path = os.path.join(os.getcwd(), "commData.xlsx")
            self.data_Names = pd.read_excel(file_path, usecols=['Name'])

            for index, value in self.data_Names.iloc[:, 0].items():
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128.png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(24, 24)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(24, 24)

                name_label = QLabel(str(value))
                name_label.setMaximumSize(QSize(170, 16777215))

                button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(30,30))

                button.setFixedSize(30,30)

                button.setStyleSheet("background: transparent; border: none;")

                button.setObjectName(f"barangay_{value}_btn")

                button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

                hbox_layout.addWidget(picture_label)
                hbox_layout.addWidget(name_label)
                hbox_layout.addWidget(button)

                container_widget = QWidget()
                container_widget.setLayout(hbox_layout)
                container_widget.setStyleSheet("background: transparent;")

                layout.addWidget(container_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")

    def load_shel_data(self):

        layout = self.verticalLayout_19.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Properly delete the widget

        self.shel_data = pd.read_excel(os.path.join(os.getcwd(), "shelData.xlsx"), header=0)

        try:
            file_path = os.path.join(os.getcwd(), "shelData.xlsx")
            self.data_Names = pd.read_excel(file_path, usecols=['Name'])

            for index, value in self.data_Names.iloc[:, 0].items():
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128 (1).png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(24, 24)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(24, 24)

                name_label = QLabel(str(value))
                name_label.setMaximumSize(QSize(170, 16777215))

                button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(30,30))

                button.setFixedSize(30,30)

                button.setStyleSheet("background: transparent; border: none;")

                button.setObjectName(f"shelter_{value}_btn")

                button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

                hbox_layout.addWidget(picture_label)
                hbox_layout.addWidget(name_label)
                hbox_layout.addWidget(button)

                container_widget = QWidget()
                container_widget.setLayout(hbox_layout)

                layout.addWidget(container_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")


    def handle_button_click(self, button_name):
        value = button_name.split("_")[1]
        
        self.stackedWidget.show()

        if button_name.startswith("barangay_"):
            self.page.show()
            self.page_2.hide()
            row = self.data[self.data['Name'] == value].index[0]

            self.switch_1.setChecked(self.data.loc[row, 'Active'])
            self.switch_1.toggle_animation()

            self.plainTextEdit_15.setPlainText(str(self.data.loc[row, 'Name']))

            self.plainTextEdit.setPlainText(str(self.data.loc[row, 'xDegrees']))
            self.plainTextEdit_2.setPlainText(str(self.data.loc[row, 'yDegrees']))
            self.plainTextEdit_3.setPlainText(str(self.data.loc[row, 'Population']))
            self.plainTextEdit_4.setPlainText(str(self.data.loc[row, 'AffectedPop']))
            self.plainTextEdit_5.setPlainText(str(self.data.loc[row, 'MaxDistance']))
            self.plainTextEdit_6.setPlainText(str(self.data.loc[row, 'Remarks']).replace('nan', ''))

            self.page.update()
            self.stackedWidget.update()

        elif button_name.startswith("shelter_"):
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.page_2.show()
            self.page.hide()
            row = self.shel_data[self.shel_data['Name'] == value].index[0]

            self.switch_2.setChecked(self.shel_data.loc[row, 'Active'])
            self.switch_2.toggle_animation()

            self.plainTextEdit_9.setPlainText(str(self.shel_data.loc[row, 'Name']))

            self.plainTextEdit_11.setPlainText(str(self.shel_data.loc[row, 'xDegrees']))
            self.plainTextEdit_10.setPlainText(str(self.shel_data.loc[row, 'yDegrees']))
            self.plainTextEdit_8.setPlainText(str(self.shel_data.loc[row, 'Area1']))
            self.plainTextEdit_12.setPlainText(str(self.shel_data.loc[row, 'Cost1']))
            self.plainTextEdit_13.setPlainText(str(self.shel_data.loc[row, 'Area2']))
            self.plainTextEdit_14.setPlainText(str(self.shel_data.loc[row, 'Cost2']))
            self.checkBox_17.setChecked(self.shel_data.loc[row, 'ResToFlood'])
            self.checkBox_18.setChecked(self.shel_data.loc[row, 'ResToTyphoon'])
            self.checkBox_19.setChecked(self.shel_data.loc[row, 'ResToEarthquake'])
            status_mapping = {"Built": 0, "Partially Built": 1, "Damaged": 2, "Empty Lot": 2}
            self.status_comboBox_2.setCurrentIndex(status_mapping.get(str(self.shel_data.loc[row, 'Status']), -1))
            self.plainTextEdit_17.setPlainText(str(self.shel_data.loc[row, 'Remarks']).replace('nan', ''))
            

            self.page_2.update()
            self.stackedWidget.update()

    def handle_add_community(self):
        if not self.is_adding_community:
            self.is_adding_community = True
            self.open_add_community_page()
        else:
            self.save_community_to_excel()
            self.is_adding_community = False

    def handle_add_shelter(self):
        if not self.is_adding_shelter:
            self.is_adding_shelter = True
            self.open_add_shelter_page()
        else:
            self.save_shelter_to_excel()
            self.is_adding_shelter = False

    def open_add_community_page(self):
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()
        self.plainTextEdit_5.clear()
        self.plainTextEdit_6.clear()

        self.stackedWidget.setCurrentWidget(self.page)
        self.stackedWidget.show()

    def open_add_shelter_page(self):
        self.plainTextEdit_11.clear()
        self.plainTextEdit_10.clear()
        self.plainTextEdit_8.clear()
        self.plainTextEdit_12.clear()
        self.plainTextEdit_13.clear()
        self.plainTextEdit_14.clear()

        self.stackedWidget.setCurrentWidget(self.page_2)
        self.stackedWidget.show()

    def save_community_to_excel(self):
        try:
            x_degrees = float(self.plainTextEdit.toPlainText()) if self.plainTextEdit.toPlainText() else 0.0
            y_degrees = float(self.plainTextEdit_2.toPlainText()) if self.plainTextEdit_2.toPlainText() else 0.0
            population = int(self.plainTextEdit_3.toPlainText()) if self.plainTextEdit_3.toPlainText() else 0
            affected_pop = int(self.plainTextEdit_4.toPlainText()) if self.plainTextEdit_4.toPlainText() else 0
            work_pop = int(self.plainTextEdit_5.toPlainText()) if self.plainTextEdit_5.toPlainText() else 0
            remarks = self.plainTextEdit_6.toPlainText()
        
            new_data = {
                "Name": "testAdd",
                "xDegrees": x_degrees,
                "yDegrees": y_degrees,
                "Population": population,
                "AffectedPop": affected_pop,
                "WorkPop": work_pop,
                "MaxDistance": "1000",
                "Remarks": remarks,
            }
        
            file_path = os.path.join(os.getcwd(), "commData.xlsx")

        
            if os.path.exists(file_path):
                existing_data = pd.read_excel(file_path)
                last_index = existing_data.index[-1]
            else:
                existing_data = pd.DataFrame(columns=new_data.keys())
                last_index = -1

            new_row = pd.DataFrame([new_data])

            updated_data = pd.concat([existing_data, new_row], ignore_index=True)
            updated_data.to_excel(file_path, index=False)

            self.data = pd.read_excel(file_path)

            self.add_new_community_to_ui(new_data, last_index + 1)

            self.add_marker_to_map("commData.xlsx", "community")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")

    def save_shelter_to_excel(self):
        try:
            x_degrees = float(self.plainTextEdit_11.toPlainText()) if self.plainTextEdit_11.toPlainText() else 0.0
            y_degrees = float(self.plainTextEdit_10.toPlainText()) if self.plainTextEdit_10.toPlainText() else 0.0
            area1 = int(self.plainTextEdit_8.toPlainText()) if self.plainTextEdit_8.toPlainText() else 0
            cost1 = int(self.plainTextEdit_12.toPlainText()) if self.plainTextEdit_12.toPlainText() else 0
            area2 = int(self.plainTextEdit_13.toPlainText()) if self.plainTextEdit_13.toPlainText() else 0
            cost2 = int(self.plainTextEdit_14.toPlainText()) if self.plainTextEdit_14.toPlainText() else 0

            new_data = {
                "Name": "testAdd",
                "xDegrees": x_degrees,
                "yDegrees": y_degrees,
                "Area1": area1,
                "Cost1": cost1,
                "Area2": area2,
                "Cost2": cost2,
                "ResToFlood": "1",
                "ResToTyphoon": "1",
                "ResToEarthquake": "1",
                "Status": "Built"
                }
        
            file_path = os.path.join(os.getcwd(), "shelData.xlsx")

        
            if os.path.exists(file_path):
                existing_data = pd.read_excel(file_path)
                last_index = existing_data.index[-1]
            else:
                existing_data = pd.DataFrame(columns=new_data.keys())
                last_index = -1

            new_row = pd.DataFrame([new_data])

            updated_data = pd.concat([existing_data, new_row], ignore_index=True)
            updated_data.to_excel(file_path, index=False)

            self.shel_data = pd.read_excel(file_path)

            self.add_new_shelter_to_ui(new_data, last_index + 1)

            self.add_marker_to_map("shelData.xlsx", "shelter")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")

    def add_new_community_to_ui(self, community_data, index):
        layout = self.communities_dropdown.layout()

        hbox_layout = QHBoxLayout()

        
        picture_label = QLabel()
        icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128.png")
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaled(31, 31)
        picture_label.setPixmap(pixmap)
        picture_label.setFixedSize(31, 31)

        name_label = QLabel(community_data["Name"])

        button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
        button = QPushButton()
        button_icon = QPixmap(button_icon_path)
        button.setIcon(button_icon)
        button.setIconSize(QSize(41, 41))
        button.setFixedSize(41, 41)
        button.setStyleSheet("background: transparent; border: none;")
        button.setObjectName(f"barangay_{community_data['Name']}_btn")

        button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

        hbox_layout.addWidget(picture_label)
        hbox_layout.addWidget(name_label)
        hbox_layout.addWidget(button)

        container_widget = QWidget()
        container_widget.setLayout(hbox_layout)

        layout.addWidget(container_widget)

    def add_new_shelter_to_ui(self, shelter_data, index):
        layout = self.verticalLayout_4.layout()

        hbox_layout = QHBoxLayout()

        picture_label = QLabel()
        icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128 (1).png")
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaled(31, 31)
        picture_label.setPixmap(pixmap)
        picture_label.setFixedSize(31, 31)

        name_label = QLabel(shelter_data["Name"])

        button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
        button = QPushButton()
        button_icon = QPixmap(button_icon_path)
        button.setIcon(button_icon)
        button.setIconSize(QSize(41, 41))
        button.setFixedSize(41, 41)
        button.setStyleSheet("background: transparent; border: none;")
        button.setObjectName(f"shelter_{shelter_data['Name']}_btn")

        button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

        hbox_layout.addWidget(picture_label)
        hbox_layout.addWidget(name_label)
        hbox_layout.addWidget(button)

        container_widget = QWidget()
        container_widget.setLayout(hbox_layout)

        layout.addWidget(container_widget)

    def add_marker_to_map(self, excel_file_path, marker_type):
        try:
            data = pd.read_excel(excel_file_path)

            if not data.empty:
                center_latitude = data.iloc[1]["xDegrees"]
                center_longitude = data.iloc[1]["yDegrees"]
                map = folium.Map(location=[center_latitude, center_longitude], zoom_start=12)
            else:
                map = folium.Map(location=[0,0], zoom_start=2)

            for index, row in data.iterrows():
                latitude = row.get("xDegrees", 1)
                longitude = row.get("yDegrees", 1)
                name = row.get("Name", "Unknown")

                if marker_type == "community":
                    color = 'green'
                elif marker_type == "shelter":
                    color = 'blue'
                else:
                    color = 'red'

                folium.Marker(
                    location=[latitude, longitude],
                    popup=name,
                    icon=folium.Icon(color=color)
                ).add_to(map)

            map_file_path = os.path.join(os.getcwd(), "optimized-routes-map.html")
            map.save(map_file_path)

            self.webEngineView.setUrl(QUrl.fromLocalFile(map_file_path))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update map: {e}")

    def add_switch(self, checkbox, is_active=False):
        # Get the layout of the parent widget
        layout = checkbox.parentWidget().layout()

        # Create the switch container widget
        switch_widget = QWidget()
        switch_layout = QHBoxLayout(switch_widget)
        switch_layout.setAlignment(Qt.AlignCenter)
        switch_layout.setContentsMargins(0, 0, 0, 0)


        # Create the switch
        switch = QPushButton()
        switch.setCheckable(True)
        switch.setChecked(is_active)
        switch.setFixedSize(38, 18)  # Set the switch size
        switch.setStyleSheet(
            "QPushButton { background-color: #4CAF50; border-radius: 8px; }" 
            if switch.isChecked() else 
            "QPushButton { background-color: #ccc; border-radius: 8px; }"
        )
        
        # Set an object name for the switch
        switch.setObjectName(checkbox.objectName().replace("checkBox", "switch"))

        # Create a circle (knob) for the switch
        knob = QPushButton(switch)
        knob.setFixedSize(14, 14)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 7px;
            }
        """)
        knob.move(22 if is_active else 2, 2)  # Initial position for the knob (left side)
        switch.knob = knob

        # Animation for toggling
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)

        # Connect the toggle functionality
        switch.clicked.connect(lambda: toggle_switch_animation())

        # Delegate knob clicks to the switch
        def knob_mouse_press(event):
            switch.click()  # Simulate a click on the switch
            super(knob.__class__, knob).mousePressEvent(event)

        knob.mousePressEvent = knob_mouse_press

        def toggle_switch_animation():
            if switch.isChecked():
                # Move knob to the right
                animation.setStartValue(QRect(2, 2, 16, 16))
                animation.setEndValue(QRect(22, 2, 16, 16))
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        border-radius: 8px;
                    }
                """)
            else:
                # Move knob to the left
                animation.setStartValue(QRect(22, 2, 16, 16))
                animation.setEndValue(QRect(2, 2, 16, 16))  # Reset to left side
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #ccc;
                        border-radius: 8px;
                    }
                """)
            animation.start()

        # Add the switch to the layout
        switch_layout.addWidget(switch)
        layout.replaceWidget(checkbox, switch_widget)  # Replace the checkbox with the switch
        checkbox.deleteLater()  # Remove the old checkbox
        switch.toggle_animation = toggle_switch_animation

        return switch

    def save_community_data_dashboard(self):
        print("yey")