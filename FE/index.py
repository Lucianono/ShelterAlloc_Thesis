from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QPushButton, QMessageBox
from PySide6.QtGui import QAction, QColor, QIcon, QCursor
from PySide6.QtCore import Qt
from functools import partial
from ui_dashboard import Ui_MainWindow
import pandas as pd
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dashboard")

        self.file_path = os.path.join(os.path.expanduser("~"), "Documents", "CommunityData.xlsx")
        #buttons on the bashboard
        self.advanced_settings_com.clicked.connect(self.open_entitymanagement_dialog)
        self.advanced_settings_shel.clicked.connect(self.open_entitymanagement_shelter_dialog)

        self.menu = QMenu(self)
        self.show()

    def open_entitymanagement_dialog(self):
        from ui_entityManagement import Ui_EntityManagementCommunities

        dialog = QDialog(self)
        addEMC_dialog = Ui_EntityManagementCommunities()
        addEMC_dialog.setupUi(dialog)

        self.load_from_excel(addEMC_dialog.communityInfo_table)

        #buttons showing on the entyman-dialog
        addEMC_dialog.mc_back_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_cancel_changes_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_import_btn.clicked.connect(lambda: self.import_excel_data(addEMC_dialog.communityInfo_table, dialog))
        addEMC_dialog.mc_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMC_dialog.communityInfo_table))
        addEMC_dialog.mc_add_community_btn.clicked.connect(lambda: self.add_row(addEMC_dialog.communityInfo_table, dialog))

        result = dialog.exec()

        if result == QDialog.Accepted:
            pass

    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        dialog = QDialog(self)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)
        #buttons showing on the entymanshel-dialog
        addEMS_dialog.ms_back_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_cancel_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_import_btn.clicked.connect(lambda: self.import_excel_data(addEMS_dialog.shelterInfo_table, dialog))
        addEMS_dialog.ms_save_changes_btn.clicked.connect(lambda: self.save_to_excel(addEMS_dialog.shelterInfo_table))
        result = dialog.exec()

        if result == QDialog.Accepted:
            pass

    def import_excel_data(self, table_widget, dialog):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx);;All Files (*)", options=options)

        if file_path:
            data = pd.read_excel(file_path).fillna("") #replace NaN with empty string
            
            table_widget.setColumnCount(len(data.columns) + 2)
            table_widget.setHorizontalHeaderLabels(['Select'] + list(data.columns) + ['Delete'])

            # Clear any existing rows
            table_widget.setRowCount(0)

            table_widget.setStyleSheet("QTableWidgetItem { color: black; }")

            # Populate the table with data
            for row_idx, row_data in data.iterrows():
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)

                # Add checkbox in the first column
                check_box_widget = QWidget()
                check_box_widget.setCursor(QCursor(Qt.PointingHandCursor))
                layout_check = QHBoxLayout(check_box_widget)
                layout_check.setAlignment(Qt.AlignCenter)
                checkbox = QCheckBox()
                layout_check.addWidget(checkbox)
                checkbox.setStyleSheet("""
                    background-color: #C0C0C0;
                    color: black;
                                       """)
                layout_check.setContentsMargins(0, 0, 0, 0)
                table_widget.setCellWidget(row_position, 0, check_box_widget)

                # Populate data columns
                for col_idx, value in enumerate(row_data, start=1):
                    item = QTableWidgetItem(str(value))
                    item.setBackground(QColor(255, 255, 255))
                    item.setForeground(QColor(0, 0, 0))
                    table_widget.setItem(row_position, col_idx, item)

                delete_btn_widget = QWidget()
                delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
                layout_btn = QHBoxLayout(delete_btn_widget)
                layout_btn.setAlignment(Qt.AlignCenter)
                delete_btn = QPushButton()
                delete_btn.setIcon(QIcon("ICONS/9022869_duotone_trash.png"))
                delete_btn.clicked.connect(partial(self.delete_row, table_widget, row_position))
                layout_btn.addWidget(delete_btn)
                layout_btn.setContentsMargins(0, 0, 0, 0)
                table_widget.setCellWidget(row_position, table_widget.columnCount() - 1, delete_btn_widget)

            # Resize columns to fit their contents
            table_widget.resizeColumnsToContents()
    def save_to_excel(self, table_widget):
        data = []
        row_count = table_widget.rowCount()
        column_count = table_widget.columnCount()

        # Collect headers, ignoring the first and last columns for checkboxes and delete buttons
        headers = [table_widget.horizontalHeaderItem(col).text() for col in range(1, column_count - 1)]

        # Collect each row's data, ignoring the first and last columns
        for row in range(row_count):
            row_data = []
            for col in range(1, column_count - 1):
                item = table_widget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        dataframe = pd.DataFrame(data, columns=headers)  #DataFrame conversion

        try:
            # Save the DataFrame to Excel
            dataframe.to_excel(self.file_path, index=False)
            QMessageBox.information(self, "Success", f"File saved successfully as {self.file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def load_from_excel(self, table_widget):
        # Load data from persistent file if it exists
        if os.path.exists(self.file_path):
            try:
                dataframe = pd.read_excel(self.file_path).fillna("")

                # Clear the table and set up headers
                table_widget.setRowCount(0)
                table_widget.setColumnCount(len(dataframe.columns) + 2)
                table_widget.setHorizontalHeaderLabels(['Select'] + list(dataframe.columns) + ['Delete'])

                # Populate the table with the data
                for row_idx, row_data in dataframe.iterrows():
                    row_position = table_widget.rowCount()
                    table_widget.insertRow(row_position)

                    # Add checkbox in the first column
                    check_box_widget = QWidget()
                    check_box_widget.setCursor(QCursor(Qt.PointingHandCursor))
                    layout_check = QHBoxLayout(check_box_widget)
                    layout_check.setAlignment(Qt.AlignCenter)
                    checkbox = QCheckBox()
                    layout_check.addWidget(checkbox)
                    checkbox.setStyleSheet("""
                        background-color: #C0C0C0;
                        color: black;
                                        """)
                    layout_check.setContentsMargins(0, 0, 0, 0)
                    table_widget.setCellWidget(row_position, 0, check_box_widget)

                    # Populate each column except for Select and Delete buttons
                    for col_idx, value in enumerate(row_data, start=1):
                        item = QTableWidgetItem(str(value))
                        table_widget.setItem(row_position, col_idx, item)

                    delete_btn_widget = QWidget()
                    delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
                    layout_btn = QHBoxLayout(delete_btn_widget)
                    layout_btn.setAlignment(Qt.AlignCenter)
                    delete_btn = QPushButton()
                    delete_btn.setIcon(QIcon("ICONS/9022869_duotone_trash.png"))
                    delete_btn.clicked.connect(partial(self.delete_row, table_widget, row_position))
                    layout_btn.addWidget(delete_btn)
                    layout_btn.setContentsMargins(0, 0, 0, 0)
                    table_widget.setCellWidget(row_position, table_widget.columnCount() - 1, delete_btn_widget)

                    # Resize columns to fit their contents
                    table_widget.resizeColumnsToContents()

                    # Add additional elements (checkbox, delete button, etc.) for each row if needed
                QMessageBox.information(self, "Load", "Data loaded successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

    def setup_delete_button(self, button, table_widget):
        button.clicked.connect(lambda: self.delete_rows(table_widget))

    def delete_selected_rows(self, table_widget):
        rows_to_delete = []
        
        # Gather rows that have checked checkboxes
        for row in range(table_widget.rowCount()):
            check_box_widget = table_widget.cellWidget(row, 0)
            if check_box_widget is not None:
                checkbox = check_box_widget.findChild(QCheckBox)
                if checkbox.isChecked():  # Check the state of the checkbox
                    rows_to_delete.append(row)
        
        if rows_to_delete:
            # Confirmation dialog before deleting
            del_msg_box = QMessageBox()
            del_msg_box.setIcon(QMessageBox.Warning)
            del_msg_box.setText("Are you sure you want to delete the selected rows?")
            del_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            del_msg_box.setDefaultButton(QMessageBox.No)
            del_msg_box.setWindowTitle("Delete Confirmation")
            response = del_msg_box.exec()

            if response == QMessageBox.Yes:
                # Remove rows in reverse order to avoid index shifting issues
                for row in sorted(rows_to_delete, reverse=True):
                    table_widget.removeRow(row)
        else:
            QMessageBox.information(self, "Info", "No rows selected for deletion.")

    def delete_row(self, table_widget, row_position):
        del_msg_box = QMessageBox()
        del_msg_box.setIcon(QMessageBox.Warning)
        del_msg_box.setText("Are you sure you want to delete this row?")
        del_msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        del_msg_box.setDefaultButton(QMessageBox.No)
        del_msg_box.setWindowTitle("Delete Confirmation")
        response = del_msg_box.exec()

        if response == QMessageBox.Yes:
            table_widget.removeRow(row_position)
            
            # Reconnect delete buttons with updated row indices after deletion
            for row in range(table_widget.rowCount()):
                delete_btn_widget = table_widget.cellWidget(row, table_widget.columnCount() - 1)
                if delete_btn_widget is not None:
                    delete_btn = delete_btn_widget.findChild(QPushButton)
                    if delete_btn:
                        delete_btn.clicked.disconnect()
                        delete_btn.clicked.connect(partial(self.delete_row, table_widget, row))

    def add_row(self, table_widget, dialog):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)

        check_box_widget = QWidget()
        layout_check = QHBoxLayout(check_box_widget)
        layout_check.setAlignment(Qt.AlignCenter)
        checkbox = QCheckBox()
        layout_check.addWidget(checkbox)
        checkbox.setStyleSheet("""
                background-color: #C0C0C0;
                color: black;
                               """)
        layout_check.setContentsMargins(0, 0, 0, 0)
        table_widget.setCellWidget(row_position, 0, check_box_widget)

        # Add empty cells in each column (except the last column if it's for delete buttons)
        for col in range(1, table_widget.columnCount() - 1):
            item = QTableWidgetItem("")  # Empty item for user input
            table_widget.setItem(row_position, col, item)

        delete_btn_widget = QWidget()
        delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
        layout_btn = QHBoxLayout(delete_btn_widget)
        layout_btn.setAlignment(Qt.AlignCenter)
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon("ICONS/9022869_duotone_trash.png"))
        delete_btn.clicked.connect(partial(self.delete_row, table_widget, row_position))
        layout_btn.addWidget(delete_btn)
        layout_btn.setContentsMargins(0, 0, 0, 0)
        table_widget.setCellWidget(row_position, table_widget.columnCount() - 1, delete_btn_widget)