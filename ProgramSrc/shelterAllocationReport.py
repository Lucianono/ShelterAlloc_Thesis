import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QTextEdit
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl, QThread
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from ui_shelterallocationreport import Ui_ShelterAllocationReport
import pandas as pd
import os
from functools import partial
from pathfinder import PathfindingWorker
from optimizedRouting import run_optimization

class ShelterAllocationReport(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_ShelterAllocationReport()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)



        self.map_path = os.path.join(os.getcwd(), "all_routes_map.html")
        self.ui.webEngineView.setUrl(QUrl.fromLocalFile(self.map_path))

        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        self.load_table_data("allocation_results.xlsx")

    def load_table_data(self, file_path):
        try:
            df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
            if df.empty:
                QMessageBox.warning(self, "Warning", "The file is empty.")
                return

            self.ui.tableWidget.setRowCount(df.shape[0])  # Set number of rows
            self.ui.tableWidget.setColumnCount(df.shape[1])  # Set number of columns
            self.ui.tableWidget.setHorizontalHeaderLabels(df.columns)  # Set column headers

            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iloc[row, col]))
                    self.ui.tableWidget.setItem(row, col, item)  # Insert item into the table

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {str(e)}")
