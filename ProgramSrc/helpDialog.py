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

        self.ui.pushButton_11.clicked.connect(self.open_QuickStart)
        self.ui.pushButton_10.clicked.connect(self.open_Dashboardhelp)
        self.ui.pushButton_9.clicked.connect(self.open_commSettingshelp)
        self.ui.pushButton_8.clicked.connect(self.open_shelSettingshelp)
        self.ui.pushButton_7.clicked.connect(self.open_modelSettingshelp)
        self.ui.pushButton_2.clicked.connect(self.open_solveSettingshelp)
        self.ui.pushButton_3.clicked.connect(self.open_AboutUshelp)
        self.setAttribute(Qt.WA_DeleteOnClose)

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
                <head>
                    <style>
                    body {{
                        text-align: center;
                    }}
                    </style>
                </head>
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
                <head>
                    <style>
                        body {{
                            text-align: center;
                        }}
                    </style>
                </head>
                <body>
                    <p>
                        This project was developed as part of our thesis requirements.  
                        We would like to express our sincere gratitude to the following individuals for their guidance and support:
                    </p>
                    <p>
                        <strong>Sir Harris Dela Cruz</strong> – Thesis Professor <br>
                        <strong>Ma’am Valentine Blez Lampayan</strong> – Thesis Adviser
                    </p>
                    <p>
                        We also extend our appreciation to the local government of Calumpit for their cooperation and for providing the necessary data for our research.
                    </p>
                    <p>
                        We are <strong>MatTresist</strong>. Thank you for using our system!
                    </p>
                    <p>
                        <strong>Bryan Jett T. Calulo, Lovely Angeline OL. Cunanan, and Elijah Inigo C. Fabian</strong>
                    </p>
                    <p>
                        View our project on Github:
                        <a href="https://github.com/Lucianono/ShelterAlloc_Thesis" style="color: blue; text-decoration: underline;">GitHub</a>
                    </p>
                </body>
            </html>
        """

        self.ui.textBrowser_6.setHtml(html_content6)

        html_content8 = f"""
            <h1>Welcome to the Shelter Location Allocation System Tutorial!</h1>
            <p><a href="https://youtu.be/BUyhHiJbwH4?si=16bq5MQWpAKgOIRr" style="color: blue; text-decoration: underline;">Youtube Tutorial</a></p>
            <p>Here’s a quick guide to get you started:</p>

            <h2>Launch the System</h2>
            <ul>
                <li>Once the app is downloaded, launch it by double-clicking it.</li>
                <li>Ensure your internet connection is active.</li>
            </ul>

            <h2>Disable Antivirus (if needed)</h2>
            <ul>
                <li>If your computer detects the system as a virus, temporarily disable your antivirus to avoid any interruptions.</li>
            </ul>

            <h2>Dashboard Overview</h2>
            <ul>
                <li>Upon opening the system, you'll be greeted with the dashboard of the app.</li>
                <li>On the left side, you'll see options for your communities and shelters.</li>
                <li>Since there are no data yet, we will import them.</li>
            </ul>

            <h2>Import Communities</h2>
            <ul>
                <li>Click on <strong>Advanced Settings</strong>.</li>
                <li>Select <strong>Import</strong>.</li>
                <li>Choose your Excel file containing community data.</li>
                <li>Click <strong>Save Changes</strong> once done.</li>
            </ul>

            <h2>Import Shelters</h2>
            <ul>
                <li>Follow the same steps to import your shelter data by going to <strong>Shelter Settings</strong>.</li>
                <li>You may also directly add communities and shelters by clicking the <strong>Add</strong> buttons.</li>
            </ul>

            <h2>Generate Optimal Shelter Location Allocation</h2>
            <ul>
                <li>Click on <strong>Generate</strong>.</li>
                <li>Select which shelters to use for the allocation process.</li>
                <li>Adjust the model settings as needed.</li>
            </ul>

            <h2>Configure Parameters</h2>
            <ul>
                <li>After configuring the settings to your preferences, click <strong>Solve</strong> to initiate the simulation.</li>
            </ul>

            <h2>Wait for the Simulation to Finish</h2>
            <ul>
                <li>The system will calculate the optimal shelter allocation.</li>
                <li>Once finished, a report dialog will pop up.</li>
            </ul>

            <h2>View and Save the Report</h2>
            <ul>
                <li>You can save the report for later use.</li>
                <li>You can also set a password to protect it.</li>
                <li><strong>Optional:</strong> If you think your communities need more resources (e.g. capacity and distance), modify the settings and retry.</li>
            </ul>

            <p><strong>That’s it!</strong> You're all set to use the Shelter Location Allocation System.</p>
        """

        self.ui.textBrowser_8.setHtml(html_content8)



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

    def open_QuickStart(self):
        self.ui.stackedWidget.show()
        self.ui.stackedWidget.setCurrentIndex(6)

        
