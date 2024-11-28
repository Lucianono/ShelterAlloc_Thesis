import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl
from ui_entityManagement import Ui_EntityManagementCommunities
import pandas as pd
import os
from functools import partial

class EntityManagementComm(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_EntityManagementCommunities()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)

        file_name = "commData.xlsx"
        required_headers = ['Name', 'xDegrees', 'yDegrees', 'Population', 'AffectedPop', 'WorkPop', 'MaxDistance',  'Remarks']
        dummy_data = pd.DataFrame([['DummyName', 0.0, 0.0, 1000, 200, 800, 100, 'Sample remarks']], columns=required_headers)

        expected_types = {
            'Name': str,
            'xDegrees': float,
            'yDegrees': float,
            'Population': int,
            'AffectedPop': int,
            'WorkPop': int,
            'MaxDistance': float,
            'Remarks': str
        }

        self.load_from_excel(self.ui.communityInfo_table, file_name, dummy_data)

        self.ui.mc_back_btn.clicked.connect(self.close)
        self.ui.mc_cancel_changes_btn.clicked.connect(self.close)
        self.ui.mc_import_btn.clicked.connect(lambda: self.import_excel_data(self.ui.communityInfo_table,required_headers ,expected_types))
        self.ui.mc_save_changes_btn.clicked.connect(lambda: self.save_to_excel(self.ui.communityInfo_table, file_name, self ,expected_types))
        self.ui.mc_add_community_btn.clicked.connect(lambda: self.add_row(self.ui.communityInfo_table))

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


    def import_excel_data(self, table_widget, required_headers, expected_types):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            data = pd.read_excel(file_path).fillna("")
            
            if list(data.columns) != required_headers:
                QMessageBox.critical(self, "Error", "The imported Excel file does not have the correct headers.")
                print(list(data.columns))
                return
            
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

    def add_row(self, table_widget):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)
        self.add_checkbox(table_widget, row_position)

        for col in range(1, table_widget.columnCount() - 1):
            table_widget.setItem(row_position, col, QTableWidgetItem(""))

        self.add_delete_button(table_widget, row_position)

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
    
