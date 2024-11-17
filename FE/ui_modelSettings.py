# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelSettings.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_modelSettings(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 462)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(350, 700))
        Dialog.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.widget_4 = QWidget(Dialog)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.modelSettings_back_btn = QPushButton(self.widget_4)
        self.modelSettings_back_btn.setObjectName(u"modelSettings_back_btn")
        self.modelSettings_back_btn.setMinimumSize(QSize(30, 41))
        self.modelSettings_back_btn.setMaximumSize(QSize(25, 41))
        self.modelSettings_back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modelSettings_back_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelSettings_back_btn.setIcon(icon)
        self.modelSettings_back_btn.setIconSize(QSize(41, 41))

        self.horizontalLayout_28.addWidget(self.modelSettings_back_btn)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        font = QFont()
        font.setFamilies([u"Ms Shell Dlg 2"])
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-family: \"Ms Shell Dlg 2\";\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"    text-decoration: none;\n"
"}")

        self.horizontalLayout_28.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_28)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 6, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 6, 1, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout.addWidget(self.plainTextEdit_4, 5, 2, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout.addWidget(self.plainTextEdit_3, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setFamilies([u"Ms Shell Dlg 2"])
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_19.setFont(font1)

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 3, 2, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 1, 0, 1, 1)

        self.hierarchy_checkBox = QCheckBox(self.widget_4)
        self.hierarchy_checkBox.setObjectName(u"hierarchy_checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hierarchy_checkBox.sizePolicy().hasHeightForWidth())
        self.hierarchy_checkBox.setSizePolicy(sizePolicy1)
        self.hierarchy_checkBox.setMinimumSize(QSize(0, 0))
        self.hierarchy_checkBox.setMaximumSize(QSize(40, 30))
        self.hierarchy_checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hierarchy_checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"}")
        self.hierarchy_checkBox.setIconSize(QSize(41, 41))
        self.hierarchy_checkBox.setChecked(False)

        self.gridLayout.addWidget(self.hierarchy_checkBox, 6, 2, 1, 1, Qt.AlignHCenter)

        self.model_comboBox = QComboBox(self.widget_4)
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.setObjectName(u"model_comboBox")
        self.model_comboBox.setMinimumSize(QSize(150, 16))
        self.model_comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.model_comboBox.setStyleSheet(u"")

        self.gridLayout.addWidget(self.model_comboBox, 0, 2, 1, 1)

        self.label_31 = QLabel(self.widget_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)

        self.plainTextEdit_8 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")

        self.gridLayout.addWidget(self.plainTextEdit_8, 1, 2, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")

        self.gridLayout.addWidget(self.plainTextEdit_6, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.modelSettings_done_btn = QPushButton(self.widget_4)
        self.modelSettings_done_btn.setObjectName(u"modelSettings_done_btn")
        self.modelSettings_done_btn.setMinimumSize(QSize(161, 51))
        self.modelSettings_done_btn.setMaximumSize(QSize(161, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.modelSettings_done_btn.setFont(font2)
        self.modelSettings_done_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modelSettings_done_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #1C5739;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
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

        self.verticalLayout_2.addWidget(self.modelSettings_done_btn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.modelSettings_back_btn.setText("")
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Model Settings", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Population", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Mutation", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Hierarchy ", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Generation", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Model", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"WeightDistance", None))
        self.hierarchy_checkBox.setText("")
        self.model_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Bilevel No Transfer (BNT)", None))
        self.model_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Single-level with Workplace Distance Inclusion (WORK)", None))

        self.label_31.setText(QCoreApplication.translate("Dialog", u"WeightCost", None))
        self.modelSettings_done_btn.setText(QCoreApplication.translate("Dialog", u"DONE", None))
    # retranslateUi

