# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(-2, 17, 1231, 831))
        self.splitter.setOrientation(Qt.Horizontal)
        self.icon_only_widget = QWidget(self.splitter)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMaximumSize(QSize(71, 831))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"\n"
"	background-color: black;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.icon_only_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 55, -1, 0)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icons/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon1 = QIcon()
        icon1.addFile(u":/icons/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)

        self.verticalLayout_9.addWidget(self.institution_1)

        self.student_1 = QPushButton(self.icon_only_widget)
        self.student_1.setObjectName(u"student_1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.student_1.setIcon(icon2)
        self.student_1.setIconSize(QSize(100, 20))
        self.student_1.setCheckable(True)

        self.verticalLayout_9.addWidget(self.student_1)

        self.teacher_1 = QPushButton(self.icon_only_widget)
        self.teacher_1.setObjectName(u"teacher_1")
        icon3 = QIcon()
        icon3.addFile(u":/icons/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teacher_1.setIcon(icon3)
        self.teacher_1.setIconSize(QSize(100, 20))
        self.teacher_1.setCheckable(True)

        self.verticalLayout_9.addWidget(self.teacher_1)

        self.finance_1 = QPushButton(self.icon_only_widget)
        self.finance_1.setObjectName(u"finance_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_1.setIcon(icon4)
        self.finance_1.setIconSize(QSize(100, 20))
        self.finance_1.setCheckable(True)

        self.verticalLayout_9.addWidget(self.finance_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 401, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)

        self.verticalLayout_10.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon6 = QIcon()
        icon6.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon6)
        self.signout_1.setIconSize(QSize(100, 16))
        self.signout_1.setCheckable(True)

        self.verticalLayout_10.addWidget(self.signout_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.splitter.addWidget(self.icon_only_widget)
        self.icon_text_widget = QWidget(self.splitter)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButtons {\n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.icon_text_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color: white;\n"
"	border-radius: 2px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -65px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(95, 45))
        self.institution_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.student_2 = QPushButton(self.students)
        self.student_2.setObjectName(u"student_2")
        self.student_2.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.student_2.setIcon(icon9)
        self.student_2.setIconSize(QSize(200, 60))
        self.student_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.student_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.student_info.setCheckable(True)

        self.verticalLayout.addWidget(self.student_info)

        self.student_payment = QPushButton(self.students_dropdown)
        self.student_payment.setObjectName(u"student_payment")
        self.student_payment.setStyleSheet(u"QPushButton {\n"
"	padding-left: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.student_payment.setCheckable(True)

        self.verticalLayout.addWidget(self.student_payment)

        self.student_transaction = QPushButton(self.students_dropdown)
        self.student_transaction.setObjectName(u"student_transaction")
        self.student_transaction.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.student_transaction.setCheckable(True)

        self.verticalLayout.addWidget(self.student_transaction)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teacher_2 = QPushButton(self.teachers)
        self.teacher_2.setObjectName(u"teacher_2")
        self.teacher_2.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teacher_2.setIcon(icon10)
        self.teacher_2.setIconSize(QSize(200, 60))
        self.teacher_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.teacher_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teachers_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teacher_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teacher_salaries = QPushButton(self.teachers_dropdown)
        self.teacher_salaries.setObjectName(u"teacher_salaries")
        self.teacher_salaries.setStyleSheet(u"QPushButton {\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teacher_salaries.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_salaries)

        self.teacher_transaction = QPushButton(self.teachers_dropdown)
        self.teacher_transaction.setObjectName(u"teacher_transaction")
        self.teacher_transaction.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teacher_transaction.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_transaction)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setFrameShape(QFrame.StyledPanel)
        self.finances.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.fianance_2 = QPushButton(self.finances)
        self.fianance_2.setObjectName(u"fianance_2")
        self.fianance_2.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fianance_2.setIcon(icon11)
        self.fianance_2.setIconSize(QSize(200, 60))
        self.fianance_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.fianance_2)

        self.finances_dropdown = QFrame(self.finances)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finances_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton {\n"
"	padding-left: -40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finances_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton {\n"
"	padding-left: -35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.businessOverview = QPushButton(self.finances_dropdown)
        self.businessOverview.setObjectName(u"businessOverview")
        self.businessOverview.setStyleSheet(u"QPushButton {\n"
"	padding-left: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.businessOverview.setCheckable(True)

        self.verticalLayout_3.addWidget(self.businessOverview)


        self.verticalLayout_6.addWidget(self.finances_dropdown)


        self.verticalLayout_7.addWidget(self.finances)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 60))
        self.signout_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.signout_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.splitter.addWidget(self.icon_text_widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.header_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(68, 68, 68);")

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(340, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 20px;\n"
"	border: 1px solid grey;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/profile.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 881, 741))
        self.stackedWidget.setMinimumSize(QSize(841, 741))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 270, 261, 111))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.webEngineView = QWebEngineView(self.page)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(59, 29, 661, 651))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 300, 181, 81))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 431, 91))
        self.label_9.setFont(font2)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 80, 491, 31))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(True)
        self.label_19.setFont(font3)
        self.studentInfo_table = QTableWidget(self.page_3)
        if (self.studentInfo_table.columnCount() < 9):
            self.studentInfo_table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(10, 250, 861, 441))
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: rgb(187, 194, 200);\n"
"}")
        self.layoutWidget1 = QWidget(self.page_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 120, 451, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.addStudent_btn = QPushButton(self.layoutWidget1)
        self.addStudent_btn.setObjectName(u"addStudent_btn")
        self.addStudent_btn.setMinimumSize(QSize(0, 41))
        self.addStudent_btn.setMaximumSize(QSize(16777215, 16777215))
        self.addStudent_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 255, 87);\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.addStudent_btn)

        self.excelExport_btn = QPushButton(self.layoutWidget1)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMinimumSize(QSize(0, 41))
        self.excelExport_btn.setMaximumSize(QSize(16777215, 16777215))
        self.excelExport_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(56, 188, 0);\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.layoutWidget1)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(0, 41))
        self.pdfExport_btn.setMaximumSize(QSize(16777215, 16777215))
        self.pdfExport_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(221, 0, 0);\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pdfExport_btn)

        self.layoutWidget2 = QWidget(self.page_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 190, 551, 43))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.layoutWidget2)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px  1px 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.select_gender)

        self.select_grade = QComboBox(self.layoutWidget2)
        self.select_grade.addItem("")
        self.select_grade.addItem("")
        self.select_grade.addItem("")
        self.select_grade.setObjectName(u"select_grade")
        self.select_grade.setMinimumSize(QSize(150, 0))
        self.select_grade.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px  1px 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.select_grade)

        self.search_student = QLineEdit(self.layoutWidget2)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMaximumSize(QSize(16777215, 31))
        self.search_student.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 20px;\n"
"	border: 1px solid grey;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 280, 311, 121))
        self.label_10.setFont(font2)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 300, 341, 101))
        self.label_11.setFont(font2)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 290, 341, 101))
        self.label_12.setFont(font2)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 310, 281, 91))
        self.label_13.setFont(font2)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(220, 300, 341, 91))
        self.label_14.setFont(font2)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 320, 141, 81))
        self.label_15.setFont(font2)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(320, 320, 161, 81))
        self.label_16.setFont(font2)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(300, 310, 321, 101))
        self.label_17.setFont(font2)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(320, 320, 141, 61))
        self.label_18.setFont(font2)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.main_screen_widget)

        self.splitter.addWidget(self.layoutWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.student_2.toggled.connect(self.students_dropdown.setHidden)
        self.teacher_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.fianance_2.toggled.connect(self.finances_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.student_2.toggled.connect(self.student_1.setChecked)
        self.teacher_2.toggled.connect(self.teacher_1.setChecked)
        self.fianance_2.toggled.connect(self.finance_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.student_1.setText("")
        self.teacher_1.setText("")
        self.finance_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.student_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_payment.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_transaction.setText(QCoreApplication.translate("MainWindow", u"Student Transaction", None))
        self.teacher_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salaries.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_transaction.setText(QCoreApplication.translate("MainWindow", u"Teacher Transaction", None))
        self.fianance_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.businessOverview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hello, Sam", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to School page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Welcome to Student Information Page", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.addStudent_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_grade.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_grade.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_grade.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 2", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Transaction", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Transaction", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

