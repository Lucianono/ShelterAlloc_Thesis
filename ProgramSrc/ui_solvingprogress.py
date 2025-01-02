# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solvingprogress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_solvingProgress(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(600, 400))
        Dialog.setMaximumSize(QSize(600, 400))
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"#frame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 87, 57, 255), stop:1 rgba(61, 189, 124, 255)\n"
"    );\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(19)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, -1, 40, -1)
        self.solvingModel_progressBar = QProgressBar(Dialog)
        self.solvingModel_progressBar.setObjectName(u"solvingModel_progressBar")
        font1 = QFont()
        font1.setPointSize(1)
        self.solvingModel_progressBar.setFont(font1)
        self.solvingModel_progressBar.setStyleSheet(u"#progressBar {\n"
"border: none;\n"
"background-color: lightgray;\n"
"height: 8px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"#progressBar::chunk {\n"
"background-color: #1C5739;\n"
"border-radius: 3px;\n"
"}")
        self.solvingModel_progressBar.setValue(24)
        self.solvingModel_progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.solvingModel_progressBar)

        self.solvingModel_textFrame = QFrame(Dialog)
        self.solvingModel_textFrame.setObjectName(u"solvingModel_textFrame")
        self.solvingModel_textFrame.setStyleSheet(u"#textFrame {\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"border: 1px solid lightgray;\n"
"}")
        self.solvingModel_textFrame.setFrameShape(QFrame.StyledPanel)
        self.solvingModel_textFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.solvingModel_textFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.solvingModel_textFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"background-color: white;\n"
"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 196))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.solvingModel_textFrame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.solving_prog_cancel_btn = QPushButton(Dialog)
        self.solving_prog_cancel_btn.setObjectName(u"solving_prog_cancel_btn")
        self.solving_prog_cancel_btn.setMinimumSize(QSize(150, 0))
        self.solving_prog_cancel_btn.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        self.solving_prog_cancel_btn.setFont(font2)
        self.solving_prog_cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solving_prog_cancel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"	font-size:16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF5A4D;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E63946;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.solving_prog_cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Solving Model</span></p></body></html>", None))
        self.solving_prog_cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

