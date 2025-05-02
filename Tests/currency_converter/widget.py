from typing import Optional
from PyQt6.QtWidgets import QWidget
from ui_widget import Ui_widget
from PyQt6.QtCore import Qt

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Currency Converter")

        self.convert_button.clicked.connect(self.convert_currency)

    def convert_currency(self):
        try:
            amount = float(self.amount_lineEdit.text())
            from_currency = self.comboBox_1.currentText()
            to_currency = self.comboBox_2.currentText()

            exchange_rates = {"USD": 1.0, "PHP": 55.94, "CAD": 1.36, "GBP": 0.76}

            if from_currency in exchange_rates and to_currency in exchange_rates:
                convert_amount = amount*(exchange_rates[to_currency] / exchange_rates[from_currency])

                self.results_display.setText(f"{amount:.2f} {from_currency} = {convert_amount:.2f} {to_currency}")
            else:
                self.results_display.setText("Invalid Currency")
        except ValueError:
            self.results_display.setText("Invalid input")