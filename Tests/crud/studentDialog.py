# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_StudentsDialog(object):
     def __init__(self, parent=None):
        super.__init__(parent)
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid black;\n"
"	border-raidus: 10px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border: 1px solid black;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 31px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px  1px 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	height: 31px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 301, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 80, 511, 411))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.name_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid black;\n"
"	border-radius: 10px\n"
"}")

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.grade_comboBox = QComboBox(self.widget)
        self.grade_comboBox.addItem("")
        self.grade_comboBox.addItem("")
        self.grade_comboBox.setObjectName(u"grade_comboBox")

        self.verticalLayout_6.addWidget(self.grade_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.widget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.address_lineEdit = QLineEdit(self.widget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.address_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid black;\n"
"	border-radius: 10px\n"
"}")

        self.verticalLayout_2.addWidget(self.address_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.number_lineEdit = QLineEdit(self.widget)
        self.number_lineEdit.setObjectName(u"number_lineEdit")
        self.number_lineEdit.setMinimumSize(QSize(0, 35))
        self.number_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.number_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid black;\n"
"	border-radius: 10px\n"
"}")

        self.verticalLayout_3.addWidget(self.number_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(self.widget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.email_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid black;\n"
"	border-radius: 10px\n"
"}")

        self.verticalLayout_4.addWidget(self.email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(320, 520, 211, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.widget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setMaximumSize(QSize(16777215, 16777215))
        self.saveStudent_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(75, 255, 87);\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.widget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 41))
        self.cancel_btn.setMaximumSize(QSize(16777215, 16777215))
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(156, 156, 156);\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

def retranslateUi(self, StudentDialog):
        StudentDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Select Grade", None))
        self.grade_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade 1", None))
        self.grade_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade 2", None))

        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Date of Birth", None))
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi

