from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtGui import QAction, QColor, QIcon, QCursor
from PySide6.QtCore import Qt, QUrl
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

        map_path = self.create_map()
        self.webEngineView.setUrl(QUrl.fromLocalFile(map_path))

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

    def create_map(self):
        map_path = os.path.join(os.getcwd(), "map.html")

        if os.path.exists(map_path):
            print(f"Map already exists at: {map_path}")
        else:
            m = folium.Map(location=[14.7919, 120.7350], zoom_start=13)

            start = (14.833799, 120.734049)
            end = (14.836125, 120.733770)

            G = ox.graph_from_point(start, dist=3000, network_type='all')
            print("number of nodes in graph:", len(G.nodes))
            print("Number of edges in graph:", len(G.edges))

            G_projected = ox.project_graph(G)

            start_node = ox.distance.nearest_nodes(G_projected, start[1], start[0])
            end_node = ox.distance.nearest_nodes(G_projected, end[1], end[0])

            path = nx.shortest_path(G, start_node, end_node, weight='length')
            print("path nodes:", path)
            path_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in path]
            print("Path coordinates:", path_coords)
            folium.PolyLine(locations=path_coords, color='red', weight=5, opacity=1).add_to(m)
            
            folium.Marker(location=start, popup='Start', icon=folium.Icon(color='green')).add_to(m)
            folium.Marker(location=end, popup='End', icon=folium.Icon(color='red')).add_to(m)
            m.save(map_path)
            print(f"New map created and saved at: {map_path}")

        return map_path

    def open_solve_settings_dialog(self):
        self.solveSettings_Window = SolveSettingsDialog()
        self.solveSettings_Window.show()

