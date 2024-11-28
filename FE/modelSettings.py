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

        expected_types = {
            "Generations": int,
            "Population": int,
            "WtCost": float,
            "WtDist": float,
            "Mutation": float,
            "MaxShelters": int,
            "MaxL2Shelters": int,
            "AreaPerIndiv": float,
            "Model": int
        }

        self.ui.modelSettings_back_btn.clicked.connect(self.close)
        self.ui.modelSettings_done_btn.clicked.connect(lambda: self.save_to_excel( "modelParam.xlsx", self ,expected_types))

        self.update_params_from_excel("modelParam.xlsx")

        print("Opened")


    def update_params_from_excel(self, excel_name):
        try:
            # get data from excel
            Model_params_data = pd.read_excel( os.path.join(os.getcwd(), excel_name), header=0).fillna("").iloc[0]
             
            self.ui.textEdit_generations.setPlainText(str(int(Model_params_data["Generations"])))
            self.ui.textEdit_population.setPlainText(str(int(Model_params_data["Population"])))
            self.ui.textEdit_wtCost.setPlainText(str(Model_params_data["WtCost"]))
            self.ui.textEdit_wtDist.setPlainText(str(Model_params_data["WtDist"]))
            self.ui.textEdit_mutation.setPlainText(str(Model_params_data["Mutation"]))
            self.ui.textEdit_maxShelters.setPlainText(str(int(Model_params_data["MaxShelters"])))
            self.ui.textEdit_maxL2Shelters.setPlainText(str(int(Model_params_data["MaxL2Shelters"])))
            self.ui.textEdit_areaPerIdniv.setPlainText(str(Model_params_data["AreaPerIndiv"]))
            self.ui.comboBox_modelType.setCurrentIndex(int(str(Model_params_data["Model"])))
            
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"File '{excel_name}' not found.")
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"Missing column in Excel: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")


    def save_to_excel(self, file_name, dialog, expected_types):
        try:
            # Collect data from the UI elements
            data = {
                "Generations": self.ui.textEdit_generations.toPlainText(),
                "Population": self.ui.textEdit_population.toPlainText(),
                "WtCost": self.ui.textEdit_wtCost.toPlainText(),
                "WtDist": self.ui.textEdit_wtDist.toPlainText(),
                "Mutation": self.ui.textEdit_mutation.toPlainText(),
                "MaxShelters": self.ui.textEdit_maxShelters.toPlainText(),
                "MaxL2Shelters": self.ui.textEdit_maxL2Shelters.toPlainText(),
                "AreaPerIndiv": self.ui.textEdit_areaPerIdniv.toPlainText(),
                "Model": self.ui.comboBox_modelType.currentIndex()
            }

            # Validate and convert data based on expected types
            validated_data = {}
            for key, value in data.items():
                if key in expected_types:
                    try:
                        # Convert the value to the expected type
                        validated_data[key] = expected_types[key](value) if value else None
                    except ValueError:
                        QMessageBox.warning(
                            self,
                            "Validation Error",
                            f"Invalid value for {key}. Expected {expected_types[key].__name__}.",
                        )
                        return
                else:
                    validated_data[key] = value  # If no type is expected, keep as-is

            # Save to Excel
            df = pd.DataFrame([validated_data])
            file_path = os.path.join(os.getcwd(), file_name)
            df.to_excel(file_path, index=False)
            dialog.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save to Excel: {e}")

        

        
