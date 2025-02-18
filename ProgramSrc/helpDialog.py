import sys
from PySide6.QtWidgets import QPushButton, QCheckBox, QDialog, QLabel, QMessageBox, QFileDialog, QTableWidgetItem, QWidget, QHBoxLayout, QTextEdit
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QUrl, QThread
from ui_helpDialog import Ui_Dialog
import pandas as pd
import os
from functools import partial

class helpDialog(QDialog):
    def __init__(self):
        super().__init__()  # Initialize the QDialog (or QWidget)
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the current widget (QDialog)
        self.setModal(True)

        self.ui.pushButton_10.clicked.connect(self.open_Dashboardhelp)
        self.ui.pushButton_9.clicked.connect(self.open_commSettingshelp)
        self.ui.pushButton_8.clicked.connect(self.open_shelSettingshelp)
        self.ui.pushButton_7.clicked.connect(self.open_modelSettingshelp)
        self.ui.pushButton_2.clicked.connect(self.open_solveSettingshelp)
        self.ui.pushButton_3.clicked.connect(self.open_AboutUshelp)



    def open_Dashboardhelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(0)

    def open_commSettingshelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(1)

    def open_shelSettingshelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(2)

    def open_modelSettingshelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(3)

    def open_solveSettingshelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(4)

    def open_AboutUshelp(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(5)
