from PySide6.QtWidgets import QMainWindow, QMenu, QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEngineSettings
from ui_index import Ui_MainWindow
from folium.plugins import MousePosition
import sys
import os
import folium
import io


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

        map_path = self.create_map()
        self.webEngineView.setUrl(QUrl.fromLocalFile(map_path))

        self.icon_text_widget.setHidden(True)

        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)

        # Connect buttons to their respective page-switching methods
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payment.clicked.connect(self.switch_to_studentPayments_page)
        self.student_transaction.clicked.connect(self.switch_to_studentTransactions_page)

        self.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teacher_salaries.clicked.connect(self.switch_to_teacherSalaries_page)
        self.teacher_transaction.clicked.connect(self.switch_to_teacherTransaction_page)

        self.budgets.clicked.connect(self.switch_to_budgetInfo_page)
        self.expenses.clicked.connect(self.switch_to_expensesInfo_page)
        self.businessOverview.clicked.connect(self.switch_to_businessOverview_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page) 

        self.student_1.clicked.connect(self.students_context_menu)
        self.teacher_1.clicked.connect(self.teachers_context_menu)
        self.finance_1.clicked.connect(self.finances_context_menu)

        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        
        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)  
        
    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_studentPayments_page(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_studentTransactions_page(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)
        
    def switch_to_teacherSalaries_page(self):
        self.stackedWidget.setCurrentIndex(6)
        
    def switch_to_teacherTransaction_page(self):
        self.stackedWidget.setCurrentIndex(7)
        
    def switch_to_budgetInfo_page(self):
        self.stackedWidget.setCurrentIndex(8)
        
    def switch_to_expensesInfo_page(self):
        self.stackedWidget.setCurrentIndex(9)
        
    def switch_to_businessOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)
        
    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    def students_context_menu(self):
        self.show_custom_context_menu(self.student_1, ["Student Information", "Student Payments", "Student Transaction"])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teacher_1, ["Teacher Information", "Teacher Salaries", "Teacher Transaction"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finance_1, ["Budgets", "Expenses", "Business Overview"])

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        menu.setStyleSheet("""
                           QMenu{
                           background-color: black;
                           color: white;
                           }
                           QMenu:selected {
                           background-color: white;
                           color: #12B298
                           }
                           """)

        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        # Use a dictionary to map menu items to their respective methods
        action_map = {
            "Student Information": self.switch_to_studentInfo_page,
            "Student Payments": self.switch_to_studentPayments_page,
            "Student Transaction": self.switch_to_studentTransactions_page,
            "Teacher Information": self.switch_to_teacherInfo_page,
            "Teacher Salaries": self.switch_to_teacherSalaries_page,
            "Teacher Transaction": self.switch_to_teacherTransaction_page,
            "Budgets": self.switch_to_budgetInfo_page,
            "Expenses": self.switch_to_expensesInfo_page,
            "Business Overview": self.switch_to_businessOverview_page,
        }

        # Call the appropriate method if the menu item exists in the action_map
        if text in action_map:
            action_map[text]()

    def create_map(self):
        # Define the path for the map file
        map_path = os.path.join(os.getcwd(), "map.html")

        # Check if the map file already exists
        if os.path.exists(map_path):
            print(f"Map already exists at: {map_path}")
        else:
            # If the file does not exist, create a new map
            m = folium.Map(location=[14.7919, 120.7350], zoom_start=13).add_child(
                folium.ClickForMarker("Julius Ian DIno"))
            m.save(map_path)
            print(f"New map created and saved at: {map_path}")

        return map_path