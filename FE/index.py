from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import QAction, QColor, QIcon, QCursor
from PySide6.QtCore import Qt
from ui_dashboard import Ui_MainWindow
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dashboard")

        self.advanced_settings_com.clicked.connect(self.open_entitymanagement_dialog)
        self.advanced_settings_shel.clicked.connect(self.open_entitymanagement_shelter_dialog)

        self.show()

        self.menu = QMenu(self)

    def open_entitymanagement_dialog(self):
        from ui_entityManagement import Ui_EntityManagementCommunities

        # Create a QDialog and set up the UI
        dialog = QDialog(self)
        addEMC_dialog = Ui_EntityManagementCommunities()
        addEMC_dialog.setupUi(dialog)

        addEMC_dialog.mc_back_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_cancel_changes_btn.clicked.connect(dialog.close)
        addEMC_dialog.mc_import_btn.clicked.connect(lambda: self.import_excel_data(addEMC_dialog.communityInfo_table, dialog))

        result = dialog.exec()

        if result == QDialog.Accepted:
            pass

    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        dialog = QDialog(self)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)
        
        addEMS_dialog.ms_back_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_cancel_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_import_btn.clicked.connect(lambda: self.import_excel_data(addEMS_dialog.shelterInfo_table, dialog))
        result = dialog.exec()

        if result == QDialog.Accepted:
            pass

    def import_excel_data(self, table_widget, dialog):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx);;All Files (*)", options=options)

        if file_path:
            data = pd.read_excel(file_path)
            
            table_widget.setColumnCount(len(data.columns) + 2)
            table_widget.setHorizontalHeaderLabels(['Select'] + list(data.columns) + ['Delete'])

            # Clear any existing rows
            table_widget.setRowCount(0)

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

                # Add delete button in the last column
                delete_btn_widget = QWidget()
                delete_btn_widget.setCursor(QCursor(Qt.PointingHandCursor))
                layout_btn = QHBoxLayout(delete_btn_widget)
                layout_btn.setAlignment(Qt.AlignCenter)
                delete_btn = QPushButton()
                delete_btn.setIcon(QIcon("ICONS/9022869_duotone_trash.png"))
                delete_btn.clicked.connect(lambda _, r=row_position: self.delete_row(table_widget, r))
                layout_btn.addWidget(delete_btn)
                layout_btn.setContentsMargins(0, 0, 0, 0)
                table_widget.setCellWidget(row_position, table_widget.columnCount() - 1, delete_btn_widget)

            # Resize columns to fit their contents
            table_widget.resizeColumnsToContents()
    
    def delete_row(self, table_widget, row_position):
        table_widget.removeRow(row_position)