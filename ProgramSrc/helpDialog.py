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
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS", "logo.png")))

        self.ui.pushButton_10.clicked.connect(self.open_Dashboardhelp)
        self.ui.pushButton_9.clicked.connect(self.open_commSettingshelp)
        self.ui.pushButton_8.clicked.connect(self.open_shelSettingshelp)
        self.ui.pushButton_7.clicked.connect(self.open_modelSettingshelp)
        self.ui.pushButton_2.clicked.connect(self.open_solveSettingshelp)
        self.ui.pushButton_3.clicked.connect(self.open_AboutUshelp)

        # Create the HTML content
        html_content1 = f"""
            <html>
                <body>
                    <img src="{sys._MEIPASS.replace('\\', '/')}/tutorial/dashboard.png" width="500">
                    <p>The front page of the system showcases the dashboard. Several parts include the map, the community/shelter browser, community/shelter information, and the legend.
                    You may select advanced settings for communities and shelters for more options in editing information. As well, You can create new communities and shelters from this page.
                    To continue pathfinding, you may press the generate button.</p>
                </body>
            </html>
        """

        # Set the HTML content in QTextBrowser
        self.ui.textBrowser.setHtml(html_content1)

        html_content2 = f"""
            <html>
                <body>
                    <img src="{sys._MEIPASS.replace('\\', '/')}/tutorial/commadvanced.png" width="500">
                    <p>The advanced settings for communities, here there are more options to create and edit your communities, you may also import an excel file of the summary of communities
                    , and also download a template to manually create a list of communities, should you prefer.</p>
                </body>
            </html>
        """

        self.ui.textBrowser_2.setHtml(html_content2)

        html_content3 = f"""
            <html>
                <body>
                    <img src="{sys._MEIPASS.replace('\\', '/')}/tutorial/sheladvanced.png" width="500">
                    <p>The advanced settings for shelters, here there are more options to create and edit your shelters, you may also import an excel file of the summary of shelters
                    , and also download a template to manually create a list of shelters, should you prefer.</p>
                </body>
            </html>
        """

        self.ui.textBrowser_3.setHtml(html_content3)

        html_content4 = f"""
            <html>
                <body>
                    <img src="{sys._MEIPASS.replace('\\', '/')}/tutorial/modelsettings.png" width="500">
                    <p>Do note that we recommend the data in this page be set to default, take caution in manipulating this data. In this page you may edit the parameters of the model
                    used. Variables include area per individual, maximum number of level 1 and 2 shelters, the weights for distance and cost, number of generations, population, and mutation rate.
                    Most of these variables require a value higher than 0, and the weights must total to exactly 1.</p>
                </body>
            </html>
        """

        self.ui.textBrowser_4.setHtml(html_content4)

        html_content5 = f"""
            <html>
                <body>
                    <img src="{sys._MEIPASS.replace('\\', '/')}/tutorial/solvesettings.png" width="500">
                    <p>The next step in pathfinding, in this page you may check the summary of what will be solved, and you may sort the shelters by whether they are resistant to
                    floods, typhoons, or earthquakes, and if they are built, partially built, damaged, or empty. Press solve for the next step in pathfinding and to get your report!</p>
                </body>
            </html>
        """

        self.ui.textBrowser_5.setHtml(html_content5)

        html_content6 = f"""
            <html>
                <body>
                    
                    <p>This project was created to fulfill our requirements for our Thesis, we would like to thank the following people for their help and support!
                    <br> Sir Harris Dela Cruz - our Thesis professor
                    <br> Ma'am Valentine Blez Lampayan - our Thesis adviser
                    <br> We would also like to thank the local government of Calumpit for cooperating with our project and providing us with the necessary data!
                    <br> <br> We are MatTresist, and thank you for using our system.
                    <br> Bryan Jett T. Calulo, Lovely Angeline OL. Cunanan, and Elijah Inigo C. Fabian.</p>
                </body>
            </html>
        """

        self.ui.textBrowser_6.setHtml(html_content6)



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

        
