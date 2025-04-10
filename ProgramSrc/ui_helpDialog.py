# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpDialog.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(800, 600))
        Dialog.setMaximumSize(QSize(800, 600))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"	background-color: #1C5739;\n"
"color: white;\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)
        self.pushButton_10.setMinimumSize(QSize(150, 0))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMinimumSize(QSize(150, 0))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setMinimumSize(QSize(150, 0))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)
        self.pushButton_7.setMinimumSize(QSize(150, 0))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setMinimumSize(QSize(150, 0))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #12c753;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"\n"
"	background-color: #1C5739;\n"
"color: white;\n"
"")

        self.verticalLayout_3.addWidget(self.label_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout_7.addWidget(self.textBrowser)


        self.verticalLayout_3.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"\n"
"	background-color: #1C5739;\n"
"color: white;\n"
"")

        self.verticalLayout_4.addWidget(self.label_3)

        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textBrowser_2 = QTextBrowser(self.widget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setOpenExternalLinks(True)

        self.verticalLayout_8.addWidget(self.textBrowser_2)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(0, 50))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: #1C5739;\n"
"\n"
"color: white;\n"
"\\n")

        self.verticalLayout_5.addWidget(self.label_4)

        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textBrowser_3 = QTextBrowser(self.widget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setOpenExternalLinks(True)

        self.verticalLayout_9.addWidget(self.textBrowser_3)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_6 = QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 50))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: #1C5739;\n"
"\n"
"color: white;\n"
"\\n")

        self.verticalLayout_6.addWidget(self.label_5)

        self.widget_4 = QWidget(self.page_4)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_10 = QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser_4 = QTextBrowser(self.widget_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setOpenExternalLinks(True)

        self.verticalLayout_10.addWidget(self.textBrowser_4)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_11 = QVBoxLayout(self.page_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: #1C5739;\n"
"\n"
"color: white;\n"
"\\n")

        self.verticalLayout_11.addWidget(self.label_6)

        self.widget_5 = QWidget(self.page_5)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.textBrowser_5 = QTextBrowser(self.widget_5)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setOpenExternalLinks(True)

        self.verticalLayout_12.addWidget(self.textBrowser_5)


        self.verticalLayout_11.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_13 = QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.page_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: #1C5739;\n"
"\n"
"color: white;\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.label_7)

        self.widget_6 = QWidget(self.page_6)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textBrowser_6 = QTextBrowser(self.widget_6)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setOpenExternalLinks(True)

        self.verticalLayout_14.addWidget(self.textBrowser_6)


        self.verticalLayout_13.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.page_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: #1C5739;\n"
"\n"
"color: white;\n"
"\n"
"")

        self.verticalLayout_17.addWidget(self.label_8)

        self.widget_7 = QWidget(self.page_7)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.textBrowser_8 = QTextBrowser(self.widget_7)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setOpenExternalLinks(True)

        self.verticalLayout_15.addWidget(self.textBrowser_8)


        self.verticalLayout_17.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Help", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Quick Start", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Dashboard", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Community Settings", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Shelter Settings", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Model Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Solve Settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"About Us", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"  Dashboard", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"  Community Settings", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"  Shelter Settings", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"  Model Settings", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"  Solve Settings", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"  About Us", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"ProgramSrc/tutorial/dashboard.png\" width=\"300\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Open Sans,Arial,sans-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u" Quick Start", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Open Sans,Arial,san"
                        "s-serif'; font-size:8pt; color:#000000; background-color:#ffffff;\">&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&quot;</span></p></body></html>", None))
    # retranslateUi

