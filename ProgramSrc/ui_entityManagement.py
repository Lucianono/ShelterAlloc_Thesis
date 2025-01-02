# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entityManagement.ui'
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

class Ui_EntityManagementCommunities(object):
    def setupUi(self, EntityManagementCommunities):
        if not EntityManagementCommunities.objectName():
            EntityManagementCommunities.setObjectName(u"EntityManagementCommunities")
        EntityManagementCommunities.resize(1200, 750)
        EntityManagementCommunities.setStyleSheet(u"* {\n"
"background-color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(EntityManagementCommunities)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(EntityManagementCommunities)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mc_back_btn = QPushButton(self.frame)
        self.mc_back_btn.setObjectName(u"mc_back_btn")
        self.mc_back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_back_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ICONS/462547553_520698087383761_137860076397263527_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mc_back_btn.setIcon(icon)
        self.mc_back_btn.setIconSize(QSize(40, 40))
        self.mc_back_btn.setCheckable(True)
        self.mc_back_btn.setChecked(True)

        self.horizontalLayout.addWidget(self.mc_back_btn)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.mc_import_btn = QPushButton(self.frame)
        self.mc_import_btn.setObjectName(u"mc_import_btn")
        self.mc_import_btn.setMinimumSize(QSize(191, 51))
        self.mc_import_btn.setMaximumSize(QSize(161, 51))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.mc_import_btn.setFont(font1)
        self.mc_import_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_import_btn.setStyleSheet(u"QPushButton {\n"
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
"    background-color: #E63946;\n"
"}\n"
"")
        self.mc_import_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.mc_import_btn)

        self.mc_add_community_btn = QPushButton(self.frame)
        self.mc_add_community_btn.setObjectName(u"mc_add_community_btn")
        self.mc_add_community_btn.setMinimumSize(QSize(281, 61))
        self.mc_add_community_btn.setFont(font1)
        self.mc_add_community_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_add_community_btn.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/ICONS/460625174_1063840541791504_8083137884705313080_n.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mc_add_community_btn.setIcon(icon1)
        self.mc_add_community_btn.setIconSize(QSize(35, 35))
        self.mc_add_community_btn.setCheckable(True)
        self.mc_add_community_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.mc_add_community_btn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(EntityManagementCommunities)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.communityInfo_table = QTableWidget(self.frame_2)
        if (self.communityInfo_table.columnCount() < 8):
            self.communityInfo_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.communityInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.communityInfo_table.rowCount() < 1):
            self.communityInfo_table.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.communityInfo_table.setVerticalHeaderItem(0, __qtablewidgetitem8)
        self.communityInfo_table.setObjectName(u"communityInfo_table")
        self.communityInfo_table.setStyleSheet(u"QHeaderView::section {\n"
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
        self.communityInfo_table.setFrameShadow(QFrame.Raised)
        self.communityInfo_table.horizontalHeader().setVisible(True)
        self.communityInfo_table.horizontalHeader().setMinimumSectionSize(100)
        self.communityInfo_table.horizontalHeader().setDefaultSectionSize(120)
        self.communityInfo_table.horizontalHeader().setStretchLastSection(True)
        self.communityInfo_table.verticalHeader().setVisible(True)
        self.communityInfo_table.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_2.addWidget(self.communityInfo_table)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(EntityManagementCommunities)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.mc_cancel_changes_btn = QPushButton(self.frame_3)
        self.mc_cancel_changes_btn.setObjectName(u"mc_cancel_changes_btn")
        self.mc_cancel_changes_btn.setMinimumSize(QSize(161, 51))
        self.mc_cancel_changes_btn.setMaximumSize(QSize(161, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.mc_cancel_changes_btn.setFont(font2)
        self.mc_cancel_changes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_cancel_changes_btn.setStyleSheet(u"QPushButton {\n"
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
        self.mc_cancel_changes_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.mc_cancel_changes_btn)

        self.mc_save_changes_btn = QPushButton(self.frame_3)
        self.mc_save_changes_btn.setObjectName(u"mc_save_changes_btn")
        self.mc_save_changes_btn.setMinimumSize(QSize(161, 51))
        self.mc_save_changes_btn.setMaximumSize(QSize(161, 51))
        self.mc_save_changes_btn.setFont(font2)
        self.mc_save_changes_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mc_save_changes_btn.setStyleSheet(u"QPushButton {\n"
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
        self.mc_save_changes_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.mc_save_changes_btn)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(EntityManagementCommunities)

        self.mc_add_community_btn.setDefault(False)


        QMetaObject.connectSlotsByName(EntityManagementCommunities)
    # setupUi

    def retranslateUi(self, EntityManagementCommunities):
        EntityManagementCommunities.setWindowTitle(QCoreApplication.translate("EntityManagementCommunities", u"Dialog", None))
        self.mc_back_btn.setText("")
        self.label.setText(QCoreApplication.translate("EntityManagementCommunities", u"Manage Communities", None))
        self.mc_import_btn.setText(QCoreApplication.translate("EntityManagementCommunities", u"Import XLSX", None))
        self.mc_add_community_btn.setText(QCoreApplication.translate("EntityManagementCommunities", u"Add Community", None))
        ___qtablewidgetitem = self.communityInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EntityManagementCommunities", u"Name", None));
        ___qtablewidgetitem1 = self.communityInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EntityManagementCommunities", u"xDegrees", None));
        ___qtablewidgetitem2 = self.communityInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EntityManagementCommunities", u"yDegrees", None));
        ___qtablewidgetitem3 = self.communityInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EntityManagementCommunities", u"Population", None));
        ___qtablewidgetitem4 = self.communityInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EntityManagementCommunities", u"AffectedPop", None));
        ___qtablewidgetitem5 = self.communityInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EntityManagementCommunities", u"WorkPop", None));
        ___qtablewidgetitem6 = self.communityInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EntityManagementCommunities", u"MaxDistance", None));
        ___qtablewidgetitem7 = self.communityInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EntityManagementCommunities", u"Remarks", None));
        ___qtablewidgetitem8 = self.communityInfo_table.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EntityManagementCommunities", u"1", None));
        self.mc_cancel_changes_btn.setText(QCoreApplication.translate("EntityManagementCommunities", u"Cancel", None))
        self.mc_save_changes_btn.setText(QCoreApplication.translate("EntityManagementCommunities", u"Save Changes", None))
    # retranslateUi

