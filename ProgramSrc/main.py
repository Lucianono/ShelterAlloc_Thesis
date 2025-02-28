from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtCore import Qt
from index import MainWindow
import sys
import os
import shutil


app = QApplication(sys.argv)


save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
if not os.path.exists(save_dir):
    os.makedirs(save_dir, exist_ok=True)  

    files_to_copy = [
        "commData.xlsx",
        "shelData.xlsx",
        "map.html",
        "allocation_results.xlsx",
        "modelCommData.xlsx",
        "modelShelData.xlsx",  
        "modelPerformanceResult.txt",
        "distance_matrix.xlsx",
        "modelParam.xlsx",
    ]

    for file_name in files_to_copy:
        bundled_path = os.path.join(sys._MEIPASS, file_name)
        destination_path = os.path.join(save_dir, file_name)
        shutil.copy2(bundled_path, destination_path)
    


# Force light mode palette
light_palette = QPalette()
light_palette.setColor(QPalette.Window, QColor(240, 240, 240))  # White background
light_palette.setColor(QPalette.WindowText, Qt.black)  # Black text
light_palette.setColor(QPalette.Base, QColor(255, 255, 255))  # White input fields
light_palette.setColor(QPalette.Text, Qt.black)
light_palette.setColor(QPalette.ButtonText, Qt.black)

app.setPalette(light_palette)

window = MainWindow()
window.show() 
window.setWindowTitle('Shelter Allocation')
window.setWindowIcon(QIcon(os.path.join(sys._MEIPASS, "ICONS", "logo.png")))

app.exec()