from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtGui import QAction, QColor, QIcon, QCursor
from PySide6.QtCore import Qt, QUrl, QTimer
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