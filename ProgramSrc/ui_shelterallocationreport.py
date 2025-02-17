# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelterallocationreport.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_ShelterAllocationReport(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(1000, 600))
        Dialog.setMaximumSize(QSize(1002, 600))
        Dialog.setStyleSheet(u"#Dialog {\n"
"background-color: white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(Dialog)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMinimumSize(QSize(1000, 75))
        self.headerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.headerFrame.setAutoFillBackground(False)
        self.headerFrame.setStyleSheet(u"#headerFrame {\n"
"   background-color: #dfe0e5;   border: none;\n"
"  padding: 10px;    border-bottom: 2px solid gray;    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);}\n"
"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 50, -1)
        self.pushButton = QPushButton(self.headerFrame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.headerFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.headerFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"   background-color: #1C5739;        \n"
"    color: white;                        \n"
"    border: none;                        \n"
"    border-radius: 10px;                 \n"
"    padding: 10px 20px;                   \n"
"    font-size: 16px;                     \n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.headerFrame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 20)
        self.webEngineView = QWebEngineView(Dialog)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QSize(450, 450))
        self.gridLayout = QGridLayout(self.webEngineView)
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_3.addWidget(self.webEngineView)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border: none;\n"
"background: none;\n"
"text-decoration: underline;\n"
"color:rgb(0, 0, 255);\n"
"text-align: left;")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0, 50));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(0, 0, 0, 50));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setBackground(QColor(0, 0, 0, 50));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: #F0F0F0;\n"
"    color: black;            \n"
"    padding: 5px;              \n"
"    border: 1px solid #C0C0C0;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    gridline-color: #C0C0C0;\n"
"    border: 1px solid #C0C0C0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"}\n"
"\n"
"QTableWidget::item::selected {\n"
"	color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E8F4F8;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #CCE7F0;\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(112)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Shelter Location-Allocation Report", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"SAVE REPORT", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Bilevel No Transfer (BNT) Model", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Generated report by Bryyyyy", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"More Details", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Selected Shelters", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Level", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Allocated Communities", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Shelter A", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Barangay A Barangay B", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Shelter B", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Barangay C Barangay D", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

