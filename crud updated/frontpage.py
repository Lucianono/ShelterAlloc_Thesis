from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

import mysql.connector

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

        self.student_1.clicked.connect(self.students_context_menu)
        self.teacher_1.clicked.connect(self.teachers_context_menu)
        self.finance_1.clicked.connect(self.finances_context_menu)

    # connect to mysql server
        self.create_connection()
    # create student table
        self.create_student_table()
    # open add student dialog
        self.addStudent_btn.clicked.connect(self.open_addstudent_dialog)
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
        #style for the menu
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

        if text == "Student Information":
            self.switch_to_studentInfo_page()
        elif text == "Student Payments":
            self.switch_to_studentPayments_page()
        elif text == "Student Transaction":
            self.switch_to_studentTransactions_page()
        elif text == "Teacher Information":
            self.switch_to_teacherInfo_page()
        elif text == "Teacher Salaries":
            self.switch_to_teacherSalaries_page()
        elif text == "Teacher Transaction":
            self.switch_to_teacherTransaction_page()
        elif text == "Budget":
            self.switch_to_budgetInfo_page()
        elif text == "Expenses":
            self.switch_to_expensesInfo_page()
        elif text == "Business Overview":
            self.switch_to_businessOverview_page()

    #creat a method for database connection

    def create_connection(self):
        host_name = "localhost"
        user_name = "root"
        password = ""
        db_name = "my_school"

        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
        )

        cursor = self.mydb.cursor()

        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')

        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = db_name
        )

        return self.mydb
    
    # create the student table

    def create_student_table(self):
        cursor = self.mydb.cursor()

        create_students_table_query = f"""
            CREATE TABLE IF NOT EXISTS student_table (
                name TEXT,
                student_id VARCHAR(15) PRIMARY KEY,
                gender TEXT,
                class TEXT,
                birthday TEXT,
                address TEXT,
                phone_number VARCHAR(15),
                email VARCHAR(15)
            )"""
        
        cursor.execute(create_students_table_query)
        # commit changes

        self.mydb.commit()
        self.mydb.close()

    # open dialog for inserting new student
    def open_addstudent_dialog(self):
        from studentDialog import Ui_StudentsDialog

        # show dialog
        addStudent_dialog = Ui_StudentsDialog(self)
        result = addStudent_dialog.exec() # blocked until dialog is closed

        if result == Ui_StudentsDialog.accepted:
            # self.insert_new_student()
            pass
    def load_students_info(self):
        # clear data in the table that exist
        self.studentInfo_table.setRowCount(0)

        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_date_from_table(selected_class, selected_gender)
    def get_date_from_table(self, class_filter, gender_filter):
        cursor = self.create_connection().cursor()

        # sql query
        query = f""" SELECT names, student_id, gender, class, birthday, address, phone_number, email FROM student_table WHERE ('{class_filter} = 'SELECT CLASS' OR class = {class_filter})
