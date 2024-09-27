from PySide6.QtWidgets import QApplication
from frontpage import MySideBar
import sys

app = QApplication(sys.argv)

window = MySideBar()
window.show()

app.exec()