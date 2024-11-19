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
             
            self.ui.textEdit_generations.setPlainText(str(Model_params_data["Generations"]))
            self.ui.textEdit_population.setPlainText(str(Model_params_data["Population"]))
            self.ui.textEdit_wtCost.setPlainText(str(Model_params_data["WtCost"]))
            self.ui.textEdit_wtDist.setPlainText(str(Model_params_data["WtDist"]))
            self.ui.textEdit_mutation.setPlainText(str(Model_params_data["Mutation"]))
            self.ui.textEdit_maxShelters.setPlainText(str(Model_params_data["MaxShelters"]))
            self.ui.textEdit_maxL2Shelters.setPlainText(str(Model_params_data["MaxL2Shelters"]))
            self.ui.textEdit_areaPerIdniv.setPlainText(str(Model_params_data["AreaPerIndiv"]))
            self.ui.comboBox_modelType.setCurrentIndex(int(Model_params_data["Model"]))

            


        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File '{excel_name}' not found.")
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"Missing column in Excel: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

        
        
