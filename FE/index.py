from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication
from PySide6.QtGui import QAction, QColor, QIcon, QCursor
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from functools import partial
from ui_dashboard import Ui_MainWindow
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

        self.menu = QMenu(self)
        self.show()

        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

    def open_entitymanagement_dialog(self):
        from ui_entityManagement import Ui_EntityManagementCommunities

        dialog = QDialog(self)
        file_name = "commData.xlsx"
        required_headers = ['Name', 'xDegrees', 'yDegrees', 'Population', 'VulPop', 'WorkPop', 'Remarks']
        dummy_data = pd.DataFrame([['DummyName', 0.0, 0.0, 1000, 200, 800, 'Sample remarks']], columns=required_headers)
        addEMC_dialog = Ui_EntityManagementCommunities()
        addEMC_dialog.setupUi(dialog)

        expected_types = {
            'Name': str,
            'xDegrees': float,
            'yDegrees': float,
            'Population': int,
            'VulPop': int,
            'WorkPop': int,
            'Remarks': str
        }

        self.load_from_excel(addEMC_dialog.communityInfo_table, file_name, dummy_data)

        addEMC_dialog.mc_back_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_cancel_changes_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_import_btn.clicked.connect(lambda: self.import_excel_data(addEMC_dialog.communityInfo_table,required_headers ,expected_types))
        addEMC_dialog.mc_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMC_dialog.communityInfo_table, file_name, dialog ,expected_types))
        addEMC_dialog.mc_add_community_btn.clicked.connect(lambda: self.add_row(addEMC_dialog.communityInfo_table))

        dialog.exec()

    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        dialog = QDialog(self)
        file_name = "shelData.xlsx"
        required_headers = ['Name', 'xDegrees', 'yDegrees', 'Area1', 'Cost1', 'Area2', 'Cost2', 'ResToFlood', 'ResToTyphoon', 'ResToEarthquake', 'Status', 'Remarks']
        dummy_data = pd.DataFrame([['DummyName', 0.0, 0.0, 500, 1000, 300, 1500, True, False, True, 'Built', 'Sample remarks']], columns=required_headers)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)

        expected_types = {
            'Name': str,
            'xDegrees': float,
            'yDegrees': float,
            'Area1': float,
            'Cost1': float,
            'Area2': float,
            'Cost2': float,
            'ResToFlood': bool,
            'ResToTyphoon': bool,
            'ResToEarthquake': bool,
            'Status': str,
            'Remarks': str
        }


        self.load_from_excel(addEMS_dialog.shelterInfo_table, file_name, dummy_data)

        addEMS_dialog.ms_back_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_cancel_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_import_btn.clicked.connect(lambda: self.import_excel_data(addEMS_dialog.shelterInfo_table,required_headers, expected_types))
        addEMS_dialog.ms_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMS_dialog.shelterInfo_table, file_name, dialog, expected_types))
        addEMS_dialog.ms_add_shelter_btn.clicked.connect(lambda: self.add_row(addEMS_dialog.shelterInfo_table))

        dialog.exec()

    def import_excel_data(self, table_widget, required_headers, expected_types):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            data = pd.read_excel(file_path).fillna("")
            
            if list(data.columns) != required_headers:
                QMessageBox.critical(self, "Error", "The imported Excel file does not have the correct headers.")
                return
            
            print(list(data.columns) )
            
            try:
                self.validate_imported_data(data, expected_types)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to display file: {e}")
                return

            self.populate_table(table_widget, data)
            

    def save_to_excel(self, table_widget, file_name, dialog, expected_types):
        data = []
        headers = [table_widget.horizontalHeaderItem(col).text() for col in range(1, table_widget.columnCount() - 1)]
        
        for row in range(table_widget.rowCount()):
            row_data = [table_widget.item(row, col).text() if table_widget.item(row, col) else "" for col in range(1, table_widget.columnCount() - 1)]
            data.append(row_data)

        if data:
            dataframe = pd.DataFrame(data, columns=headers)
            # validate table first
            try:
                self.validate_imported_data(dataframe, expected_types)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to display file: {e}")
                return
            # save the table here 
            file_path = os.path.join(os.getcwd(), file_name)
            if file_path:
                try:
                    dataframe.to_excel(file_path, index=False)
                    QMessageBox.information(self, "Success", f"File saved successfully as {file_path}")
                    dialog.close()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            else:
                QMessageBox.warning(self, "Warning", "Save canceled.")
        else:
            QMessageBox.warning(self, "Warning", "No data to save.")

    def load_from_excel(self, table_widget, file_name, dummy_data):
        if file_name and os.path.exists( os.path.join(os.getcwd(), file_name) ):
            try:
                data = pd.read_excel( os.path.join(os.getcwd(), file_name) ).fillna("")
                self.populate_table(table_widget, data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
        else:
            self.populate_table(table_widget, dummy_data)

    def validate_imported_data(self, data, expected_types):
        
        for column, expected_type in expected_types.items():
            if column not in data.columns:
                raise ValueError(f"Missing expected column: {column}")

            for idx, value in enumerate(data[column]):
                if pd.isnull(value):
                    continue  # Skip NaN values
                
                # Check if the value is of the expected type
                if expected_type == str:
                    if not isinstance(value, str):
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. Expected a string.")
                elif expected_type == float:
                    try:
                        float(value)  # Try converting to float
                    except ValueError:
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. Expected a float.")
                elif expected_type == int:
                    try:
                        int(value)  # Try converting to int
                    except ValueError:
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. Expected an integer.")
                elif expected_type == bool:
                    if not isinstance(value, bool):
                        # Optionally, you could also allow values like 0/1 to be cast to bool:
                        bool_value = bool(int(value)) if value in [0, 1] else bool(value)
                        if bool_value not in [0, 1, True, False]:
                            raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. Expected a boolean.")

    def populate_table(self, table_widget, data):
        table_widget.setRowCount(0)
        table_widget.setColumnCount(len(data.columns) + 2)
        table_widget.setHorizontalHeaderLabels(['Select'] + list(data.columns) + ['Delete'])

        for row_idx, row_data in data.iterrows():
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            self.add_checkbox(table_widget, row_position)
            
            for col_idx, value in enumerate(row_data, start=1):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(row_position, col_idx, item)
            
            self.add_delete_button(table_widget, row_position)

        table_widget.resizeColumnsToContents()

    def add_checkbox(self, table_widget, row_position):
        check_box_widget = QWidget()
        layout = QHBoxLayout(check_box_widget)
        layout.setAlignment(Qt.AlignCenter)
        check_box_widget.setLayout(layout)
        checkbox = QCheckBox()
        layout.addWidget(checkbox)
        layout.setContentsMargins(0, 0, 0, 0)
        table_widget.setCellWidget(row_position, 0, check_box_widget)

    def add_delete_button(self, table_widget, row_position):
        delete_btn_widget = QWidget()
        delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
        layout = QHBoxLayout(delete_btn_widget)
        layout.setAlignment(Qt.AlignCenter)
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon("ICONS/9022869_duotone_trash.png"))
        delete_btn.setFixedSize(20, 20)
        delete_btn.clicked.connect(partial(self.delete_row, table_widget, row_position))
        layout.addWidget(delete_btn)
        layout.setContentsMargins(0, 0, 0, 0)
        delete_btn_widget.setLayout(layout)
        table_widget.setCellWidget(row_position, table_widget.columnCount() - 1, delete_btn_widget)

    def delete_row(self, table_widget, row_position):
        response = QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this row?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            table_widget.removeRow(row_position)
            self.reconnect_delete_buttons(table_widget)

    def add_row(self, table_widget):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)
        self.add_checkbox(table_widget, row_position)

        for col in range(1, table_widget.columnCount() - 1):
            table_widget.setItem(row_position, col, QTableWidgetItem(""))

        self.add_delete_button(table_widget, row_position)

    def reconnect_delete_buttons(self, table_widget):
        for row in range(table_widget.rowCount()):
            delete_btn_widget = table_widget.cellWidget(row, table_widget.columnCount() - 1)
            if delete_btn_widget:
                delete_btn = delete_btn_widget.findChild(QPushButton)
                delete_btn.clicked.disconnect()
                delete_btn.clicked.connect(partial(self.delete_row, table_widget, row))

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
