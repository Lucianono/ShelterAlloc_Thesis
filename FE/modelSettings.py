import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl
from ui_modelSettings import Ui_modelSettings
import pandas as pd
import os
from functools import partial

class ModelSettings(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_modelSettings()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)

        self.ui.modelSettings_back_btn.clicked.connect(self.close)
        self.ui.modelSettings_done_btn.clicked.connect(self.close)

        self.update_params_from_excel("modelParam.xlsx")

        print("Opened")

    def update_params_from_excel(self, excel_name):
        try:
            # get data from excel
            Model_params_data = pd.read_excel( os.path.join(os.getcwd(), excel_name), header=0).fillna("").iloc[0] 
            print(Model_params_data["Model"])


        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File '{excel_name}' not found.")
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"Missing column in Excel: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

        
        
