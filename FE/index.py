from PySide6.QtWidgets import QMainWindow, QMenu, QDialog
from PySide6.QtGui import QAction
from ui_dashboard import Ui_MainWindow

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
        
        result = dialog.exec()

        if result == QDialog.Accepted:
            pass
    
    def open_entitymanagement_shelter_dialog(self):
        from ui_entityManagementShelter import Ui_entityManagementShelter

        # Create a QDialog and set up the UI
        dialog = QDialog(self)
        addEMS_dialog = Ui_entityManagementShelter()
        addEMS_dialog.setupUi(dialog)
        
        result = dialog.exec()

        if result == QDialog.Accepted:
            pass
