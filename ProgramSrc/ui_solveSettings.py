# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solveSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_solveSettings(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(855, 474)
        Dialog.setToolTipDuration(-2)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(8, 0, 8, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMaximumSize(QSize(16777215, 40))
        self.frame_10.setStyleSheet(u"margin:0;\n"
"padding:0;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(5000, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_14.setFont(font1)
        self.label_14.setToolTipDuration(10000)
        self.label_14.setStyleSheet(u"margin-right:;")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.write_community_btn = QPushButton(self.frame_10)
        self.write_community_btn.setObjectName(u"write_community_btn")
        self.write_community_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.write_community_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/9022659_duotone_note_pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.write_community_btn.setIcon(icon)
        self.write_community_btn.setIconSize(QSize(30, 30))
        self.write_community_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.write_community_btn)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.scrollArea_2 = QScrollArea(self.frame_9)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMaximumSize(QSize(16777215, 160))
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"border: 1px solid gray;\n"
"background-color: white;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 364, 239))
        font2 = QFont()
        font2.setBold(True)
        self.scrollAreaWidgetContents_4.setFont(font2)
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color: white;\n"
"color:rgb(43, 43, 43);")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.scrollAreaWidgetContents_4)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_17.setFont(font3)
        self.label_17.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_17.setFrameShape(QFrame.Box)
        self.label_17.setFrameShadow(QFrame.Raised)
        self.label_17.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_17)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 100))
        self.label_19.setFont(font3)
        self.label_19.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_19.setFrameShape(QFrame.Box)
        self.label_19.setFrameShadow(QFrame.Raised)
        self.label_19.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_19)

        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 100))
        self.label_31.setFont(font3)
        self.label_31.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_31.setFrameShape(QFrame.NoFrame)
        self.label_31.setFrameShadow(QFrame.Plain)
        self.label_31.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_31)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 100))
        self.label_21.setFont(font3)
        self.label_21.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_21.setFrameShape(QFrame.Box)
        self.label_21.setFrameShadow(QFrame.Raised)
        self.label_21.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_21)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 100))
        self.label_32.setFont(font3)
        self.label_32.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_32.setFrameShape(QFrame.Box)
        self.label_32.setFrameShadow(QFrame.Raised)
        self.label_32.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_32)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 100))
        self.label_16.setFont(font3)
        self.label_16.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_16.setFrameShape(QFrame.Box)
        self.label_16.setFrameShadow(QFrame.Raised)
        self.label_16.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_16)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 100))
        self.label_18.setFont(font3)
        self.label_18.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_18)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 100))
        self.label_30.setFont(font3)
        self.label_30.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_30.setFrameShape(QFrame.Box)
        self.label_30.setFrameShadow(QFrame.Raised)
        self.label_30.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.label_30)


        self.verticalLayout_6.addWidget(self.widget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 8)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 8, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setStyleSheet(u"margin:0;\n"
"padding:0;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(5000, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setToolTipDuration(10000)
        self.label_3.setStyleSheet(u"margin-right:;")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.write_shelter_btn = QPushButton(self.frame_6)
        self.write_shelter_btn.setObjectName(u"write_shelter_btn")
        self.write_shelter_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.write_shelter_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"	align: right;\n"
"}")
        self.write_shelter_btn.setIcon(icon)
        self.write_shelter_btn.setIconSize(QSize(30, 30))
        self.write_shelter_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.write_shelter_btn)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.scrollArea = QScrollArea(self.frame_5)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 160))
        self.scrollArea.setMaximumSize(QSize(16777215, 160))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border: 1px solid gray;\n"
"background-color: white;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 384, 148))
        self.scrollAreaWidgetContents_2.setFont(font2)
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: white;\n"
"color:rgb(43, 43, 43);")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.verticalWidget, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea, 0, Qt.AlignTop)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 8)

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 0, 8, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QSize(16777215, 40))
        self.frame_12.setToolTipDuration(10000)
        self.frame_12.setStyleSheet(u"margin:0;\n"
"padding:0;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(5000, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setUnderline(True)
        self.label_20.setFont(font4)
        self.label_20.setToolTipDuration(10000)
        self.label_20.setStyleSheet(u"margin-right:;")

        self.horizontalLayout_7.addWidget(self.label_20)

        self.shelter_res_checkbox = QCheckBox(self.frame_12)
        self.shelter_res_checkbox.setObjectName(u"shelter_res_checkbox")
        self.shelter_res_checkbox.setMaximumSize(QSize(30, 30))
        self.shelter_res_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelter_res_checkbox.setChecked(False)

        self.horizontalLayout_7.addWidget(self.shelter_res_checkbox)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.scrollArea_4 = QScrollArea(self.frame_11)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy1)
        self.scrollArea_4.setStyleSheet(u"QScrollArea{\n"
"border: 1px solid gray;\n"
"background-color: white;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 385, 114))
        self.scrollAreaWidgetContents_5.setFont(font2)
        self.scrollAreaWidgetContents_5.setStyleSheet(u"background-color: white;\n"
"color:rgb(43, 43, 43);")
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 100))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_22.setFont(font5)
        self.label_22.setToolTipDuration(10000)

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 100))
        self.label_23.setFont(font5)
        self.label_23.setToolTipDuration(10000)

        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 100))
        self.label_24.setFont(font5)
        self.label_24.setToolTipDuration(10000)

        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)

        self.shelter_res_flood_checkbox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.shelter_res_flood_checkbox.setObjectName(u"shelter_res_flood_checkbox")
        self.shelter_res_flood_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_res_flood_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.shelter_res_flood_checkbox, 0, 1, 1, 1)

        self.shelter_res_earthquake_checkbox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.shelter_res_earthquake_checkbox.setObjectName(u"shelter_res_earthquake_checkbox")
        self.shelter_res_earthquake_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_res_earthquake_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.shelter_res_earthquake_checkbox, 2, 1, 1, 1)

        self.shelter_res_typhoon_checkbox = QCheckBox(self.scrollAreaWidgetContents_5)
        self.shelter_res_typhoon_checkbox.setObjectName(u"shelter_res_typhoon_checkbox")
        self.shelter_res_typhoon_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_res_typhoon_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.shelter_res_typhoon_checkbox, 1, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_8.addWidget(self.scrollArea_4)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 8)

        self.horizontalLayout_3.addWidget(self.frame_11)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 0, 8, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setToolTipDuration(10000)
        self.frame_8.setStyleSheet(u"margin:0;\n"
"padding:0;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(5000, 16777215))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"margin-right:;")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.shelter_stat_checkbox = QCheckBox(self.frame_8)
        self.shelter_stat_checkbox.setObjectName(u"shelter_stat_checkbox")
        self.shelter_stat_checkbox.setMaximumSize(QSize(30, 30))
        self.shelter_stat_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shelter_stat_checkbox.setChecked(False)

        self.horizontalLayout_5.addWidget(self.shelter_stat_checkbox)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.scrollArea_5 = QScrollArea(self.frame_7)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy1.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy1)
        self.scrollArea_5.setStyleSheet(u"QScrollArea{\n"
"border: 1px solid gray;\n"
"background-color: white;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 363, 131))
        self.scrollAreaWidgetContents_6.setFont(font2)
        self.scrollAreaWidgetContents_6.setStyleSheet(u"background-color: white;\n"
"color:rgb(43, 43, 43);")
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_26 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 100))
        self.label_26.setFont(font5)
        self.label_26.setToolTipDuration(10000)

        self.gridLayout_4.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 100))
        self.label_27.setFont(font5)
        self.label_27.setToolTipDuration(10000)

        self.gridLayout_4.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 100))
        self.label_28.setFont(font5)
        self.label_28.setToolTipDuration(10000)

        self.gridLayout_4.addWidget(self.label_28, 2, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 100))
        self.label_29.setFont(font5)
        self.label_29.setToolTipDuration(10000)

        self.gridLayout_4.addWidget(self.label_29, 3, 0, 1, 1)

        self.shelter_stat_built_checkbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.shelter_stat_built_checkbox.setObjectName(u"shelter_stat_built_checkbox")
        self.shelter_stat_built_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_stat_built_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.shelter_stat_built_checkbox, 0, 1, 1, 1)

        self.shelter_stat_pbuilt_checkbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.shelter_stat_pbuilt_checkbox.setObjectName(u"shelter_stat_pbuilt_checkbox")
        self.shelter_stat_pbuilt_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_stat_pbuilt_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.shelter_stat_pbuilt_checkbox, 1, 1, 1, 1)

        self.shelter_stat_dmg_checkbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.shelter_stat_dmg_checkbox.setObjectName(u"shelter_stat_dmg_checkbox")
        self.shelter_stat_dmg_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_stat_dmg_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.shelter_stat_dmg_checkbox, 2, 1, 1, 1)

        self.shelter_stat_empty_lot_checkbox = QCheckBox(self.scrollAreaWidgetContents_6)
        self.shelter_stat_empty_lot_checkbox.setObjectName(u"shelter_stat_empty_lot_checkbox")
        self.shelter_stat_empty_lot_checkbox.setMaximumSize(QSize(30, 16777215))
        self.shelter_stat_empty_lot_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.shelter_stat_empty_lot_checkbox, 3, 1, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_4.addWidget(self.scrollArea_5)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.label.setFont(font6)
        self.label.setToolTipDuration(10000)
        self.label.setStyleSheet(u"qproperty-alignment: AlignRight;")

        self.verticalLayout.addWidget(self.label)

        self.solveSet_adc_set_btn = QPushButton(self.frame_2)
        self.solveSet_adc_set_btn.setObjectName(u"solveSet_adc_set_btn")
        font7 = QFont()
        font7.setPointSize(8)
        font7.setUnderline(True)
        self.solveSet_adc_set_btn.setFont(font7)
        self.solveSet_adc_set_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solveSet_adc_set_btn.setStyleSheet(u"border: none;\n"
"background: none;\n"
"text-decoration: underline;\n"
"color:rgb(0, 0, 255);\n"
"text-align: right;")

        self.verticalLayout.addWidget(self.solveSet_adc_set_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.model_pick_comboBox = QComboBox(self.frame_2)
        self.model_pick_comboBox.addItem("")
        self.model_pick_comboBox.setObjectName(u"model_pick_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.model_pick_comboBox.sizePolicy().hasHeightForWidth())
        self.model_pick_comboBox.setSizePolicy(sizePolicy2)
        self.model_pick_comboBox.setMinimumSize(QSize(400, 0))
        self.model_pick_comboBox.setMaximumSize(QSize(400, 16777215))
        font8 = QFont()
        font8.setPointSize(11)
        self.model_pick_comboBox.setFont(font8)
        self.model_pick_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.model_pick_comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid gray;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QComboBox::dropdown {\n"
"	border-left: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.model_pick_comboBox)

        self.solveSet_solve_btn = QPushButton(self.frame_2)
        self.solveSet_solve_btn.setObjectName(u"solveSet_solve_btn")
        font9 = QFont()
        font9.setPointSize(16)
        font9.setBold(True)
        self.solveSet_solve_btn.setFont(font9)
        self.solveSet_solve_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solveSet_solve_btn.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 87, 57, 255), stop:1 rgba(61, 189, 124, 255));\n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"padding:8px 80px;\n"
"border-radius:8;\n"
"margin-left:40px;")

        self.horizontalLayout.addWidget(self.solveSet_solve_btn)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        Dialog.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">SELECTED COMMUNITIES</span> shows the list of communities that will be used in the model</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_14.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Selected Communities", None))
        self.write_community_btn.setText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Barangay A", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Barangay B", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Barangay D", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Barangay A", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Barangay B", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Barangay C", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Barangay D", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Barangay C", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">SHELTER DATA</span> shows the list of shelters that will be used in the model</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_3.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_3.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Selected Shelters", None))
        self.write_shelter_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Shelter B", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Shelter A", None))
#if QT_CONFIG(tooltip)
        self.frame_12.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Shelter Resistance</span> represent the ability of a shelter to withstand specific environmental disaster/s. Select the types of disasters that the shelter can withstand.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SHELTER RESISTANCE</span> represent the ability of a shelter to withstand specific environmental disaster/s. Select the types of disasters that the shelter can withstand.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_20.setWhatsThis(QCoreApplication.translate("Dialog", u"hello", None))
#endif // QT_CONFIG(whatsthis)
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Shelter Resistance", None))
        self.shelter_res_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">FLOOD</span> a shelter can resist or withstand flooding events</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Flood", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">TYPHOON</span> shelter\u2019s structural integrity against strong winds and heavy rains caused by typhoons</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Typhoon", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">EARTHQUAKE</span> shelter\u2019s capability to endure seismic activity and ground shaking</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Earthquake", None))
        self.shelter_res_flood_checkbox.setText("")
        self.shelter_res_earthquake_checkbox.setText("")
        self.shelter_res_typhoon_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.frame_8.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Shelter Status</span> indicates the current condition of the shelter. Select the condition type for the evacuees to stay in.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">SHELTER STATUS</span> indicates the current condition of the shelter. Select the condition type for the evacuees to stay in.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Shelter Status", None))
        self.shelter_stat_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">BUILT</span> The shelter is fully constructed and ready for use.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Built", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">PARTIALLY BUILT</span> the shelter is incomplete but may offer some protection.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Partially Built", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">DAMAGED</span> the shelter is in need of repairs but is still usable.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Damaged", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">EMPTY LOT</span> no shelter has been built on this site yet.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Empty Lot", None))
        self.shelter_stat_built_checkbox.setText("")
        self.shelter_stat_pbuilt_checkbox.setText("")
        self.shelter_stat_dmg_checkbox.setText("")
        self.shelter_stat_empty_lot_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">MODEL</span> select to use which model is appropriate</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"Model", None))
        self.solveSet_adc_set_btn.setText(QCoreApplication.translate("Dialog", u"Advanced Settings", None))
        self.model_pick_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Bilevel No Transfer (BNT)", None))

        self.solveSet_solve_btn.setText(QCoreApplication.translate("Dialog", u"SOLVE", None))
    # retranslateUi

