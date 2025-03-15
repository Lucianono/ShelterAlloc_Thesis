import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QPlainTextEdit
from PySide6.QtGui import QIcon, QCursor, QKeyEvent
from PySide6.QtCore import Qt, QUrl, QEvent, QObject
from ui_modelSettings import Ui_modelSettings
import pandas as pd
import os
from functools import partial

class ModelSettings(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_modelSettings()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)
        self.setModal(True)
        self.setWindowTitle("Model Settings")
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS", "logo.png")))
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        text_fields = [
            self.ui.textEdit_generations,
            self.ui.textEdit_population,
            self.ui.textEdit_wtCost,
            self.ui.textEdit_wtDist,
            self.ui.textEdit_mutation,
            self.ui.textEdit_maxShelters,
            self.ui.textEdit_maxL2Shelters,
            self.ui.textEdit_areaPerIndiv
        ]

        for field in text_fields:
            field.installEventFilter(self)

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

        self.ui.modelSettings_done_btn.setAutoDefault(False)
        self.ui.modelSettings_done_btn.setDefault(False)

        self.update_params_from_excel("modelParam.xlsx")

        print("Opened")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() in {Qt.Key_Return, Qt.Key_Enter}:
            obj.clearFocus()  # Unselect the field
            return True  # Mark event as handled (no new line added)
        return super().eventFilter(obj, event)    
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()  # Prevent the dialog from closing
        else:
            super().keyPressEvent(event)


    def update_params_from_excel(self, excel_name):
        try:
            updated = False

            # get data from excel
            excel_path = os.path.join(self.save_dir, excel_name)

            if os.path.exists(excel_path):
                Model_params_data = pd.read_excel(excel_path, header=0)

            shel_file = "shelData.xlsx"
            shel_path = os.path.join(self.save_dir, shel_file)
            default_shelter_count = 0

            if os.path.exists(shel_path):
                try:
                    shel_data = pd.read_excel(shel_path, header=None)
                    first_column = shel_data.iloc[:, 0]
                    default_shelter_count = (first_column.astype(str).str.upper() == "TRUE").sum()
                except Exception as e:
                    QMessageBox.warning(self, "Warning", f"Could not process {shel_file}: {e}")

            if "MaxShelters" in Model_params_data.columns:
                Model_params_data.at[0, "MaxShelters"] = default_shelter_count
                updated = True
            if "MaxL2Shelters" in Model_params_data.columns:
                Model_params_data.at[0, "MaxL2Shelters"] = default_shelter_count
                updated = True

            if updated:
                Model_params_data.to_excel(excel_path, index=False)
                    
             
            self.ui.textEdit_generations.setPlainText(str(int(Model_params_data.at[0, "Generations"])))
            self.ui.textEdit_population.setPlainText(str(int(Model_params_data.at[0, "Population"])))
            self.ui.textEdit_wtCost.setPlainText(str(Model_params_data.at[0, "WtCost"]))
            self.ui.textEdit_wtDist.setPlainText(str(Model_params_data.at[0, "WtDist"]))
            self.ui.textEdit_mutation.setPlainText(str(Model_params_data.at[0, "Mutation"]))
            self.ui.textEdit_maxShelters.setPlainText(str(int(Model_params_data.at[0, "MaxShelters"])))
            self.ui.textEdit_maxL2Shelters.setPlainText(str(int(Model_params_data.at[0, "MaxL2Shelters"])))
            self.ui.textEdit_areaPerIndiv.setPlainText(str(Model_params_data.at[0, "AreaPerIndiv"]))
            self.ui.comboBox_modelType.setCurrentIndex(int(Model_params_data.at[0, "Model"]))
            
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
                "AreaPerIndiv": self.ui.textEdit_areaPerIndiv.toPlainText(),
                "Model": self.ui.comboBox_modelType.currentIndex()
            }

            # Validate and convert data based on expected types
            for key,value in data.items():
               # Check if the value is of the expected type
                if expected_types[key] == str:
                    if not isinstance(value, str):
                        raise ValueError(f"Invalid value '{value}' for '{key}'. Expected a string.")
                elif expected_types[key] == float:
                    try:
                        data[key] = float(value)  # Try converting to float
                        if key in ["Mutation", "AreaPerIndiv"]:
                            if data[key] <= 0:
                                QMessageBox.warning(self, "Invalid Input", f"'{key}' must be greater than 0.")
                                return
                    except ValueError:
                        raise ValueError(f"Invalid value '{value}' for '{key}' . Expected a float.")
                elif expected_types[key] == int:
                    try:
                        data[key] = int(value)  # Try converting to int
                        if key in ["Generations", "Population", "MaxShelters", "MaxL2Shelters"]:
                            if data[key] <= 0:
                                QMessageBox.warning(self, "Invalid Input", f"'{key}' must be greater than 0.")
                                return
                    except ValueError:
                        raise ValueError(f"Invalid value '{value}' for '{key}'. Expected an integer.")
                    
            if not abs((data["WtCost"] + data["WtDist"]) - 1.0) < 1e-6:
                QMessageBox.warning(self, "Invalid Input", "WtCost + WtDist must equal 1.0")
                return


            # Save to Excel
            df = pd.DataFrame([data])
            file_path = os.path.join(self.save_dir, file_name)
            df.to_excel(file_path, index=False)
            dialog.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save to Excel: {e}")
