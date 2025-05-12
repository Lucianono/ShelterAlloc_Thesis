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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_modelSettings(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 550)
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
        self.label_32 = QLabel(self.widget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_30, 4, 0, 1, 1)

        self.textEdit_generations = QPlainTextEdit(self.widget_4)
        self.textEdit_generations.setObjectName(u"textEdit_generations")

        self.gridLayout.addWidget(self.textEdit_generations, 6, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 3, 1, 1, 1)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_20, 6, 0, 1, 1)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setFamilies([u"Ms Shell Dlg 2"])
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_19.setFont(font1)
        self.label_19.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 1, 1, 1)

        self.textEdit_population = QPlainTextEdit(self.widget_4)
        self.textEdit_population.setObjectName(u"textEdit_population")

        self.gridLayout.addWidget(self.textEdit_population, 7, 2, 1, 1)

        self.textEdit_wtCost = QPlainTextEdit(self.widget_4)
        self.textEdit_wtCost.setObjectName(u"textEdit_wtCost")

        self.gridLayout.addWidget(self.textEdit_wtCost, 5, 2, 1, 1)

        self.textEdit_mutation = QPlainTextEdit(self.widget_4)
        self.textEdit_mutation.setObjectName(u"textEdit_mutation")

        self.gridLayout.addWidget(self.textEdit_mutation, 8, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 4, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 5, 1, 1, 1)

        self.comboBox_modelType = QComboBox(self.widget_4)
        self.comboBox_modelType.addItem("")
        self.comboBox_modelType.setObjectName(u"comboBox_modelType")
        self.comboBox_modelType.setMinimumSize(QSize(150, 16))
        self.comboBox_modelType.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_modelType.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox_modelType, 0, 2, 1, 1)

        self.label_31 = QLabel(self.widget_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_31, 5, 0, 1, 1)

        self.textEdit_wtDist = QPlainTextEdit(self.widget_4)
        self.textEdit_wtDist.setObjectName(u"textEdit_wtDist")

        self.gridLayout.addWidget(self.textEdit_wtDist, 4, 2, 1, 1)

        self.label_33 = QLabel(self.widget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_27, 7, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 1, 1, 1)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_28, 8, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 8, 1, 1, 1)

        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setToolTipDuration(10000)

        self.gridLayout.addWidget(self.label_29, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 2, 1, 1, 1)

        self.textEdit_maxShelters = QPlainTextEdit(self.widget_4)
        self.textEdit_maxShelters.setObjectName(u"textEdit_maxShelters")

        self.gridLayout.addWidget(self.textEdit_maxShelters, 3, 2, 1, 1)

        self.textEdit_maxL2Shelters = QPlainTextEdit(self.widget_4)
        self.textEdit_maxL2Shelters.setObjectName(u"textEdit_maxL2Shelters")

        self.gridLayout.addWidget(self.textEdit_maxL2Shelters, 2, 2, 1, 1)

        self.textEdit_areaPerIndiv = QPlainTextEdit(self.widget_4)
        self.textEdit_areaPerIndiv.setObjectName(u"textEdit_areaPerIndiv")

        self.gridLayout.addWidget(self.textEdit_areaPerIndiv, 1, 2, 1, 1)


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
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">MAX LEVEL 2 SHELTERS</span> the maximum number of level 2 shelters that can be constructed or used</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("Dialog", u"MaxLvl2Shelters", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">WEIGHT DISTANCE</span> the shortest distance between the population and the shelters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("Dialog", u"WeightDistance", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">GENERATIONS</span> represents a stage in the genetic algorithm process. Higher generations indicate progress toward finding the best solution.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Generations", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">MODEL</span> select to use which model is appropriate</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Model", None))
        self.comboBox_modelType.setItemText(0, QCoreApplication.translate("Dialog", u"Bilevel No Transfer (BNT)", None))

#if QT_CONFIG(tooltip)
        self.label_31.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">WEIGHT COST</span> the cost of constructing or maintaining shelters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("Dialog", u"WeightCost", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">MAX SHELTERS</span> the maximum number of shelters allowed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("Dialog", u"MaxShelters", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">POPULATION</span> a set of potential solutions that evolves over multiple iterations/generations</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Population", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">MUTATION RATE</span> determines if a community is randomly selected to update shelter allocations based on a random value</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Mutation Rate", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">AREA PER INDIVIDUAL</span> represents the amount of space allocated for each individual in a shelter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Dialog", u"AreaPerIndividual", None))
        self.modelSettings_done_btn.setText(QCoreApplication.translate("Dialog", u"DONE", None))
    # retranslateUi

