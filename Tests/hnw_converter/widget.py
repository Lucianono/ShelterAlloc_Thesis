from typing import Optional
from PyQt6.QtWidgets import QWidget
from ui_widget import Ui_widget
from PyQt6.QtCore import Qt

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Height & Weight Converter")

        self.kilo_lineEdit.textChanged.connect(self.convert_weight)
        self.pound_lineEdit.textChanged.connect(self.convert_weight)
        self.ounce_lineEdit.textChanged.connect(self.convert_weight)

        self.centimeter_lineEdit.textChanged.connect(self.convert_height)
        self.meter_lineEdit.textChanged.connect(self.convert_height)
        self.feet_lineEdit.textChanged.connect(self.convert_height)
    
    def convert_weight(self):
        kilo_text = self.kilo_lineEdit.text()

        if kilo_text == "":
            self.pound_lineEdit.clear()
            self.ounce_lineEdit.clear()
            return
        
        try:
            kg_value = float(self.kilo_lineEdit.text())
            lb_value = kg_value * 2.20462
            oz_value = kg_value * 35.274

            self.pound_lineEdit.setText(f"{lb_value:.2f}")
            self.ounce_lineEdit.setText(f"{oz_value:.2f}")

        except ValueError:
            pass
    
    def convert_height(self):
        centimeter_text = self.centimeter_lineEdit.text()

        if centimeter_text == "":
            self.meter_lineEdit.clear()
            self.feet_lineEdit.clear()
            return
        
        try:
            centimeter_value = float(self.centimeter_lineEdit.text())
            meter_value = centimeter_value / 100
            feet_value = meter_value / 0.3048

            self.meter_lineEdit.setText(f"{meter_value:.2f}")
            self.feet_lineEdit.setText(f"{feet_value:.2f}")

        except ValueError:
            pass

        except ZeroDivisionError:
            pass