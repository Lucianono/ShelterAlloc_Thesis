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
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_17 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.SideBar = QWidget(self.centralwidget)
        self.SideBar.setObjectName(u"SideBar")
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
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
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 331, 718))
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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(31, 31))
        self.label_24.setMaximumSize(QSize(31, 31))
        self.label_24.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_24)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.label_16.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_16)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.barangay_a_btn = QPushButton(self.frame_5)
        self.barangay_a_btn.setObjectName(u"barangay_a_btn")
        self.barangay_a_btn.setMinimumSize(QSize(41, 41))
        self.barangay_a_btn.setMaximumSize(QSize(41, 41))
        self.barangay_a_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_a_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/ICONS/462544067_1241440546885630_5886192978905579196_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.barangay_a_btn.setIcon(icon2)
        self.barangay_a_btn.setIconSize(QSize(41, 41))
        self.barangay_a_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.barangay_a_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(31, 31))
        self.label_21.setMaximumSize(QSize(31, 31))
        self.label_21.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_21)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.barangay_b_btn = QPushButton(self.frame_5)
        self.barangay_b_btn.setObjectName(u"barangay_b_btn")
        self.barangay_b_btn.setMinimumSize(QSize(41, 41))
        self.barangay_b_btn.setMaximumSize(QSize(41, 41))
        self.barangay_b_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_b_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.barangay_b_btn.setIcon(icon2)
        self.barangay_b_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_8.addWidget(self.barangay_b_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(31, 31))
        self.label_22.setMaximumSize(QSize(31, 31))
        self.label_22.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_5)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.barangay_c_btn = QPushButton(self.frame_5)
        self.barangay_c_btn.setObjectName(u"barangay_c_btn")
        self.barangay_c_btn.setMinimumSize(QSize(41, 41))
        self.barangay_c_btn.setMaximumSize(QSize(41, 41))
        self.barangay_c_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_c_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.barangay_c_btn.setIcon(icon2)
        self.barangay_c_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_10.addWidget(self.barangay_c_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(31, 31))
        self.label_25.setMaximumSize(QSize(31, 31))
        self.label_25.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_25)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_21.addWidget(self.label_12)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)

        self.barangay_d_btn = QPushButton(self.frame_5)
        self.barangay_d_btn.setObjectName(u"barangay_d_btn")
        self.barangay_d_btn.setMinimumSize(QSize(41, 41))
        self.barangay_d_btn.setMaximumSize(QSize(41, 41))
        self.barangay_d_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_d_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.barangay_d_btn.setIcon(icon2)
        self.barangay_d_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_20.addWidget(self.barangay_d_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(31, 31))
        self.label_23.setMaximumSize(QSize(31, 31))
        self.label_23.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.barangay_e_btn = QPushButton(self.frame_5)
        self.barangay_e_btn.setObjectName(u"barangay_e_btn")
        self.barangay_e_btn.setMinimumSize(QSize(41, 41))
        self.barangay_e_btn.setMaximumSize(QSize(41, 41))
        self.barangay_e_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_e_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.barangay_e_btn.setIcon(icon2)
        self.barangay_e_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_12.addWidget(self.barangay_e_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(31, 31))
        self.label_26.setMaximumSize(QSize(31, 31))
        self.label_26.setPixmap(QPixmap(u":/ICONS/pin-5-128.png"))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_26)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.horizontalLayout_23.addWidget(self.label_13)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)

        self.barangay_f_btn = QPushButton(self.frame_5)
        self.barangay_f_btn.setObjectName(u"barangay_f_btn")
        self.barangay_f_btn.setMinimumSize(QSize(41, 41))
        self.barangay_f_btn.setMaximumSize(QSize(41, 41))
        self.barangay_f_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.barangay_f_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.barangay_f_btn.setIcon(icon2)
        self.barangay_f_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_22.addWidget(self.barangay_f_btn)


        self.communities_dropdown.addLayout(self.horizontalLayout_22)


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
"    background-color: #0e4c87;\n"
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

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(31, 31))
        self.label_3.setMaximumSize(QSize(31, 31))
        self.label_3.setPixmap(QPixmap(u":/ICONS/pin-5-128 (1).png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_3)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_9.setFont(font4)

        self.horizontalLayout_13.addWidget(self.label_9)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.shelter_a_btn = QPushButton(self.frame_6)
        self.shelter_a_btn.setObjectName(u"shelter_a_btn")
        self.shelter_a_btn.setMinimumSize(QSize(41, 41))
        self.shelter_a_btn.setMaximumSize(QSize(41, 41))
        self.shelter_a_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelter_a_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.shelter_a_btn.setIcon(icon2)
        self.shelter_a_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_14.addWidget(self.shelter_a_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(31, 31))
        self.label_17.setMaximumSize(QSize(31, 31))
        self.label_17.setPixmap(QPixmap(u":/ICONS/pin-5-128 (1).png"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_10)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.shelter_b_btn = QPushButton(self.frame_6)
        self.shelter_b_btn.setObjectName(u"shelter_b_btn")
        self.shelter_b_btn.setMinimumSize(QSize(41, 41))
        self.shelter_b_btn.setMaximumSize(QSize(41, 41))
        self.shelter_b_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelter_b_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.shelter_b_btn.setIcon(icon2)
        self.shelter_b_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_16.addWidget(self.shelter_b_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)


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
        self.widget_2.setMaximumSize(QSize(16777215, 50))
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
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.reports_btn.setFont(font5)
        self.reports_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reports_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.reports_btn)

        self.help_btn = QPushButton(self.frame_4)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setFont(font5)
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.help_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.help_btn)

        self.account_btn = QPushButton(self.frame_4)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setFont(font5)
        self.account_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.account_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
"	border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.account_btn)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.horizontalLayout_19.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.resistance_comboBox = QComboBox(self.widget_2)
        self.resistance_comboBox.addItem("")
        self.resistance_comboBox.addItem("")
        self.resistance_comboBox.addItem("")
        self.resistance_comboBox.addItem("")
        self.resistance_comboBox.setObjectName(u"resistance_comboBox")
        self.resistance_comboBox.setMinimumSize(QSize(150, 0))
        self.resistance_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.resistance_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	selection-background-color: #2980B9;\n"
"	height: 20px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.resistance_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.status_comboBox = QComboBox(self.widget_2)
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.setObjectName(u"status_comboBox")
        self.status_comboBox.setMinimumSize(QSize(150, 0))
        self.status_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.status_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"	selection-background-color: #2980B9;\n"
"	height: 20px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.status_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.setStretch(0, 3)
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
        self.stackedWidget.setMinimumSize(QSize(0, 800))
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
"}")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.page.setMinimumSize(QSize(0, 700))
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_14 = QPushButton(self.widget_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(30, 41))
        self.pushButton_14.setMaximumSize(QSize(25, 41))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QSize(41, 41))

        self.horizontalLayout_28.addWidget(self.pushButton_14)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        font6 = QFont()
        font6.setFamilies([u"Ms Shell Dlg 2"])
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: none;\n"
"}")

        self.horizontalLayout_28.addWidget(self.label_18)

        self.checkBox_15 = QCheckBox(self.widget_4)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy2)
        self.checkBox_15.setMinimumSize(QSize(0, 0))
        self.checkBox_15.setMaximumSize(QSize(40, 40))
        self.checkBox_15.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_15.setIconSize(QSize(41, 41))
        self.checkBox_15.setChecked(False)

        self.horizontalLayout_28.addWidget(self.checkBox_15)

        self.pushButton_16 = QPushButton(self.widget_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(41, 41))
        self.pushButton_16.setMaximumSize(QSize(41, 41))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/ICONS/9022869_duotone_trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon4)
        self.pushButton_16.setIconSize(QSize(41, 41))

        self.horizontalLayout_28.addWidget(self.pushButton_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout.addWidget(self.plainTextEdit_3, 2, 2, 1, 1)

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.plainTextEdit_5 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")

        self.gridLayout.addWidget(self.plainTextEdit_5, 4, 2, 1, 1)

        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 4, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 1, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout.addWidget(self.plainTextEdit_4, 3, 2, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 2, 1, 1)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        font7 = QFont()
        font7.setFamilies([u"Ms Shell Dlg 2"])
        font7.setBold(True)
        font7.setUnderline(True)
        self.label_19.setFont(font7)

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.widget_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        self.plainTextEdit.setMaximumSize(QSize(206, 31))

        self.gridLayout.addWidget(self.plainTextEdit, 0, 2, 1, 1, Qt.AlignHCenter)

        self.plainTextEdit_6 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")

        self.gridLayout.addWidget(self.plainTextEdit_6, 5, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 1, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 5, 0, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout)


        self.verticalLayout_13.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy2.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy2)
        self.page_2.setMinimumSize(QSize(0, 800))
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 750))
        self.scrollArea.setStyleSheet(u"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 371, 750))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 41))
        self.pushButton_15.setMaximumSize(QSize(25, 41))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setIconSize(QSize(41, 41))

        self.horizontalLayout_29.addWidget(self.pushButton_15)

        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: none;\n"
"}")

        self.horizontalLayout_29.addWidget(self.label_31)

        self.checkBox_16 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy2.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy2)
        self.checkBox_16.setMinimumSize(QSize(0, 0))
        self.checkBox_16.setMaximumSize(QSize(40, 40))
        self.checkBox_16.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_16.setIconSize(QSize(41, 41))
        self.checkBox_16.setChecked(False)

        self.horizontalLayout_29.addWidget(self.checkBox_16)

        self.pushButton_17 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(41, 41))
        self.pushButton_17.setMaximumSize(QSize(41, 41))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        self.pushButton_17.setIcon(icon4)
        self.pushButton_17.setIconSize(QSize(41, 41))

        self.horizontalLayout_29.addWidget(self.pushButton_17)


        self.verticalLayout_11.addLayout(self.horizontalLayout_29)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(12)
        self.label_32 = QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_2.addWidget(self.label_32, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 3, 1, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font-style:italic;")
        self.label_34.setIndent(24)

        self.gridLayout_2.addWidget(self.label_34, 3, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 2, 1, 1, 1)

        self.plainTextEdit_8 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")

        self.gridLayout_2.addWidget(self.plainTextEdit_8, 4, 2, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font-style:italic;")
        self.label_35.setIndent(24)

        self.gridLayout_2.addWidget(self.label_35, 4, 0, 1, 1)

        self.plainTextEdit_9 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")

        self.gridLayout_2.addWidget(self.plainTextEdit_9, 3, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 4, 1, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font7)

        self.gridLayout_2.addWidget(self.label_36, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.plainTextEdit_11 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        sizePolicy2.setHeightForWidth(self.plainTextEdit_11.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_11.setSizePolicy(sizePolicy2)
        self.plainTextEdit_11.setMaximumSize(QSize(204, 29))

        self.gridLayout_2.addWidget(self.plainTextEdit_11, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font-style:italic;")
        self.label_37.setIndent(24)

        self.gridLayout_2.addWidget(self.label_37, 5, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 5, 1, 1, 1)

        self.plainTextEdit_12 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")

        self.gridLayout_2.addWidget(self.plainTextEdit_12, 5, 2, 1, 1)

        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_2.addWidget(self.label_47, 15, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_23, 16, 1, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_2.addWidget(self.label_48, 16, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_22, 15, 1, 1, 1)

        self.plainTextEdit_10 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")

        self.gridLayout_2.addWidget(self.plainTextEdit_10, 1, 2, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font-style:italic;")
        self.label_43.setIndent(24)

        self.gridLayout_2.addWidget(self.label_43, 12, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 10, 1, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 6, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_16, 9, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 6, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 8, 1, 1, 1)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font-style:italic;")
        self.label_39.setIndent(24)

        self.gridLayout_2.addWidget(self.label_39, 7, 0, 1, 1)

        self.plainTextEdit_15 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")

        self.gridLayout_2.addWidget(self.plainTextEdit_15, 7, 2, 1, 1)

        self.plainTextEdit_13 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")

        self.gridLayout_2.addWidget(self.plainTextEdit_13, 8, 2, 1, 1)

        self.plainTextEdit_14 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")

        self.gridLayout_2.addWidget(self.plainTextEdit_14, 9, 2, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font-style:italic;")
        self.label_40.setIndent(24)

        self.gridLayout_2.addWidget(self.label_40, 8, 0, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font-style:italic;")
        self.label_41.setIndent(24)

        self.gridLayout_2.addWidget(self.label_41, 9, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 7, 1, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 10, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy2.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy2)
        self.checkBox_17.setMinimumSize(QSize(0, 0))
        self.checkBox_17.setMaximumSize(QSize(40, 30))
        self.checkBox_17.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_17.setIconSize(QSize(41, 41))
        self.checkBox_17.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_17, 11, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_20 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_20.setObjectName(u"checkBox_20")
        sizePolicy2.setHeightForWidth(self.checkBox_20.sizePolicy().hasHeightForWidth())
        self.checkBox_20.setSizePolicy(sizePolicy2)
        self.checkBox_20.setMinimumSize(QSize(0, 0))
        self.checkBox_20.setMaximumSize(QSize(40, 30))
        self.checkBox_20.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_20.setIconSize(QSize(41, 41))
        self.checkBox_20.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_20, 14, 2, 1, 1, Qt.AlignHCenter)

        self.label_44 = QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font-style:italic;")
        self.label_44.setIndent(24)

        self.gridLayout_2.addWidget(self.label_44, 11, 0, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font-style:italic;")
        self.label_45.setIndent(24)

        self.gridLayout_2.addWidget(self.label_45, 13, 0, 1, 1)

        self.label_46 = QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font-style:italic;")
        self.label_46.setIndent(24)

        self.gridLayout_2.addWidget(self.label_46, 14, 0, 1, 1)

        self.checkBox_18 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_18.setObjectName(u"checkBox_18")
        sizePolicy2.setHeightForWidth(self.checkBox_18.sizePolicy().hasHeightForWidth())
        self.checkBox_18.setSizePolicy(sizePolicy2)
        self.checkBox_18.setMinimumSize(QSize(0, 0))
        self.checkBox_18.setMaximumSize(QSize(40, 30))
        self.checkBox_18.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_18.setIconSize(QSize(41, 41))
        self.checkBox_18.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_18, 13, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_20, 13, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 12, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 14, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 11, 1, 1, 1)

        self.checkBox_19 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_19.setObjectName(u"checkBox_19")
        sizePolicy2.setHeightForWidth(self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy2)
        self.checkBox_19.setMinimumSize(QSize(0, 0))
        self.checkBox_19.setMaximumSize(QSize(40, 30))
        self.checkBox_19.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.checkBox_19.setIconSize(QSize(41, 41))
        self.checkBox_19.setChecked(False)

        self.gridLayout_2.addWidget(self.checkBox_19, 12, 2, 1, 1, Qt.AlignHCenter)

        self.plainTextEdit_17 = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")

        self.gridLayout_2.addWidget(self.plainTextEdit_17, 16, 2, 1, 1)

        self.status_comboBox_2 = QComboBox(self.scrollAreaWidgetContents)
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.addItem("")
        self.status_comboBox_2.setObjectName(u"status_comboBox_2")
        self.status_comboBox_2.setMinimumSize(QSize(150, 14))
        self.status_comboBox_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.status_comboBox_2, 15, 2, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_27.addWidget(self.stackedWidget, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.Main)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.webEngineView = QWebEngineView(self.widget_3)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy4.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.webEngineView)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_4.addWidget(self.webEngineView, 1, 0, 1, 1)

        self.solve_btn = QPushButton(self.widget_3)
        self.solve_btn.setObjectName(u"solve_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.solve_btn.sizePolicy().hasHeightForWidth())
        self.solve_btn.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setPointSize(24)
        font8.setBold(True)
        self.solve_btn.setFont(font8)
        self.solve_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solve_btn.setStyleSheet(u"* {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 87, 57, 255), stop:1 rgba(61, 189, 124, 255));\n"
"	color: white;\n"
"	padding:10;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(61, 189, 124, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.solve_btn, 2, 0, 1, 1)


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
        self.label_24.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Barangay A", None))
        self.barangay_a_btn.setText("")
        self.label_21.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Barangay B", None))
        self.barangay_b_btn.setText("")
        self.label_22.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Barangay C", None))
        self.barangay_c_btn.setText("")
        self.label_25.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Barangay D", None))
        self.barangay_d_btn.setText("")
        self.label_23.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Barangay E", None))
        self.barangay_e_btn.setText("")
        self.label_26.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Barangay F", None))
        self.barangay_f_btn.setText("")
        self.shelter_dropdown.setText(QCoreApplication.translate("MainWindow", u"Shelters", None))
        self.add_shelter_btn.setText(QCoreApplication.translate("MainWindow", u"Add Shelter", None))
        self.advanced_settings_shel.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.label_3.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Shelter A", None))
        self.shelter_a_btn.setText("")
        self.label_17.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Shelter B", None))
        self.shelter_b_btn.setText("")
        self.label_2.setText("")
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.account_btn.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_11.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Resistance", None))
        self.resistance_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))
        self.resistance_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Flood", None))
        self.resistance_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Typhoon", None))
        self.resistance_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Earthquake", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.status_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))
        self.status_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Built", None))
        self.status_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Partially Built", None))
        self.status_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Damaged", None))
        self.status_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Empty Lot", None))

        self.pushButton_14.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Barangay A", None))
        self.checkBox_15.setText("")
        self.pushButton_16.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"yDegrees", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"VulnerablePop", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"WorkingPop", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"xDegrees", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Remarks", None))
        self.pushButton_15.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Shelter A", None))
        self.checkBox_16.setText("")
        self.pushButton_17.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"yDegrees", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"xDegrees", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Remarks", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Typhoon", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Cost", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Resitance", None))
        self.checkBox_17.setText("")
        self.checkBox_20.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Flood", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Earthquake", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Volcanic", None))
        self.checkBox_18.setText("")
        self.checkBox_19.setText("")
        self.status_comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Built", None))
        self.status_comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Partially Built", None))
        self.status_comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Damaged", None))
        self.status_comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Empty Lot", None))

        self.solve_btn.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
    # retranslateUi

