from PySide6.QtWidgets import QMainWindow, QMenu, QDialog, QTableWidgetItem, QFileDialog
from PySide6.QtGui import QAction, QColor
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

    def import_excel_data(self, table_widget, dialog):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx);;All Files (*)", options=options)
        
        if file_path:
            data = pd.read_excel(file_path)
            
            table_widget.setRowCount(0)
            table_widget.setColumnCount(0)

            # Set the number of columns
            table_widget.setColumnCount(len(data.columns))
            table_widget.setHorizontalHeaderLabels(data.columns)

            # Populate the table with data
            for row_idx, row_data in data.iterrows():
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setBackground(QColor(255, 255, 255))
                    item.setForeground(QColor(0, 0, 0))
                    table_widget.setItem(row_position, col_idx, item)

            # Refresh the table and adjust column sizes
            table_widget.viewport().update()  # Refresh the view
            table_widget.resizeColumnsToContents()  # Resize columns to fit their contents


    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        dialog = QDialog(self)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)
        
        addEMS_dialog.ms_back_btn.clicked.connect(dialog.close)
        addEMS_dialog.ms_cancel_btn.clicked.connect(dialog.close)
        result = dialog.exec()

        if result == QDialog.Accepted:
            pass