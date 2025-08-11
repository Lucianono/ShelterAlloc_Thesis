from PySide6.QtWidgets import QLabel, QMainWindow, QMenu, QDialog, QInputDialog, QFileDialog, QTableWidgetItem, QPlainTextEdit, QFileDialog, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QApplication, QLineEdit
from PySide6.QtGui import QAction, QColor, QIcon, QCursor, QPixmap
from PySide6.QtCore import Qt, QUrl, QTimer, QSize, QRect, QPropertyAnimation, QEvent
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from functools import partial
from ui_dashboard import Ui_MainWindow
from solveSettings import SolveSettingsDialog
from entityManagementComm import EntityManagementComm
from entityManagementShelter import EntityManagementShelter
from helpDialog import helpDialog
from folium.plugins import MousePosition
from optimizedRouting import run_optimization
from shelterAllocationReport import ShelterAllocationReport
import msoffcrypto
import pandas as pd
import os
import sys
import folium
import io
import networkx as nx
import osmnx as ox

class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dashboard")
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.installEventFilter(self)

        self.add_filter_to_existing_text_fields()

        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        
        comm_file = os.path.join(self.save_dir, "commData.xlsx")
        shel_file = os.path.join(self.save_dir, "shelData.xlsx")
        comm_headers = ["Active", "Name", "Latitude", "Longitude", "Population", "AffectedPop", "MaxDistance", "Remarks"]
        shel_headers = ["Active", "Name", "Latitude", "Longitude", "Area1", "Cost1", "Area2", "Cost2", "ResToFlood", "ResToTyphoon", "ResToEarthquake", "Status", "Remarks"]
        self.ensure_excel_file_exists(comm_file, comm_headers)
        self.ensure_excel_file_exists(shel_file, shel_headers)

        self.is_adding_community = False
        self.is_adding_shelter = False

        self.pushButton_14.setCursor(Qt.PointingHandCursor)
        self.pushButton_15.setCursor(Qt.PointingHandCursor)

        self.stackedWidget.hide()
        
        self.add_community_btn.clicked.connect(self.handle_add_community)
        self.add_shelter_btn.clicked.connect(self.handle_add_shelter)


        self.load_comm_data()
        self.load_shel_data()

        self.initial_map_file_path = os.path.join(self.save_dir, "map.html")
        self.webEngineView.setUrl(QUrl.fromLocalFile(self.initial_map_file_path))

        self.file_path = None
        self.advanced_settings_com.clicked.connect(self.open_entitymanagement_dialog)
        self.advanced_settings_shel.clicked.connect(self.open_entitymanagement_shelter_dialog)
        self.solve_btn.clicked.connect(self.open_solve_settings_dialog)

        #change map when this combobox changed
        self.shelterprev_comboBox.currentIndexChanged.connect(self.filter_shelter_map)
        self.marker_comboBox.currentIndexChanged.connect(self.refresh_map)

        self.help_btn.clicked.connect(self.open_help_dialog_page)
        self.reports_btn.clicked.connect(self.open_reports)
        
        # swap checkboxes to switches
        self.switch_1 = self.add_switch(self.checkBox_15)
        self.switch_2 = self.add_switch(self.checkBox_16)

        self.menu = QMenu(self)
        self.show()

        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

            
        self.update_first_column(os.path.join(self.save_dir,"commData.xlsx"))
        self.update_first_column(os.path.join(self.save_dir,"shelData.xlsx")) 



    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            obj.clearFocus()  # Unselect the field
            return True  # Mark event as handled (no new line added)
        return super().eventFilter(obj, event)    


    def update_first_column(self, file_name):
        df = pd.read_excel(file_name, dtype=str)

        if df.empty:
            print(f"{file_name} is empty. Skipping...")
            return
        first_column_name = df.columns[0]

        df[first_column_name] = df[first_column_name].fillna("")

        mask_blank_first_column = df[first_column_name] == ""
        mask_other_columns_filled = df.iloc[:, 1:].notna().any(axis=1)
        rows_to_update = mask_blank_first_column & mask_other_columns_filled
        df.loc[rows_to_update, first_column_name] = "True"

        df[first_column_name] = df[first_column_name].astype(str)

        df.to_excel(file_name, index=False, engine="openpyxl")


    def ensure_excel_file_exists(self, filepath, columns):
        if not os.path.exists(filepath):
            df = pd.DataFrame(columns=columns)
            df.to_excel(filepath, index=False)

    def open_help_dialog_page(self):
        self.help_dialog_window = helpDialog()
        self.help_dialog_window.show()

    def open_entitymanagement_dialog(self):
        self.entityManagementComm_Window = EntityManagementComm()
        self.entityManagementComm_Window.changes_saved.connect(self.load_comm_data)
        self.entityManagementComm_Window.show()

    def open_entitymanagement_shelter_dialog(self):
        self.entityManagementShelter_Window = EntityManagementShelter()
        self.entityManagementShelter_Window.changes_saved.connect(self.load_shel_data)
        self.entityManagementShelter_Window.show()

    def open_solve_settings_dialog(self):
        self.solveSettings_Window = SolveSettingsDialog()
        self.solveSettings_Window.changes_saved_comm.connect(self.load_comm_data)
        self.solveSettings_Window.changes_saved_shel.connect(self.load_shel_data)
        self.solveSettings_Window.show()

    def unhide_stacked_widget(self):
        self.stackedWidget.show()

    def load_comm_data(self):
        layout = self.verticalLayout_18.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Properly delete the widget

        self.data = pd.read_excel(os.path.join(self.save_dir, "commData.xlsx"), header=0)
        self.refresh_map()
        
        try:
            file_path = os.path.join(self.save_dir, "commData.xlsx")
            self.data_Names = pd.read_excel(file_path, usecols=['Name','Active'])

            for row in self.data_Names.itertuples(index=False):
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                if row.Active :
                    icon_path = os.path.join(sys._MEIPASS, "ICONS", "pin-5-128.png")
                else : 
                    icon_path = os.path.join(sys._MEIPASS, "ICONS", "pin-5-128 (2).png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(24, 24)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(24, 24)

                name_label = QLabel(str(row.Name))
                name_label.setMaximumSize(QSize(170, 16777215))

                button_icon_path = os.path.join(sys._MEIPASS, "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(30,30))

                button.setFixedSize(30,30)

                button.setStyleSheet("background: transparent; border: none;")
                button.setCursor(Qt.PointingHandCursor)

                button.setObjectName(f"barangay_{row.Name}_btn")

                button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

                hbox_layout.addWidget(picture_label)
                hbox_layout.addWidget(name_label)
                hbox_layout.addWidget(button)

                container_widget = QWidget()
                container_widget.setLayout(hbox_layout)
                container_widget.setStyleSheet("background: transparent;")

                layout.addWidget(container_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")

    def add_filter_to_existing_text_fields(self):
        for child in self.findChildren(QPlainTextEdit):
            child.installEventFilter(self)
    
    def childEvent(self, event):
        if event.type() == QEvent.ChildAdded:
            child = event.child()
            if isinstance(child, QPlainTextEdit):
                child.installEventFilter(self)
        return super().childEvent(event)
    
    def load_shel_data(self):

        layout = self.verticalLayout_19.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Properly delete the widget

        self.shel_data = pd.read_excel(os.path.join(self.save_dir, "shelData.xlsx"), header=0)
        self.refresh_map()

        try:
            file_path = os.path.join(self.save_dir, "shelData.xlsx")
            self.data_Names = pd.read_excel(file_path, usecols=['Name','Active'])

            for row in self.data_Names.itertuples(index=False):
                hbox_layout = QHBoxLayout()

                picture_label = QLabel()
                if row.Active :
                    icon_path = os.path.join(sys._MEIPASS, "ICONS", "pin-5-128 (1).png")
                else : 
                    icon_path = os.path.join(sys._MEIPASS, "ICONS", "pin-5-128 (2).png")
                pixmap = QPixmap(icon_path)

                pixmap = pixmap.scaled(24, 24)

                picture_label.setPixmap(pixmap)
                picture_label.setFixedSize(24, 24)

                name_label = QLabel(str(row.Name))
                name_label.setMaximumSize(QSize(170, 16777215))

                button_icon_path = os.path.join(sys._MEIPASS, "ICONS", "462544067_1241440546885630_5886192978905579196_n.png")
                button = QPushButton()

                button_icon = QPixmap(button_icon_path)
                button.setIcon(button_icon)
                button.setIconSize(QSize(30,30))

                button.setFixedSize(30,30)

                button.setStyleSheet("background: transparent; border: none;")
                button.setCursor(Qt.PointingHandCursor)

                button.setObjectName(f"shelter_{row.Name}_btn")

                button.clicked.connect(lambda checked, button_name=button.objectName(): self.handle_button_click(button_name))

                hbox_layout.addWidget(picture_label)
                hbox_layout.addWidget(name_label)
                hbox_layout.addWidget(button)

                container_widget = QWidget()
                container_widget.setLayout(hbox_layout)

                layout.addWidget(container_widget)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")


    def eventFilter(self, obj, event):
        if isinstance(obj, QPlainTextEdit) and event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                obj.clearFocus()  # Unselect the field
                return True  # Event handled
        return super().eventFilter(obj, event)

    def handle_button_click(self, button_name):
        value = button_name.split("_")[1]
        
        self.stackedWidget.show()

        if button_name.startswith("barangay_"):
            self.page.show()
            self.page_2.hide()
            self.label_18.setText("Edit Community")
            row = self.data[self.data['Name'] == value].index[0]

            self.switch_1.setChecked(self.data.loc[row, 'Active'])
            self.switch_1.toggle_animation()

            self.plainTextEdit_15.setPlainText(str(self.data.loc[row, 'Name']))

            self.plainTextEdit.setPlainText(str(self.data.loc[row, 'Latitude']))
            self.plainTextEdit_2.setPlainText(str(self.data.loc[row, 'Longitude']))
            self.plainTextEdit_3.setPlainText(str(self.data.loc[row, 'Population']))
            self.plainTextEdit_4.setPlainText(str(self.data.loc[row, 'AffectedPop']))
            self.plainTextEdit_5.setPlainText(str(self.data.loc[row, 'MaxDistance']))
            self.plainTextEdit_6.setPlainText(str(self.data.loc[row, 'Remarks']).replace('nan', ''))

            self.focus_to_marker(self.data.loc[row, 'Latitude'],self.data.loc[row, 'Longitude'])

            #connect button for saving
            self.mc_cancel_changes_btn.show()
            self.mc_save_changes_btn.clicked.disconnect()
            self.mc_cancel_changes_btn.clicked.disconnect()
            self.mc_save_changes_btn.clicked.connect(lambda: self.save_community_data_dashboard(str(self.data.loc[row, 'Name'])))
            self.mc_cancel_changes_btn.clicked.connect(lambda: self.delete_community_data_dashboard(str(self.data.loc[row, 'Name'])))

            self.page.update()
            self.stackedWidget.update()

        elif button_name.startswith("shelter_"):
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.page_2.show()
            self.page.hide()
            row = self.shel_data[self.shel_data['Name'] == value].index[0]

            self.switch_2.setChecked(self.shel_data.loc[row, 'Active'])
            self.switch_2.toggle_animation()

            self.plainTextEdit_9.setPlainText(str(self.shel_data.loc[row, 'Name']))

            self.plainTextEdit_11.setPlainText(str(self.shel_data.loc[row, 'Latitude']))
            self.plainTextEdit_10.setPlainText(str(self.shel_data.loc[row, 'Longitude']))
            self.plainTextEdit_8.setPlainText(str(self.shel_data.loc[row, 'Area1']))
            self.plainTextEdit_12.setPlainText(str(self.shel_data.loc[row, 'Cost1']))
            self.plainTextEdit_13.setPlainText(str(self.shel_data.loc[row, 'Area2']))
            self.plainTextEdit_14.setPlainText(str(self.shel_data.loc[row, 'Cost2']))
            self.checkBox_17.setChecked(bool(self.shel_data.loc[row, 'ResToFlood'])) if pd.notna(self.shel_data.loc[row, 'ResToFlood']) else self.checkBox_17.setChecked(False)
            self.checkBox_19.setChecked(bool(self.shel_data.loc[row, 'ResToTyphoon'])) if pd.notna(self.shel_data.loc[row, 'ResToTyphoon']) else self.checkBox_19.setChecked(False)
            self.checkBox_18.setChecked(bool(self.shel_data.loc[row, 'ResToEarthquake'])) if pd.notna(self.shel_data.loc[row, 'ResToEarthquake']) else self.checkBox_18.setChecked(False)
            status_mapping = {"Built": 0, "Partially Built": 1, "Damaged": 2, "Empty Lot": 3}
            self.status_comboBox_2.setCurrentIndex(status_mapping.get(str(self.shel_data.loc[row, 'Status']), -1))
            self.plainTextEdit_17.setPlainText(str(self.shel_data.loc[row, 'Remarks']).replace('nan', ''))

            self.focus_to_marker(self.shel_data.loc[row, 'Latitude'],self.shel_data.loc[row, 'Longitude'])

            #connect button for saving
            self.mc_cancel_changes_btn_2.show()
            self.mc_save_changes_btn_2.clicked.disconnect()
            self.mc_cancel_changes_btn_2.clicked.disconnect()
            self.mc_save_changes_btn_2.clicked.connect(lambda: self.save_shelter_data_dashboard(str(self.shel_data.loc[row, 'Name'])))
            self.mc_cancel_changes_btn_2.clicked.connect(lambda: self.delete_shelter_data_dashboard(str(self.shel_data.loc[row, 'Name'])))
            
            self.page_2.update()
            self.stackedWidget.update()

    def handle_add_community(self):
        self.open_add_community_page()

    def handle_add_shelter(self):
        self.open_add_shelter_page()

    def open_add_community_page(self):
        self.label_18.setText("New Community")

        self.mc_cancel_changes_btn.hide()

        self.switch_1.setChecked(True)
        self.switch_1.toggle_animation()

        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()
        self.plainTextEdit_5.clear()
        self.plainTextEdit_6.clear()
        self.plainTextEdit_15.clear()

        self.mc_save_changes_btn.clicked.disconnect()
        self.mc_save_changes_btn.clicked.connect(lambda: self.save_community_data_dashboard("c0mmN3wc0d3"))
       

        self.stackedWidget.setCurrentWidget(self.page)
        self.stackedWidget.show()

    def open_add_shelter_page(self):
        self.label_31.setText("New Shelter")

        self.mc_cancel_changes_btn_2.hide()

        self.switch_2.setChecked(True)
        self.switch_2.toggle_animation()

        self.plainTextEdit_9.clear()
        self.plainTextEdit_11.clear()
        self.plainTextEdit_10.clear()
        self.plainTextEdit_8.clear()
        self.plainTextEdit_12.clear()
        self.plainTextEdit_13.clear()
        self.plainTextEdit_14.clear()
        self.plainTextEdit_17.clear()
        self.checkBox_17.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_19.setChecked(False)
        self.status_comboBox_2.setCurrentIndex(0)

        self.mc_save_changes_btn_2.clicked.disconnect()
        self.mc_save_changes_btn_2.clicked.connect(lambda: self.save_shelter_data_dashboard("sh31N3wc0d3"))
       

        self.stackedWidget.setCurrentWidget(self.page_2)
        self.stackedWidget.show()

      
    def refresh_map(self):
        try:
            comm_data = pd.read_excel( os.path.join(self.save_dir,"commData.xlsx"),usecols=['Name','Latitude','Longitude','Active'])
            shel_data = pd.read_excel( os.path.join(self.save_dir,"shelData.xlsx"),usecols=['Name','Latitude','Longitude','Active'])

            show_inactive_marker = self.marker_comboBox.currentIndex() == 0

            if not comm_data.empty:
                avg_lat = comm_data['Latitude'].mean()
                avg_lon = comm_data['Longitude'].mean()
                self.map = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)
            elif not shel_data.empty:
                avg_lat = shel_data['Latitude'].mean()
                avg_lon = shel_data['Longitude'].mean()
                self.map = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)
            else:
                self.map = folium.Map(location=[0,0], zoom_start=2)

            MousePosition(
                position='bottomright',
                separator=' | ',
                prefix="Coordinates: ",
                empty_string='Unavailable',
                num_digits=6
            ).add_to(self.map)

            for index, row in comm_data.iterrows():
                latitude = row.get("Latitude", 1)
                longitude = row.get("Longitude", 1)
                name = row.get("Name", "Unknown")

                if row.get("Active") :
                    color="green"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)

                elif show_inactive_marker :
                    color="lightgray"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)

                

            for index, row in shel_data.iterrows():
                latitude = row.get("Latitude", 1)
                longitude = row.get("Longitude", 1)
                name = row.get("Name", "Unknown")

                if row.get("Active") :
                    color="blue"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)
                    
                elif show_inactive_marker :
                    color="lightgray"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)

            map_file_path = os.path.join(self.save_dir, "map.html")
            self.map.save(map_file_path)

            self.webEngineView.setUrl(QUrl.fromLocalFile(map_file_path))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update map: {e}")

    def focus_to_marker(self,xDeg,yDeg):
        try:
            focused_map = folium.Map(location=[xDeg, yDeg], zoom_start=16)

            # Re-add all existing markers from the current map to the focused map
            for child in self.map._children.values():
                focused_map.add_child(child)

            self.map = focused_map
            map_file_path = os.path.join(self.save_dir, "map.html")
            self.map.save(map_file_path)

            self.webEngineView.setUrl(QUrl.fromLocalFile(map_file_path))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to focus on marker: {e}")

    def add_switch(self, checkbox, is_active=False):
        # Get the layout of the parent widget
        layout = checkbox.parentWidget().layout()

        # Create the switch container widget
        switch_widget = QWidget()
        switch_layout = QHBoxLayout(switch_widget)
        switch_layout.setAlignment(Qt.AlignCenter)
        switch_layout.setContentsMargins(0, 0, 0, 0)


        # Create the switch
        switch = QPushButton()
        switch.setCheckable(True)
        switch.setChecked(is_active)
        switch.setFixedSize(38, 18)  # Set the switch size
        switch.setStyleSheet(
            "QPushButton { background-color: #4CAF50; border-radius: 8px; }" 
            if switch.isChecked() else 
            "QPushButton { background-color: #ccc; border-radius: 8px; }"
        )
        
        # Set an object name for the switch
        switch.setObjectName(checkbox.objectName().replace("checkBox", "switch"))

        # Create a circle (knob) for the switch
        knob = QPushButton(switch)
        knob.setFixedSize(14, 14)
        knob.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 7px;
            }
        """)
        knob.move(22 if is_active else 2, 2)  # Initial position for the knob (left side)
        switch.knob = knob

        # Animation for toggling
        animation = QPropertyAnimation(knob, b"geometry")
        animation.setDuration(200)

        # Connect the toggle functionality
        switch.clicked.connect(lambda: toggle_switch_animation())

        # Delegate knob clicks to the switch
        def knob_mouse_press(event):
            switch.click()  # Simulate a click on the switch
            super(knob.__class__, knob).mousePressEvent(event)

        knob.mousePressEvent = knob_mouse_press

        def toggle_switch_animation():
            if switch.isChecked():
                # Move knob to the right
                animation.setStartValue(QRect(2, 2, 16, 16))
                animation.setEndValue(QRect(22, 2, 16, 16))
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        border-radius: 8px;
                    }
                """)
            else:
                # Move knob to the left
                animation.setStartValue(QRect(22, 2, 16, 16))
                animation.setEndValue(QRect(2, 2, 16, 16))  # Reset to left side
                switch.setStyleSheet("""
                    QPushButton {
                        background-color: #ccc;
                        border-radius: 8px;
                    }
                """)
            animation.start()

        # Add the switch to the layout
        switch_layout.addWidget(switch)
        layout.replaceWidget(checkbox, switch_widget)  # Replace the checkbox with the switch
        checkbox.deleteLater()  # Remove the old checkbox
        switch.toggle_animation = toggle_switch_animation

        return switch

    # Validate the data
    def validate_input_data(self, old_name, data, expected_types):
        if data['Name'] in self.data['Name'].values and data['Name'] != old_name:
            raise ValueError(f"Duplicate entry found for 'Name': {data['Name']}.")

        for key, expected_type in expected_types.items():
            value = data.get(key)
            if value is None:
                raise ValueError(f"Missing value for {key}.")
            
            if (pd.isnull(value) or value == '') and key != "Remarks":
                raise ValueError(f"Missing value for {key}.")
            
            try:
                # Attempt type conversion
                if expected_type == int:
                    int(value)
                elif expected_type == float:
                    float(value)
                elif expected_type == str:
                    str(value)
            except ValueError:
                raise ValueError(f"Invalid type for {key}. Expected {expected_type.__name__}, got {type(value).__name__}.")
            
        # check if area2 >= area1
        if "Area1" in expected_types:
            shelter = data
            if float(shelter["Area2"]) < float(shelter["Area1"]):
                raise ValueError(f"{shelter["Name"]}: area2 should be greater than or equal to area1.")

    def save_community_data_dashboard(self, old_data_name):
                
        data_active = self.switch_1.isChecked()
        data_name = self.plainTextEdit_15.toPlainText().strip()
        data_Latitude = self.plainTextEdit.toPlainText().strip()
        data_Longitude = self.plainTextEdit_2.toPlainText().strip()
        data_population = self.plainTextEdit_3.toPlainText().strip()
        data_affectedPop = self.plainTextEdit_4.toPlainText().strip()
        data_maxDistance = self.plainTextEdit_5.toPlainText().strip()
        data_remarks = self.plainTextEdit_6.toPlainText().strip()

        # Validate the input
        new_row = {
            "Active": data_active,
            "Name": data_name,
            "Latitude": data_Latitude,
            "Longitude": data_Longitude,
            "Population": data_population,
            "AffectedPop": data_affectedPop,
            "MaxDistance": data_maxDistance,
            "Remarks": data_remarks,
        }
        expected_types = {
            'Name': str,
            'Latitude': float,
            'Longitude': float,
            'Population': int,
            'AffectedPop': int,
            'MaxDistance': float,
            'Remarks': str
        }
        try:
            self.validate_input_data(old_data_name, new_row, expected_types)
            print("All data is valid.")
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"{e}")
            return
        

        if (old_data_name == "c0mmN3wc0d3") :
            new_row = pd.DataFrame([new_row])
            self.data = pd.concat([self.data, new_row], ignore_index=True) 
        else :
            row_idx = self.data.loc[self.data["Name"] == old_data_name].index[0]
            self.data.loc[row_idx, "Active"] = data_active
            self.data.loc[row_idx, "Name"] = data_name
            self.data.loc[row_idx, "Latitude"] = float(data_Latitude)
            self.data.loc[row_idx, "Longitude"] = float(data_Longitude)
            self.data.loc[row_idx, "Population"] = int(data_population)
            self.data.loc[row_idx, "AffectedPop"] = int(data_affectedPop)
            self.data.loc[row_idx, "MaxDistance"] = float(data_maxDistance)
            self.data.loc[row_idx, "Remarks"] = data_remarks

        # Save the updated DataFrame back to the Excel file
        file_path = os.path.join(self.save_dir, "commData.xlsx")
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            self.data.to_excel(writer, index=False)

        self.load_comm_data()

    def save_shelter_data_dashboard(self, old_data_name):
        data_active = self.switch_2.isChecked()
        data_name = self.plainTextEdit_9.toPlainText().strip()
        data_Latitude = self.plainTextEdit_11.toPlainText().strip()
        data_Longitude = self.plainTextEdit_10.toPlainText().strip()
        data_area1 = self.plainTextEdit_8.toPlainText().strip()
        data_cost1 = self.plainTextEdit_12.toPlainText().strip()
        data_area2 = self.plainTextEdit_13.toPlainText().strip()
        data_cost2 = self.plainTextEdit_14.toPlainText().strip()
        data_resFlood = self.checkBox_17.isChecked()
        data_resTyphoon = self.checkBox_19.isChecked()
        data_resEarthquake = self.checkBox_18.isChecked()
        status_mapping = ["Built", "Partially Built", "Damaged", "Empty Lot"]
        data_status = status_mapping[self.status_comboBox_2.currentIndex()]
        data_remarks = self.plainTextEdit_17.toPlainText().strip()

        # Validate the input
        new_row = {
            "Active": data_active,
            "Name": data_name,
            "Latitude": data_Latitude,
            "Longitude": data_Longitude,
            'Area1': data_area1,
            'Cost1': data_cost1,
            'Area2': data_area2,
            'Cost2': data_cost2,
            'ResToFlood': data_resFlood,
            'ResToTyphoon': data_resTyphoon,
            'ResToEarthquake': data_resEarthquake,
            'Status': data_status,
            "Remarks": data_remarks,
        }
        expected_types = {
            'Name': str,
            'Latitude': float,
            'Longitude': float,
            'Area1': float,
            'Cost1': float,
            'Area2': float,
            'Cost2': float,
            'ResToFlood': bool,
            'ResToTyphoon': bool,
            'ResToEarthquake': bool,
            'Status': str,
            'Remarks': str
        }
        try:
            self.validate_input_data(old_data_name, new_row, expected_types)
            print("All data is valid.")
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"{e}")
            return
        
        if (old_data_name == "sh31N3wc0d3") :
            new_row = pd.DataFrame([new_row])
            self.shel_data = pd.concat([self.shel_data, new_row], ignore_index=True) 
        else :
            row_idx = self.shel_data.loc[self.shel_data["Name"] == old_data_name].index[0]
            self.shel_data.loc[row_idx, "Active"] = data_active
            self.shel_data.loc[row_idx, "Name"] = data_name
            self.shel_data.loc[row_idx, "Latitude"] = float(data_Latitude)
            self.shel_data.loc[row_idx, "Longitude"] = float(data_Longitude)
            self.shel_data.loc[row_idx, "Area1"] = float(data_area1)
            self.shel_data.loc[row_idx, "Cost1"] = float(data_cost1)
            self.shel_data.loc[row_idx, "Area2"] = float(data_area2)
            self.shel_data.loc[row_idx, "Cost2"] = float(data_cost2)
            self.shel_data.loc[row_idx, "ResToFlood"] = data_resFlood
            self.shel_data.loc[row_idx, "ResToTyphoon"] = data_resTyphoon
            self.shel_data.loc[row_idx, "ResToEarthquake"] = data_resEarthquake
            self.shel_data.loc[row_idx, "Status"] = data_status
            self.shel_data.loc[row_idx, "Remarks"] = data_remarks

        # Save the updated DataFrame back to the Excel file
        file_path = os.path.join(self.save_dir, "shelData.xlsx")
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            self.shel_data.to_excel(writer, index=False)

        self.load_shel_data()

    def delete_community_data_dashboard(self, old_data_name):
        
        response = QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this item?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            row_idx = self.data.loc[self.data["Name"] == old_data_name].index[0]
            self.data = self.data.drop(index = row_idx)
            
            # Save the updated DataFrame back to the Excel file
            file_path = os.path.join(self.save_dir, "commData.xlsx")
            with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
                self.data.to_excel(writer, index=False)

            self.stackedWidget.hide()
            self.load_comm_data()

    def delete_shelter_data_dashboard(self, old_data_name):

        response = QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this item?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:

            row_idx = self.shel_data.loc[self.shel_data["Name"] == old_data_name].index[0]
            self.shel_data = self.shel_data.drop(index = row_idx)
            
            # Save the updated DataFrame back to the Excel file
            file_path = os.path.join(self.save_dir, "shelData.xlsx")
            with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
                self.shel_data.to_excel(writer, index=False)

            self.stackedWidget.hide()
            self.load_shel_data()

    def filter_shelter_map(self, index):
            file_path= os.path.join(self.save_dir,"shelData.xlsx")

            data = pd.read_excel(file_path)
            if index == 0:
                self.refresh_map()
                return
            elif index > 1 and index <= 5:
                status_mapping = ["Built", "Partially Built", "Damaged", "Empty Lot"]
                data_status = status_mapping[index-2]
                data = data[data["Status"] == data_status]
            elif index > 5 and index <= 8:
                status_mapping = ["ResToFlood", "ResToTyphoon", "ResToEarthquake"]
                data_status = status_mapping[index-6]
                data = data[data[data_status] == True]


            # Reflect filtered data in the UI
            self.preview_map(data)
   
    def preview_map(self,data):
        try:

            show_inactive_marker = self.marker_comboBox.currentIndex() == 0

            if not data.empty:
                avg_lat = data['Latitude'].mean()
                avg_lon = data['Longitude'].mean()
                self.map = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)
            else:
                self.map = folium.Map(location=[0,0], zoom_start=2)


            for index, row in data.iterrows():
                latitude = row.get("Latitude", 1)
                longitude = row.get("Longitude", 1)
                name = row.get("Name", "Unknown")

                if row.get("Active") :
                    color="blue"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)

                elif show_inactive_marker :
                    
                    color="lightgray"
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=name,
                        icon=folium.Icon(color=color)
                    ).add_to(self.map)

            map_file_path = os.path.join(self.save_dir, "map.html")
            self.map.save(map_file_path)

            self.webEngineView.setUrl(QUrl.fromLocalFile(map_file_path))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update map: {e}")

    def open_reports(self):
        try:

    
            file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xls *.xlsx)")
            if file_path:
                decrypted = io.BytesIO()

                # Try opening the file
                with open(file_path, "rb") as f:
                    office_file = msoffcrypto.OfficeFile(f)
                    
                    if office_file.is_encrypted():  # Check if password is required
                        password, ok = QInputDialog.getText(self, "Password Required", "Enter password:", QLineEdit.Password)
                        if not ok or not password:
                            QMessageBox.warning(self, "Error", "No password entered.")
                            return
                        
                        try:
                            office_file.load_key(password=password)
                            office_file.decrypt(decrypted)
                            decrypted.seek(0)
                        except Exception as e:
                            QMessageBox.warning(self, "Error", f"Invalid password: {str(e)}")
                            return
                        
                    else:
                        decrypted = file_path


            #allocation_results.xlsx
            data = pd.read_excel(decrypted,sheet_name="Shelter Location-Allocation", usecols = ["Community","Allocated Population","Shelter Assigned","Level"], header=3).fillna("")
            output_file = os.path.join(self.save_dir, "allocation_results.xlsx")
            data.to_excel(output_file, index=False)

            #modelCommData.xlsx
            data = pd.read_excel(decrypted,sheet_name="Community Data", header=0).fillna("")
            output_file = os.path.join(self.save_dir, "modelCommData.xlsx")
            data.to_excel(output_file, index=False)

            #modelShelData.xlsx
            data = pd.read_excel(decrypted,sheet_name="Shelter Data", header=0).fillna("")
            output_file = os.path.join(self.save_dir, "modelShelData.xlsx")
            data.to_excel(output_file, index=False)

            #modelPerformanceResult.txt
            data = pd.read_excel(decrypted,sheet_name="Report Analysis", header=1).fillna("")
            output_file = os.path.join(self.save_dir, "modelPerformanceResult.txt")
            data.to_csv(output_file, index=False, sep='\t')

            #optimized-routes-map.html
            run_optimization()

            self.report_Window = ShelterAllocationReport(False)
            self.report_Window.show()



        except Exception as e :
            QMessageBox.critical(self, "Error", f"Failed to open file: {e}")
