from PySide6.QtWidgets import QLabel, QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtGui import QAction, QColor, QIcon, QCursor, QPixmap
from PySide6.QtCore import Qt, QUrl, QTimer, QSize
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
        
        self.add_community_btn.clicked.connect(self.handle_add_community)
        self.add_shelter_btn.clicked.connect(self.handle_add_shelter)

        self.load_comm_data()
        self.load_shel_data()

        self.data = pd.read_excel(os.path.join(os.getcwd(), "commData.xlsx"), skiprows=1)
        self.shel_data = pd.read_excel(os.path.join(os.getcwd(), "shelData.xlsx"), skiprows=1)

        #for value in self.data.iloc[:, 0]:
         #   button = self.findChild(QPushButton, f"barangay_{value}_btn")
          #  if button:
           #     button.clicked.connect(lambda checked, value=value: self.handle_button_click(value))

        self.barangay_a_btn.clicked.connect(self.unhide_stacked_widget)

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

        self.menu = QMenu(self)
        self.show()

        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

    def open_entitymanagement_dialog(self):
        self.entityManagementComm_Window = EntityManagementComm()
        self.entityManagementComm_Window.show()

    def open_entitymanagement_shelter_dialog(self):
        self.entityManagementShelter_Window = EntityManagementShelter()
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
        try:
            file_path = os.path.join(os.getcwd(), "commData.xlsx")
            self.data = pd.read_excel(file_path, usecols=[0], skiprows=[0])

            layout = self.communities_dropdown.layout()

            for index, value in self.data.iloc[:, 0].items():
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128.png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(31, 31)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(31, 31)

                name_label = QLabel(str(value))

                button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(41, 41))

                button.setFixedSize(41, 41)

                button.setStyleSheet("background: transparent; border: none;")

                button.setObjectName(f"barangay_{value}_btn")

                button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

                hbox_layout.addWidget(picture_label)
                hbox_layout.addWidget(name_label)
                hbox_layout.addWidget(button)

                container_widget = QWidget()
                container_widget.setLayout(hbox_layout)

                layout.addWidget(container_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")

    def load_shel_data(self):
        try:
            file_path = os.path.join(os.getcwd(), "shelData.xlsx")
            self.shel_data = pd.read_excel(file_path, usecols=[0], skiprows=[0])

            layout = self.verticalLayout_4.layout()

            for index, value in self.shel_data.iloc[:, 0].items():
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                icon_path = os.path.join(os.getcwd(), "ICONS", "pin-5-128 (1).png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(31, 31)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(31, 31)

                name_label = QLabel(str(value))

                button_icon_path = os.path.join(os.getcwd(), "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(41, 41))

                button.setFixedSize(41, 41)

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
            row = self.data[self.data.iloc[:, 0] == value].index[0]

            self.label_18.setText(str(self.data.iloc[row, 0]))

            self.plainTextEdit.setPlainText(str(self.data.iloc[row, 1]))
            self.plainTextEdit_2.setPlainText(str(self.data.iloc[row, 2]))
            self.plainTextEdit_3.setPlainText(str(self.data.iloc[row, 3]))
            self.plainTextEdit_4.setPlainText(str(self.data.iloc[row, 4]))
            self.plainTextEdit_5.setPlainText(str(self.data.iloc[row, 5]))
            self.plainTextEdit_6.setPlainText(str(self.data.iloc[row, 6]))

        elif button_name.startswith("shelter_"):
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.page_2.show()
            self.page.hide()
            row = self.shel_data[self.shel_data.iloc[:, 0] == value].index[0]

            self.label_31.setText(str(self.shel_data.iloc[row, 0]))

            self.plainTextEdit_11.setPlainText(str(self.shel_data.iloc[row, 1]))
            self.plainTextEdit_10.setPlainText(str(self.shel_data.iloc[row, 2]))
            self.plainTextEdit_8.setPlainText(str(self.shel_data.iloc[row, 3]))
            self.plainTextEdit_12.setPlainText(str(self.shel_data.iloc[row, 4]))
            self.plainTextEdit_13.setPlainText(str(self.shel_data.iloc[row, 5]))
            self.plainTextEdit_14.setPlainText(str(self.shel_data.iloc[row, 6]))

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

            self.add_marker_to_map(x_degrees, y_degrees, new_data["Name"], "community")

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

            self.add_marker_to_map(new_data["xDegrees"], new_data["yDegrees"], new_data["Name"], "shelter")

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

    def add_marker_to_map(self, latitude, longitude, name, marker_type):
        try:
            map_file_path = os.path.join(os.getcwd(), "optimized-routes-map.html")

            if os.path.exists(map_file_path):
                with open(map_file_path, "r") as f:
                    map_html = f.read()
                map = folium.Map(location=[latitude, longitude], zoom_start=12)
            else:
                map = folium.Map(location=[latitude, longitude], zoom_start=12)

            if marker_type == "community":
                color = 'green'
            elif marker_type == "shelter":
                color = 'blue'

            folium.Marker(
                location=[latitude, longitude],
                popup=name,
                icon=folium.Icon(color)
            ).add_to(map)

            map.save(map_file_path)
            self.webEngineView.setUrl(QUrl.fromLocalFile(map_file_path))
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update map: {e}")


