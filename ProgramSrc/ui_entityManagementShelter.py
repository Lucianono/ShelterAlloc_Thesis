# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entityManagementShelter.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_entityManagementShelter(object):
    def setupUi(self, entityManagementShelter):
        if not entityManagementShelter.objectName():
            entityManagementShelter.setObjectName(u"entityManagementShelter")
        entityManagementShelter.resize(1200, 724)
        entityManagementShelter.setStyleSheet(u"* {\n"
"background-color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(entityManagementShelter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(entityManagementShelter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ms_back_btn = QPushButton(self.frame)
        self.ms_back_btn.setObjectName(u"ms_back_btn")
        self.ms_back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_back_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ms_back_btn.setIcon(icon)
        self.ms_back_btn.setIconSize(QSize(40, 40))
        self.ms_back_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.ms_back_btn)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ms_export_btn = QPushButton(self.frame)
        self.ms_export_btn.setObjectName(u"ms_export_btn")
        self.ms_export_btn.setMinimumSize(QSize(191, 51))
        self.ms_export_btn.setMaximumSize(QSize(161, 51))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.ms_export_btn.setFont(font1)
        self.ms_export_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_export_btn.setToolTipDuration(10000)
        self.ms_export_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #136ec2;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #167bda;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #167bda;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ICONS/icons8-xls-export-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ms_export_btn.setIcon(icon1)
        self.ms_export_btn.setIconSize(QSize(35, 35))
        self.ms_export_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.ms_export_btn)

        self.ms_import_btn = QPushButton(self.frame)
        self.ms_import_btn.setObjectName(u"ms_import_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ms_import_btn.sizePolicy().hasHeightForWidth())
        self.ms_import_btn.setSizePolicy(sizePolicy)
        self.ms_import_btn.setMinimumSize(QSize(191, 51))
        self.ms_import_btn.setMaximumSize(QSize(191, 51))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.ms_import_btn.setFont(font2)
        self.ms_import_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_import_btn.setToolTipDuration(10000)
        self.ms_import_btn.setStyleSheet(u"QPushButton {\n"
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
"    background-color: #12c753;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ICONS/icons8-xls-import-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ms_import_btn.setIcon(icon2)
        self.ms_import_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.ms_import_btn)

        self.ms_add_shelter_btn = QPushButton(self.frame)
        self.ms_add_shelter_btn.setObjectName(u"ms_add_shelter_btn")
        self.ms_add_shelter_btn.setMinimumSize(QSize(281, 61))
        self.ms_add_shelter_btn.setFont(font2)
        self.ms_add_shelter_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_add_shelter_btn.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/ICONS/460625174_1063840541791504_8083137884705313080_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ms_add_shelter_btn.setIcon(icon3)
        self.ms_add_shelter_btn.setIconSize(QSize(35, 35))
        self.ms_add_shelter_btn.setCheckable(True)
        self.ms_add_shelter_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.ms_add_shelter_btn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(entityManagementShelter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.shelterInfo_table = QTableWidget(self.frame_2)
        if (self.shelterInfo_table.columnCount() < 12):
            self.shelterInfo_table.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.shelterInfo_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.shelterInfo_table.rowCount() < 1):
            self.shelterInfo_table.setRowCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.shelterInfo_table.setVerticalHeaderItem(0, __qtablewidgetitem12)
        self.shelterInfo_table.setObjectName(u"shelterInfo_table")
        self.shelterInfo_table.setStyleSheet(u"QHeaderView::section {\n"
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
"	background-color: white;\n"
"    padding: 5px;\n"
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
        self.shelterInfo_table.setFrameShadow(QFrame.Raised)
        self.shelterInfo_table.horizontalHeader().setMinimumSectionSize(100)
        self.shelterInfo_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.shelterInfo_table.horizontalHeader().setStretchLastSection(True)
        self.shelterInfo_table.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_2.addWidget(self.shelterInfo_table)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(entityManagementShelter)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setKerning(True)
        self.label_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.ms_cancel_btn = QPushButton(self.frame_3)
        self.ms_cancel_btn.setObjectName(u"ms_cancel_btn")
        self.ms_cancel_btn.setMinimumSize(QSize(161, 51))
        self.ms_cancel_btn.setMaximumSize(QSize(161, 51))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.ms_cancel_btn.setFont(font4)
        self.ms_cancel_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_cancel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff;\n"
"    color: #FF3B30;\n"
"    padding: 5px;\n"
"    border: 3px solid #FF3B30 ;\n"
"    border-radius: 15px;\n"
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

        self.horizontalLayout_3.addWidget(self.ms_cancel_btn)

        self.ms_save_changes_btn = QPushButton(self.frame_3)
        self.ms_save_changes_btn.setObjectName(u"ms_save_changes_btn")
        self.ms_save_changes_btn.setMinimumSize(QSize(161, 51))
        self.ms_save_changes_btn.setMaximumSize(QSize(161, 51))
        self.ms_save_changes_btn.setFont(font4)
        self.ms_save_changes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ms_save_changes_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.ms_save_changes_btn)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(entityManagementShelter)

        self.ms_add_shelter_btn.setDefault(False)


        QMetaObject.connectSlotsByName(entityManagementShelter)
    # setupUi

    def retranslateUi(self, entityManagementShelter):
        entityManagementShelter.setWindowTitle(QCoreApplication.translate("entityManagementShelter", u"Dialog", None))
        self.ms_back_btn.setText("")
        self.label.setText(QCoreApplication.translate("entityManagementShelter", u"Manage Shelters", None))
#if QT_CONFIG(tooltip)
        self.ms_export_btn.setToolTip(QCoreApplication.translate("entityManagementShelter", u"<html><head/><body><p><span style=\" font-weight:600;\">DOWNLOAD TEMPLATE </span>download an excel file containing the sample shelter data (template)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ms_export_btn.setText(QCoreApplication.translate("entityManagementShelter", u"Download\n"
"Template", None))
#if QT_CONFIG(tooltip)
        self.ms_import_btn.setToolTip(QCoreApplication.translate("entityManagementShelter", u"<html><head/><body><p><span style=\" font-weight:600;\">IMPORT</span> upload an excel file and display its contents in the table</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ms_import_btn.setText(QCoreApplication.translate("entityManagementShelter", u"Import", None))
        self.ms_add_shelter_btn.setText(QCoreApplication.translate("entityManagementShelter", u"Add Shelter", None))
        ___qtablewidgetitem = self.shelterInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("entityManagementShelter", u"Name", None));
        ___qtablewidgetitem1 = self.shelterInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("entityManagementShelter", u"Latitude", None));
        ___qtablewidgetitem2 = self.shelterInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("entityManagementShelter", u"Longitude", None));
        ___qtablewidgetitem3 = self.shelterInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("entityManagementShelter", u"Area1", None));
        ___qtablewidgetitem4 = self.shelterInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("entityManagementShelter", u"Cost1", None));
        ___qtablewidgetitem5 = self.shelterInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("entityManagementShelter", u"Area2", None));
        ___qtablewidgetitem6 = self.shelterInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("entityManagementShelter", u"Cost2", None));
        ___qtablewidgetitem7 = self.shelterInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("entityManagementShelter", u"ResToFlood", None));
        ___qtablewidgetitem8 = self.shelterInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("entityManagementShelter", u"ResToTyphoon", None));
        ___qtablewidgetitem9 = self.shelterInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("entityManagementShelter", u"ResToEarthquake", None));
        ___qtablewidgetitem10 = self.shelterInfo_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("entityManagementShelter", u"Status", None));
        ___qtablewidgetitem11 = self.shelterInfo_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("entityManagementShelter", u"Actions", None));
        ___qtablewidgetitem12 = self.shelterInfo_table.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("entityManagementShelter", u"1", None));
        self.label_2.setText(QCoreApplication.translate("entityManagementShelter", u"Ctrl+D : Enable/Disable All", None))
        self.ms_cancel_btn.setText(QCoreApplication.translate("entityManagementShelter", u"Cancel", None))
        self.ms_save_changes_btn.setText(QCoreApplication.translate("entityManagementShelter", u"Save Changes", None))
    # retranslateUi

