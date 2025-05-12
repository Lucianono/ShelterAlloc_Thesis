# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_17 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.SideBar = QWidget(self.centralwidget)
        self.SideBar.setObjectName(u"SideBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy1)
        self.SideBar.setMinimumSize(QSize(350, 0))
        self.SideBar.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.SideBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.SideBar)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #1C5739;\n"
"	color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.frame)

        self.scrollArea_2 = QScrollArea(self.SideBar)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"#scollArea_2{\n"
"	background-color: #f0f0f0;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 348, 612))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget = QWidget(self.scrollAreaWidgetContents_9)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-radius: 15;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.communities_dropdown_2 = QPushButton(self.frame_2)
        self.communities_dropdown_2.setObjectName(u"communities_dropdown_2")
        self.communities_dropdown_2.setEnabled(True)
        self.communities_dropdown_2.setMinimumSize(QSize(0, 30))
        self.communities_dropdown_2.setMaximumSize(QSize(16777215, 31))
        self.communities_dropdown_2.setFont(font)
        self.communities_dropdown_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.communities_dropdown_2.setStyleSheet(u"* {\n"
"	background-color: none;\n"
"	border: none;\n"
"	padding:0;\n"
"	margin-left:-20;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/352021_arrow_drop down_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/ICONS/352023_arrow_drop_up_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.communities_dropdown_2.setIcon(icon)
        self.communities_dropdown_2.setIconSize(QSize(50, 50))
        self.communities_dropdown_2.setCheckable(True)
        self.communities_dropdown_2.setChecked(False)

        self.verticalLayout.addWidget(self.communities_dropdown_2)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setStyleSheet(u"QLabel{\n"
"	font-size:13px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.communities_dropdown = QVBoxLayout()
        self.communities_dropdown.setObjectName(u"communities_dropdown")
        self.add_community_btn = QPushButton(self.frame_5)
        self.add_community_btn.setObjectName(u"add_community_btn")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.add_community_btn.setFont(font1)
        self.add_community_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_community_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #14AE5C;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #12c753;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #10a84c;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ICONS/460625174_1063840541791504_8083137884705313080_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_community_btn.setIcon(icon1)
        self.add_community_btn.setIconSize(QSize(35, 35))
        self.add_community_btn.setFlat(False)

        self.communities_dropdown.addWidget(self.add_community_btn)

        self.advanced_settings_com = QPushButton(self.frame_5)
        self.advanced_settings_com.setObjectName(u"advanced_settings_com")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(True)
        font2.setUnderline(True)
        self.advanced_settings_com.setFont(font2)
        self.advanced_settings_com.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.advanced_settings_com.setStyleSheet(u" * {\n"
"background-color: none;\n"
"color: none;\n"
"border: none;\n"
"color: #00B5FF;\n"
"}")

        self.communities_dropdown.addWidget(self.advanced_settings_com)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.communities_dropdown.addLayout(self.verticalLayout_18)


        self.horizontalLayout_18.addLayout(self.communities_dropdown)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-radius: 15;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.shelter_dropdown = QPushButton(self.frame_3)
        self.shelter_dropdown.setObjectName(u"shelter_dropdown")
        self.shelter_dropdown.setMaximumSize(QSize(16777215, 30))
        self.shelter_dropdown.setFont(font)
        self.shelter_dropdown.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelter_dropdown.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"	margin-left:-20;\n"
"}")
        self.shelter_dropdown.setIcon(icon)
        self.shelter_dropdown.setIconSize(QSize(50, 50))
        self.shelter_dropdown.setCheckable(True)
        self.shelter_dropdown.setChecked(False)

        self.verticalLayout_6.addWidget(self.shelter_dropdown)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QLabel{\n"
"	font-size:13px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add_shelter_btn = QPushButton(self.frame_6)
        self.add_shelter_btn.setObjectName(u"add_shelter_btn")
        self.add_shelter_btn.setFont(font1)
        self.add_shelter_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_shelter_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #1A83E5;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #295987;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0e4c87;\n"
"}\n"
"")
        self.add_shelter_btn.setIcon(icon1)
        self.add_shelter_btn.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.add_shelter_btn)

        self.advanced_settings_shel = QPushButton(self.frame_6)
        self.advanced_settings_shel.setObjectName(u"advanced_settings_shel")
        self.advanced_settings_shel.setFont(font2)
        self.advanced_settings_shel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.advanced_settings_shel.setStyleSheet(u" * {\n"
"background-color: none;\n"
"color: none;\n"
"border: none;\n"
"color: #00B5FF;\n"
"}")

        self.verticalLayout_4.addWidget(self.advanced_settings_shel)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_4.addLayout(self.verticalLayout_19)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.widget, 0, Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.horizontalLayout_17.addWidget(self.SideBar)

        self.Main = QFrame(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Main)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.Main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.widget_2.setStyleSheet(u"background-color: white;")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"* {\n"
"	background-color: #1C5739;\n"
"	color: white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.reports_btn = QPushButton(self.frame_4)
        self.reports_btn.setObjectName(u"reports_btn")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.reports_btn.setFont(font3)
        self.reports_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reports_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.reports_btn)

        self.help_btn = QPushButton(self.frame_4)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setFont(font3)
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.help_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.help_btn)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_19.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_25 = QSpacerItem(100, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_25)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setToolTipDuration(-1)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.marker_comboBox = QComboBox(self.widget_2)
        self.marker_comboBox.addItem("")
        self.marker_comboBox.addItem("")
        self.marker_comboBox.setObjectName(u"marker_comboBox")
        self.marker_comboBox.setMinimumSize(QSize(150, 0))
        self.marker_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.marker_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	selection-background-color: #2980B9;\n"
"	height: 20px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.marker_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.shelterprev_comboBox = QComboBox(self.widget_2)
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.addItem("")
        self.shelterprev_comboBox.setObjectName(u"shelterprev_comboBox")
        self.shelterprev_comboBox.setMinimumSize(QSize(150, 0))
        self.shelterprev_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelterprev_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	selection-background-color: #2980B9;\n"
"	height: 20px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.shelterprev_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.solve_btn = QPushButton(self.widget_2)
        self.solve_btn.setObjectName(u"solve_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.solve_btn.sizePolicy().hasHeightForWidth())
        self.solve_btn.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setKerning(True)
        self.solve_btn.setFont(font4)
        self.solve_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solve_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 87, 57, 255), stop:1 rgba(61, 189, 124, 255));\n"
"	color: white;\n"
"    padding: 1px 16px;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(61, 189, 124, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.solve_btn)

        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, -1)
        self.stackedWidget = QStackedWidget(self.Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPlainTextEdit{\n"
"border: 1px solid rgb(209, 209, 209);\n"
"background-color: white;\n"
"border-radius: 7;\n"
"padding:2;\n"
"max-height:25;\n"
"min-height:10;\n"
"max-width:200;\n"
"}\n"
"QComboBox{\n"
"border: 1px solid rgb(209, 209, 209);\n"
"background-color: white;\n"
"border-radius: 7;\n"
"padding:2;\n"
"max-height:25;\n"
"min-height:10;\n"
"max-width:200;\n"
"}\n"
"QLabel {\n"
"    font-size: 12px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: underline;\n"
"}\n"
"QStackedWidget{\n"
"	border: 1px solid rgb(209, 209, 209);\n"
"	background: transparent;\n"
"\n"
"}\n"
"QScrollArea{\n"
"	border:none;\n"
"	background:transparent;\n"
"	background-color: #ff8dd2;\n"
"}\n"
"#scrollAreaWidgetContents{\n"
"	background-color: #f0f0f0;\n"
"}\n"
"#page{\n"
"	background-color: #f0f0f0;\n"
"}")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy3)
        self.page.setMinimumSize(QSize(0, 700))
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_14 = QPushButton(self.widget_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(30, 41))
        self.pushButton_14.setMaximumSize(QSize(25, 41))
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(41, 41))

        self.horizontalLayout_28.addWidget(self.pushButton_14)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(220, 0))
        self.label_18.setMaximumSize(QSize(220, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Ms Shell Dlg 2"])
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: none;\n"
"}")

        self.horizontalLayout_28.addWidget(self.label_18)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_15)

        self.checkBox_15 = QCheckBox(self.widget_4)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy4)
        self.checkBox_15.setMinimumSize(QSize(0, 0))
        self.checkBox_15.setMaximumSize(QSize(40, 40))
        self.checkBox_15.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_15.setIconSize(QSize(41, 41))
        self.checkBox_15.setChecked(False)

        self.horizontalLayout_28.addWidget(self.checkBox_15)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout.addWidget(self.plainTextEdit_3, 3, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 1, 1, 1)

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_28, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.plainTextEdit_5 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")

        self.gridLayout.addWidget(self.plainTextEdit_5, 5, 2, 1, 1)

        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_29, 5, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 1, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout.addWidget(self.plainTextEdit_4, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        font6 = QFont()
        font6.setFamilies([u"Ms Shell Dlg 2"])
        font6.setBold(True)
        font6.setUnderline(True)
        self.label_19.setFont(font6)
        self.label_19.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 2, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.widget_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy4.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy4)
        self.plainTextEdit.setMaximumSize(QSize(206, 31))

        self.gridLayout.addWidget(self.plainTextEdit, 1, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 6, 1, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_30, 6, 0, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")

        self.gridLayout.addWidget(self.plainTextEdit_6, 6, 2, 1, 1)

        self.label_23 = QLabel(self.widget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font6)
        self.label_23.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_26, 0, 1, 1, 1)

        self.plainTextEdit_15 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_15.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_15.setSizePolicy(sizePolicy4)
        self.plainTextEdit_15.setMaximumSize(QSize(206, 31))

        self.gridLayout.addWidget(self.plainTextEdit_15, 0, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 25, -1, -1)
        self.mc_cancel_changes_btn = QPushButton(self.widget_4)
        self.mc_cancel_changes_btn.setObjectName(u"mc_cancel_changes_btn")
        self.mc_cancel_changes_btn.setMinimumSize(QSize(0, 25))
        self.mc_cancel_changes_btn.setMaximumSize(QSize(161, 25))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.mc_cancel_changes_btn.setFont(font7)
        self.mc_cancel_changes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_cancel_changes_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff;\n"
"    color: #FF3B30;\n"
"    padding: 2px;\n"
"    border: 2px solid #FF3B30 ;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E63946;\n"
"}\n"
"")
        self.mc_cancel_changes_btn.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.mc_cancel_changes_btn)

        self.mc_save_changes_btn = QPushButton(self.widget_4)
        self.mc_save_changes_btn.setObjectName(u"mc_save_changes_btn")
        self.mc_save_changes_btn.setMinimumSize(QSize(0, 25))
        self.mc_save_changes_btn.setMaximumSize(QSize(161, 25))
        self.mc_save_changes_btn.setFont(font7)
        self.mc_save_changes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_save_changes_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #1C5739;\n"
"    color: white;\n"
"    padding: 2px;\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #25754c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1C5739;\n"
"}\n"
"")
        self.mc_save_changes_btn.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.mc_save_changes_btn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)


        self.verticalLayout_13.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy4.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy4)
        self.page_2.setMinimumSize(QSize(0, 800))
        self.page_2.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setMinimumSize(QSize(0, 750))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 328, 733))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setSpacing(9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_15 = QPushButton(self.widget_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 41))
        self.pushButton_15.setMaximumSize(QSize(25, 41))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QSize(41, 41))

        self.horizontalLayout_29.addWidget(self.pushButton_15)

        self.label_31 = QLabel(self.widget_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(220, 0))
        self.label_31.setMaximumSize(QSize(220, 16777215))
        self.label_31.setFont(font5)
        self.label_31.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: none;\n"
"}")

        self.horizontalLayout_29.addWidget(self.label_31)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_24)

        self.checkBox_16 = QCheckBox(self.widget_5)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy4.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy4)
        self.checkBox_16.setMinimumSize(QSize(0, 0))
        self.checkBox_16.setMaximumSize(QSize(40, 40))
        self.checkBox_16.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_16.setIconSize(QSize(41, 41))
        self.checkBox_16.setChecked(False)

        self.horizontalLayout_29.addWidget(self.checkBox_16)


        self.verticalLayout_15.addLayout(self.horizontalLayout_29)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(12)
        self.plainTextEdit_8 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")

        self.gridLayout_2.addWidget(self.plainTextEdit_8, 4, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 3, 1, 1, 1)

        self.label_35 = QLabel(self.widget_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setToolTipDuration(10000)
        self.label_35.setStyleSheet(u"font-style:italic;")
        self.label_35.setIndent(24)

        self.gridLayout_2.addWidget(self.label_35, 4, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_16, 8, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 7, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 6, 1, 1, 1)

        self.label_43 = QLabel(self.widget_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setToolTipDuration(10000)
        self.label_43.setStyleSheet(u"font-style:italic;")
        self.label_43.setIndent(24)

        self.gridLayout_2.addWidget(self.label_43, 11, 0, 1, 1)

        self.label_36 = QLabel(self.widget_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font6)
        self.label_36.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_36, 1, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 5, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 4, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 1, 1, 1, 1)

        self.label_37 = QLabel(self.widget_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setToolTipDuration(10000)
        self.label_37.setStyleSheet(u"font-style:italic;")
        self.label_37.setIndent(24)

        self.gridLayout_2.addWidget(self.label_37, 5, 0, 1, 1)

        self.plainTextEdit_11 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_11.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_11.setSizePolicy(sizePolicy4)
        self.plainTextEdit_11.setMaximumSize(QSize(206, 31))

        self.gridLayout_2.addWidget(self.plainTextEdit_11, 1, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 11, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 10, 1, 1, 1)

        self.label_33 = QLabel(self.widget_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_32, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)

        self.label_47 = QLabel(self.widget_5)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_47, 13, 0, 1, 1)

        self.label_48 = QLabel(self.widget_5)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_48, 14, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_22, 13, 1, 1, 1)

        self.plainTextEdit_12 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")

        self.gridLayout_2.addWidget(self.plainTextEdit_12, 5, 2, 1, 1)

        self.plainTextEdit_10 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")

        self.gridLayout_2.addWidget(self.plainTextEdit_10, 2, 2, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_23, 14, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 9, 1, 1, 1)

        self.label_38 = QLabel(self.widget_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_38, 6, 0, 1, 1)

        self.checkBox_18 = QCheckBox(self.widget_5)
        self.checkBox_18.setObjectName(u"checkBox_18")
        sizePolicy4.setHeightForWidth(self.checkBox_18.sizePolicy().hasHeightForWidth())
        self.checkBox_18.setSizePolicy(sizePolicy4)
        self.checkBox_18.setMinimumSize(QSize(0, 0))
        self.checkBox_18.setMaximumSize(QSize(40, 30))
        self.checkBox_18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_18.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_18.setIconSize(QSize(41, 41))
        self.checkBox_18.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_18, 12, 2, 1, 1, Qt.AlignHCenter)

        self.label_45 = QLabel(self.widget_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setToolTipDuration(10000)
        self.label_45.setStyleSheet(u"font-style:italic;")
        self.label_45.setIndent(24)

        self.gridLayout_2.addWidget(self.label_45, 12, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_20, 12, 1, 1, 1)

        self.plainTextEdit_17 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")

        self.gridLayout_2.addWidget(self.plainTextEdit_17, 14, 2, 1, 1)

        self.status_comboBox_2 = QComboBox(self.widget_5)
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.setObjectName(u"status_comboBox_2")
        self.status_comboBox_2.setMinimumSize(QSize(150, 16))
        self.status_comboBox_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.status_comboBox_2, 13, 2, 1, 1)

        self.plainTextEdit_13 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")

        self.gridLayout_2.addWidget(self.plainTextEdit_13, 7, 2, 1, 1)

        self.checkBox_19 = QCheckBox(self.widget_5)
        self.checkBox_19.setObjectName(u"checkBox_19")
        sizePolicy4.setHeightForWidth(self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy4)
        self.checkBox_19.setMinimumSize(QSize(0, 0))
        self.checkBox_19.setMaximumSize(QSize(40, 30))
        self.checkBox_19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_19.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_19.setIconSize(QSize(41, 41))
        self.checkBox_19.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_19, 11, 2, 1, 1, Qt.AlignHCenter)

        self.label_40 = QLabel(self.widget_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setToolTipDuration(10000)
        self.label_40.setStyleSheet(u"font-style:italic;")
        self.label_40.setIndent(24)

        self.gridLayout_2.addWidget(self.label_40, 7, 0, 1, 1)

        self.plainTextEdit_14 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")

        self.gridLayout_2.addWidget(self.plainTextEdit_14, 8, 2, 1, 1)

        self.checkBox_17 = QCheckBox(self.widget_5)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy4.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy4)
        self.checkBox_17.setMinimumSize(QSize(0, 0))
        self.checkBox_17.setMaximumSize(QSize(40, 30))
        self.checkBox_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_17.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_17.setIconSize(QSize(41, 41))
        self.checkBox_17.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_17, 10, 2, 1, 1, Qt.AlignHCenter)

        self.label_41 = QLabel(self.widget_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setToolTipDuration(10000)
        self.label_41.setStyleSheet(u"font-style:italic;")
        self.label_41.setIndent(24)

        self.gridLayout_2.addWidget(self.label_41, 8, 0, 1, 1)

        self.label_42 = QLabel(self.widget_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_42, 9, 0, 1, 1)

        self.label_44 = QLabel(self.widget_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setToolTipDuration(10000)
        self.label_44.setStyleSheet(u"font-style:italic;")
        self.label_44.setIndent(24)

        self.gridLayout_2.addWidget(self.label_44, 10, 0, 1, 1)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setToolTipDuration(10000)

        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 0, 1, 1, 1)

        self.plainTextEdit_9 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        sizePolicy4.setHeightForWidth(self.plainTextEdit_9.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_9.setSizePolicy(sizePolicy4)
        self.plainTextEdit_9.setMaximumSize(QSize(206, 31))

        self.gridLayout_2.addWidget(self.plainTextEdit_9, 0, 2, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout_2)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 25, -1, -1)
        self.mc_cancel_changes_btn_2 = QPushButton(self.widget_5)
        self.mc_cancel_changes_btn_2.setObjectName(u"mc_cancel_changes_btn_2")
        self.mc_cancel_changes_btn_2.setMinimumSize(QSize(0, 25))
        self.mc_cancel_changes_btn_2.setMaximumSize(QSize(161, 25))
        self.mc_cancel_changes_btn_2.setFont(font7)
        self.mc_cancel_changes_btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_cancel_changes_btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff;\n"
"    color: #FF3B30;\n"
"    padding: 2px;\n"
"    border: 2px solid #FF3B30 ;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E63946;\n"
"}\n"
"")
        self.mc_cancel_changes_btn_2.setCheckable(True)

        self.horizontalLayout_31.addWidget(self.mc_cancel_changes_btn_2)

        self.mc_save_changes_btn_2 = QPushButton(self.widget_5)
        self.mc_save_changes_btn_2.setObjectName(u"mc_save_changes_btn_2")
        self.mc_save_changes_btn_2.setMinimumSize(QSize(0, 25))
        self.mc_save_changes_btn_2.setMaximumSize(QSize(161, 25))
        self.mc_save_changes_btn_2.setFont(font7)
        self.mc_save_changes_btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_save_changes_btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #1C5739;\n"
"    color: white;\n"
"    padding: 2px;\n"
"    border: none;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #25754c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1C5739;\n"
"}\n"
"")
        self.mc_save_changes_btn_2.setCheckable(True)

        self.horizontalLayout_31.addWidget(self.mc_save_changes_btn_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_31)


        self.verticalLayout_11.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_27.addWidget(self.stackedWidget, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.Main)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.widget_3)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy6.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy6)
        self.gridLayout_3 = QGridLayout(self.webEngineView)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_16.addWidget(self.webEngineView)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setStyleSheet(u"border:none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.frame_7)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(31, 31))
        self.label_3.setMaximumSize(QSize(31, 31))
        self.label_3.setPixmap(QPixmap(u":/ICONS/pin-5-128 (1).png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        font8 = QFont()
        font8.setBold(True)
        self.label_6.setFont(font8)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.frame_7)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy6.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy6)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(31, 31))
        self.label_5.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)

        self.horizontalLayout_7.addWidget(self.label_7)


        self.horizontalLayout_5.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.frame_7)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy6.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy6)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(31, 31))
        self.label_4.setPixmap(QPixmap(u":/ICONS/pin-5-128 (2).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font8)

        self.horizontalLayout_8.addWidget(self.label_8)


        self.horizontalLayout_5.addWidget(self.widget_7)


        self.verticalLayout_16.addWidget(self.frame_7)


        self.horizontalLayout_27.addWidget(self.widget_3)

        self.horizontalLayout_27.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_17.addWidget(self.Main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.shelter_dropdown.toggled.connect(self.frame_6.setHidden)
        self.communities_dropdown_2.toggled.connect(self.frame_5.setHidden)
        self.pushButton_15.clicked.connect(self.stackedWidget.hide)
        self.pushButton_14.clicked.connect(self.stackedWidget.hide)

        self.communities_dropdown_2.setDefault(False)
        self.add_community_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shelter Location-Allocation System", None))
        self.communities_dropdown_2.setText(QCoreApplication.translate("MainWindow", u"Communities", None))
        self.add_community_btn.setText(QCoreApplication.translate("MainWindow", u"Add Community", None))
        self.advanced_settings_com.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.shelter_dropdown.setText(QCoreApplication.translate("MainWindow", u"Shelters", None))
        self.add_shelter_btn.setText(QCoreApplication.translate("MainWindow", u"Add Shelter", None))
        self.advanced_settings_shel.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.label_2.setText("")
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Report Preview", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Marker Options", None))
        self.marker_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SHOW Disabled Markers", None))
        self.marker_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"HIDE Disabled Markers", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Shelter Preview", None))
        self.shelterprev_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"---", None))
        self.shelterprev_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ALL", None))
        self.shelterprev_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Built", None))
        self.shelterprev_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Partially Built", None))
        self.shelterprev_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Damaged", None))
        self.shelterprev_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Empty Lot", None))
        self.shelterprev_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Resistant to Flood", None))
        self.shelterprev_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Resistant to Typhoon", None))
        self.shelterprev_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Resistant to Earthquake", None))

        self.solve_btn.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.pushButton_14.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Community Edit", None))
        self.checkBox_15.setText("")
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LONGITUDE </span>the angular distance of a place east or west of the meridian</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">POPULATION</span> number of people residing in the specified area</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Population", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">AFFECTED POPULATION</span> number of individuals impacted by a disaster or requiring shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"AffectedPop", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">MAX DISTANCE</span> farthest distance between a community and the assigned shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"MaxDistance", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LATITUDE </span>geographic coordinate that measures how far north or south a location is from the equator</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">REMARKS </span>additional notes or observations regarding the shelter location or allocation process.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Remarks", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">NAME</span> designated identifier of a specific community site</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.mc_cancel_changes_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.mc_save_changes_btn.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.pushButton_15.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Shelter Edit", None))
        self.checkBox_16.setText("")
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">AREA</span> total space occupied by a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Area", None))
#if QT_CONFIG(tooltip)
        self.label_43.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">TYPHOON</span> shelter\u2019s structural integrity against strong winds and heavy rains caused by typhoons</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Typhoon", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LATITUDE </span>geographic coordinate that measures how far north or south a location is from the equatora</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
#if QT_CONFIG(tooltip)
        self.label_37.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">COST</span> financial requirement for constructing, maintaining, or upgrading a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LEVEL 1</span> built shelter providing minimal protection and resources for temporary housing.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LONGITUDE </span>the angular distance of a place east or west of the meridian</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
#if QT_CONFIG(tooltip)
        self.label_47.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">STATUS</span> current condition, availability, or operational state of a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Status", None))
#if QT_CONFIG(tooltip)
        self.label_48.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">REMARKS </span>additional notes or observations regarding the shelter location or allocation process</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Remarks", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">LEVEL 2</span> upgraded shelter with improved durability, capacity, and facilities</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.checkBox_18.setText("")
#if QT_CONFIG(tooltip)
        self.label_45.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">EARTHQUAKE</span> shelter\u2019s capability to endure seismic activity and ground shaking</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Earthquake", None))
        self.status_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Built", None))
        self.status_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Partially Built", None))
        self.status_comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Damaged", None))
        self.status_comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Empty Lot", None))

        self.checkBox_19.setText("")
#if QT_CONFIG(tooltip)
        self.label_40.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">AREA</span> total space occupied by a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.checkBox_17.setText("")
#if QT_CONFIG(tooltip)
        self.label_41.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">COST</span> financial requirement for constructing, maintaining, or upgrading a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">RESISTANCE</span> ability of a shelter to withstand natural disasters and environmental hazards</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Resitance", None))
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">FLOOD</span> a shelter can resist or withstand flooding events</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Flood", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">NAME</span> designated identifier of a specific shelter site</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.mc_cancel_changes_btn_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.mc_save_changes_btn_2.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Shelters", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Communities", None))
        self.label_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
    # retranslateUi

