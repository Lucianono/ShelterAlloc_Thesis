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


