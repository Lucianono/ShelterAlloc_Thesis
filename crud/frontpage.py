from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

        self.icon_text_widget.setHidden(True)

        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)

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