import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon, QCursor,QShortcut, QKeySequence, QKeyEvent
from PySide6.QtCore import Signal, Qt, QUrl, QPropertyAnimation, QRect, QObject
from ui_entityManagement import Ui_EntityManagementCommunities
import pandas as pd
import os
from functools import partial



class EntityManagementComm(QDialog):
    
    changes_saved = Signal()

    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_EntityManagementCommunities()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)
        self.setModal(True)
        self.setWindowTitle("Entity Management Community")
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        try:
            icon_path = os.path.join(sys._MEIPASS, "ICONS", "logo.png")
        except AttributeError:
            icon_path = os.path.join(os.path.dirname(__file__), "ICONS", "logo.png")
        self.setWindowIcon(QIcon(icon_path))
        self.setAttribute(Qt.WA_DeleteOnClose)


        file_name = "commData.xlsx"
        required_headers = ['Name', 'Latitude', 'Longitude', 'Population', 'AffectedPop', 'MaxDistance',  'Remarks']
        dummy_data = pd.DataFrame([['DummyName', 0.0, 0.0, 1000, 200, 100, 'Sample remarks']], columns=required_headers)

        expected_types = {
            'Name': str,
            'Latitude': float,
            'Longitude': float,
            'Population': int,
            'AffectedPop': int,
            'MaxDistance': float,
            'Remarks': str
        }

        self.load_from_excel(self.ui.communityInfo_table, file_name, dummy_data)

        self.ui.mc_back_btn.clicked.connect(self.close)
        self.ui.mc_cancel_changes_btn.clicked.connect(self.close)
        self.ui.mc_import_btn.clicked.connect(lambda: self.import_excel_data(self.ui.communityInfo_table,required_headers ,expected_types))
        self.ui.mc_save_changes_btn.clicked.connect(lambda: self.save_to_excel(self.ui.communityInfo_table, file_name, self , required_headers ,expected_types))
        self.ui.mc_add_community_btn.clicked.connect(lambda: self.add_row(self.ui.communityInfo_table))
        self.ui.mc_export_btn.clicked.connect(lambda: self.export_excel_data(dummy_data))    

        self.shortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.shortcut.activated.connect(lambda: self.toggle_all_switches(self.ui.communityInfo_table))

    def load_from_excel(self, table_widget, file_name, dummy_data):
        file_path = os.path.join(self.save_dir, file_name)
        if os.path.exists(file_path):
            try:
                data = pd.read_excel(os.path.join(self.save_dir, file_name)).fillna("")
                self.populate_table(table_widget, data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")
        else:
            self.populate_table(table_widget, dummy_data)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()  # Prevent the dialog from closing
        else:
            super().keyPressEvent(event)

    def validate_imported_data(self, data, expected_types):
        
        for column, expected_type in expected_types.items():
            if column not in data.columns:
                raise ValueError(f"Missing expected column: {column}")

            for idx, value in enumerate(data[column]):

                # Ensure value is a string before calling .strip()
                if isinstance(value, str):
                    value = value.strip()

                if (pd.isnull(value) or value == '') and column != "Remarks":
                    raise ValueError(f"No data found in column '{column}' at row {idx + 1}. Please provide a value.")
                
                # Check if the value is of the expected type
                if expected_type == str:
                    if not isinstance(value, str):
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. This should be text.")
                elif expected_type == float:
                    try:
                        float(value)  # Try converting to float
                    except ValueError:
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. This should be a number with decimals.")
                elif expected_type == int:
                    try:
                        int(value)  # Try converting to int
                    except ValueError:
                        raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. This should be a number.")
                elif expected_type == bool:
                    if not isinstance(value, bool):
                        # Optionally, you could also allow values like 0/1 to be cast to bool:
                        if value.lower() in {"true", "false"}:
                            value = value.lower() == "true"
                        elif str(value) in {"0", "1"}:
                            value = bool(int(value))
                        else:
                            raise ValueError(f"Invalid data type in column '{column}' at row {idx + 1}. This should be true or false.")
        
        # Check for duplicate values in the "Name" column
        if "Name" in data.columns:
            duplicate_names = data["Name"][data["Name"].duplicated()]
            if not duplicate_names.empty:
                raise ValueError(f"Duplicate entries found in the 'Name' column: {', '.join(duplicate_names)}")
                        

    def import_excel_data(self, table_widget, required_headers, expected_types):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            data = pd.read_excel(file_path).fillna("")
            
            if list(data.columns) != required_headers:
                QMessageBox.critical(self, "Error", f"The imported Excel file does not have the correct headers. {required_headers}")
                print(list(data.columns))
                return
            
            try:
                self.validate_imported_data(data, expected_types)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to display file: {e}")
                return

            self.populate_table(table_widget, data)
    def export_excel_data(self, dummy_data):
        default_file_name = os.path.join(self.save_dir, "dummy_data_community.xlsx")
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel File", default_file_name, "Excel Files (*.xlsx)")

        if file_path:
            try:
                if not file_path.endswith(".xlsx"):
                    file_path += ".xlsx"

                dummy_data.to_excel(file_path, index=False)

                QMessageBox.information(self, "Success", "Dummy data exported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export file: {e}")
            
    def save_to_excel(self, table_widget, file_name, dialog, required_headers, expected_types):
        data = []
        
        headers = ['Active'] + required_headers
        
        for row in range(table_widget.rowCount()):
            switch_button = table_widget.cellWidget(row, 0)
            if switch_button:
                active_switch = switch_button.findChild(QPushButton)
                is_active = active_switch.isChecked() if active_switch else False
            else:
                is_active = False
            row_data = [table_widget.item(row, col).text().strip() if table_widget.item(row, col) else "" for col in range(1, table_widget.columnCount() - 1)]
            row_data = [is_active] + row_data
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
            file_path = os.path.join(self.save_dir, file_name)
            if file_path:
                try:
                    dataframe.to_excel(file_path, index=False)
                    self.changes_saved.emit()
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
        self.add_switch(table_widget, row_position)

        for col in range(1, table_widget.columnCount() - 1):
            table_widget.setItem(row_position, col, QTableWidgetItem(""))

        self.add_delete_button(table_widget, row_position)

    def populate_table(self, table_widget, data):
        table_widget.setRowCount(0)

        hadActiveColumn = True
        headers = [
            "Active", "Name", "Latitude", "Longitude", 'Population', 'AffectedPop', 'MaxDistance (m)', "Remarks", "Delete"
        ]

        if "Active" not in data.columns:
            hadActiveColumn = False
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in data.iterrows():
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            is_active = row_data.get('Active', True) == True
            self.add_switch(table_widget, row_position, is_active)
            
            #remove Active if Active already exists
            if hadActiveColumn:
                row_data = row_data[1:] 

            for col_idx, value in enumerate(row_data, start=1):
                item = QTableWidgetItem(str(value))
                table_widget.setItem(row_position, col_idx, item)
            
            self.add_delete_button(table_widget, row_position)

        table_widget.resizeColumnsToContents()

    def add_switch(self, table_widget, row_position, is_active=False):
        switch_widget = QWidget()
        layout = QHBoxLayout(switch_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the switch
        switch = QPushButton()
        switch.setCheckable(True)
        switch.setChecked(is_active)
        switch.setFixedSize(38, 18)  # Set the switch size
        switch.setStyleSheet(
            "QPushButton { background-color: #4CAF50; border-radius: 8px; }" 
            if switch.isChecked() else 
            "QPushButton { background-color: #ccc; border-radius: 8px; }"
        )

        # Create a circle (knob) for the switch
        knob = QPushButton(switch)
        knob.setFixedSize(14, 14)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 7px;
            }
        """)
        knob.move(22 if is_active else 2, 2)  # Initial position for the knob (left side)
        if switch.isChecked():
            switch.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    border-radius: 8px;
                }
            """)

        # Create a unique animation instance for this switch
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)

        # Connect the toggle functionality
        switch.clicked.connect(lambda: self.toggle_switch_animation(switch, knob, animation))

        # Delegate knob clicks to the switch
        def knob_mouse_press(event):
            switch.click()  # Simulate a click on the switch
            super(knob.__class__, knob).mousePressEvent(event)

        knob.mousePressEvent = knob_mouse_press

        # Add the switch to the layout
        layout.addWidget(switch)
        table_widget.setCellWidget(row_position, 0, switch_widget)

    def toggle_switch_animation(self, switch, knob, animation):
        if switch.isChecked():
            # Move knob to the right
            animation.setStartValue(QRect(2, 2, 16, 16))
            animation.setEndValue(QRect(22, 2, 16, 16))
            switch.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    border-radius: 8px;
                }
            """)
        else:
            # Move knob to the left
            animation.setStartValue(QRect(22, 2, 16, 16))
            animation.setEndValue(QRect(2, 2, 16, 16))  # Reset to left side
            switch.setStyleSheet("""
                QPushButton {
                    background-color: #ccc;
                    border-radius: 8px;
                }
            """)
        animation.start()


    def add_delete_button(self, table_widget, row_position):
        delete_btn_widget = QWidget()
        delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
        layout = QHBoxLayout(delete_btn_widget)
        layout.setAlignment(Qt.AlignCenter)
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS/9022869_duotone_trash.png")))
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

    def reconnect_delete_buttons(self, table_widget):
        for row in range(table_widget.rowCount()):
            delete_btn_widget = table_widget.cellWidget(row, table_widget.columnCount() - 1)
            if delete_btn_widget:
                delete_btn = delete_btn_widget.findChild(QPushButton)
                delete_btn.clicked.disconnect()
                delete_btn.clicked.connect(partial(self.delete_row, table_widget, row))

    def toggle_all_switches(self, table_widget):
        if table_widget.rowCount() == 0:
            return
        
        state = table_widget.cellWidget(0, 0).findChild(QPushButton).isChecked()

        for row in range(table_widget.rowCount()):
            if state is table_widget.cellWidget(row, 0).findChild(QPushButton).isChecked(): 
                table_widget.cellWidget(row, 0).findChild(QPushButton).click()

