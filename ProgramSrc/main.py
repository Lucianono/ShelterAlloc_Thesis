from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from index import MainWindow
import sys

app = QApplication(sys.argv)

# Force light mode palette
light_palette = QPalette()
light_palette.setColor(QPalette.Window, QColor(255, 255, 255))  # White background
light_palette.setColor(QPalette.WindowText, Qt.black)  # Black text
light_palette.setColor(QPalette.Base, QColor(255, 255, 255))  # White input fields
light_palette.setColor(QPalette.Text, Qt.black)
light_palette.setColor(QPalette.ButtonText, Qt.black)

app.setPalette(light_palette)

window = MainWindow()
window.show() 

app.exec()