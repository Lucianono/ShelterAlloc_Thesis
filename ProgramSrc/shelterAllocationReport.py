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

        self.ui.pushButton_2.connect()

        self.load_table_data("allocation_results.xlsx")
        self.reload_label()

    def save_report(self):
        return

    def reload_label(self):
        model_results_path = os.path.join(os.getcwd(), "modelPerformanceResult.txt")
        with open(model_results_path, "r") as file:
            content = file.readlines()

        formatted_text = "<br>".join(line.strip() for line in content)
        self.ui.label_4.setText(formatted_text)

    def load_table_data(self, file_path):
        try:
            df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
            if df.empty:
                QMessageBox.warning(self, "Warning", "The file is empty.")
                return

            self.ui.tableWidget.setRowCount(df.shape[0])  # Set number of rows
            self.ui.tableWidget.setColumnCount(df.shape[1])  # Set number of columns
            self.ui.tableWidget.setHorizontalHeaderLabels(["Community","Shelter Allocated","Level"])  # Set column headers

            self.ui.tableWidget.setColumnWidth(0,150)
            self.ui.tableWidget.setColumnWidth(1,170)
            self.ui.tableWidget.setColumnWidth(2,30)

            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iloc[row, col]))
                    self.ui.tableWidget.setItem(row, col, item)  # Insert item into the table

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {str(e)}")


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)  # Create application instance
    window = ShelterAllocationReport()  # Create an instance of your dialog
    window.show()  # Show the window
    sys.exit(app.exec())  # Start event loop