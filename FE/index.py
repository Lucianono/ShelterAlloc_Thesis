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
        addEMC_dialog = Ui_EntityManagementCommunities()
        addEMC_dialog.setupUi(dialog)

        self.load_from_excel(addEMC_dialog.communityInfo_table)

        addEMC_dialog.mc_back_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_cancel_changes_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_import_btn.clicked.connect(lambda: self.import_excel_data(addEMC_dialog.communityInfo_table))
        addEMC_dialog.mc_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMC_dialog.communityInfo_table))
        addEMC_dialog.mc_add_community_btn.clicked.connect(lambda: self.add_row(addEMC_dialog.communityInfo_table))

        dialog.exec()

    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        dialog = QDialog(self)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)

        addEMS_dialog.ms_back_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_cancel_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_import_btn.clicked.connect(lambda: self.import_excel_data(addEMS_dialog.shelterInfo_table))
        addEMS_dialog.ms_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMS_dialog.shelterInfo_table))
        addEMS_dialog.ms_add_shelter_btn.clicked.connect(lambda: self.add_row(addEMS_dialog.shelterInfo_table))

        dialog.exec()

    def import_excel_data(self, table_widget):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            data = pd.read_excel(file_path).fillna("")
            required_headers = ['Name', 'xDegrees', 'yDegrees', 'Population', 'VulPop', 'WorkPop', 'Remarks']
            
            if list(data.columns) != required_headers:
                QMessageBox.critical(self, "Error", "The imported Excel file does not have the correct headers.")
                return

            self.populate_table(table_widget, data)

    def save_to_excel(self, table_widget):
        data = []
        headers = [table_widget.horizontalHeaderItem(col).text() for col in range(1, table_widget.columnCount() - 1)]
        
        for row in range(table_widget.rowCount()):
            row_data = [table_widget.item(row, col).text() if table_widget.item(row, col) else "" for col in range(1, table_widget.columnCount() - 1)]
            data.append(row_data)

        if data:
            dataframe = pd.DataFrame(data, columns=headers)
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)")
            if file_path:
                try:
                    dataframe.to_excel(file_path, index=False)
                    QMessageBox.information(self, "Success", f"File saved successfully as {file_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
            else:
                QMessageBox.warning(self, "Warning", "Save canceled.")
        else:
            QMessageBox.warning(self, "Warning", "No data to save.")

    def load_from_excel(self, table_widget):
        if self.file_path and os.path.exists(self.file_path):
            try:
                data = pd.read_excel(self.file_path).fillna("")
                self.populate_table(table_widget, data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

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
            m = folium.Map(location=[14.7919, 120.7350], zoom_start=13).add_child(
                folium.ClickForMarker("Julius Ian Dino")
            )
            m.save(map_path)
            print(f"New map created and saved at: {map_path}")

        return map_path
