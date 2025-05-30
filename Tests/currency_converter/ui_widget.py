# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(362, 498)
        font = QtGui.QFont()
        font.setPointSize(16)
        widget.setFont(font)
        self.label = QtWidgets.QLabel(parent=widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=widget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.amount_lineEdit = QtWidgets.QLineEdit(parent=widget)
        self.amount_lineEdit.setGeometry(QtCore.QRect(30, 160, 301, 41))
        self.amount_lineEdit.setStyleSheet("* {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    padding: 1px;\n"
"}")
        self.amount_lineEdit.setObjectName("amount_lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=widget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_1 = QtWidgets.QComboBox(parent=widget)
        self.comboBox_1.setGeometry(QtCore.QRect(30, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=widget)
        self.label_4.setGeometry(QtCore.QRect(150, 270, 51, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Arrows/arrows.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=widget)
        self.label_5.setGeometry(QtCore.QRect(210, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(parent=widget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.results_display = QtWidgets.QLabel(parent=widget)
        self.results_display.setGeometry(QtCore.QRect(30, 330, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.results_display.setFont(font)
        self.results_display.setObjectName("results_display")
        self.convert_button = QtWidgets.QPushButton(parent=widget)
        self.convert_button.setGeometry(QtCore.QRect(40, 390, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.convert_button.setFont(font)
        self.convert_button.setStyleSheet("* {\n"
"    background-color: #09A67B;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"}")
        self.convert_button.setObjectName("convert_button")
        self.label_6 = QtWidgets.QLabel(parent=widget)
        self.label_6.setGeometry(QtCore.QRect(60, 460, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "Currency Converter"))
        self.label_2.setText(_translate("widget", "Enter Amount:"))
        self.amount_lineEdit.setPlaceholderText(_translate("widget", "Enter Amount Here"))
        self.label_3.setText(_translate("widget", "From:"))
        self.comboBox_1.setItemText(0, _translate("widget", "USD"))
        self.comboBox_1.setItemText(1, _translate("widget", "PHP"))
        self.comboBox_1.setItemText(2, _translate("widget", "GBP"))
        self.comboBox_1.setItemText(3, _translate("widget", "CAD"))
        self.label_5.setText(_translate("widget", "To:"))
        self.comboBox_2.setItemText(0, _translate("widget", "USD"))
        self.comboBox_2.setItemText(1, _translate("widget", "PHP"))
        self.comboBox_2.setItemText(2, _translate("widget", "GBP"))
        self.comboBox_2.setItemText(3, _translate("widget", "CAD"))
        self.results_display.setText(_translate("widget", "1 USD = 55.94 PHP"))
        self.convert_button.setText(_translate("widget", "Get Exchange Rate"))
        self.label_6.setText(_translate("widget", "exchanged rates are hard coded*"))
