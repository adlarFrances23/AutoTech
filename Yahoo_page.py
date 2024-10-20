
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(579, 354)
        Form.setStyleSheet("*{\n"
"background-color:#3377ff;}")
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(0, 30, 581, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size:20px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 120, 271, 31))
        self.lineEdit.setStyleSheet("Background-color:none;\n"
"font-size:15px")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 170, 271, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_4.setGeometry(QtCore.QRect(320, 220, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_5.setGeometry(QtCore.QRect(140, 220, 70, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_6.setGeometry(QtCore.QRect(230, 220, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.login_btn = QtWidgets.QPushButton(parent=Form)
        self.login_btn.setGeometry(QtCore.QRect(170, 260, 211, 41))
        self.login_btn.setMouseTracking(True)
        self.login_btn.setStyleSheet("background:black;\n"
"border: 1px solid #3385ff;\n"
"color:white;\n"
"font-family: Georgia, serif;\n"
"font-size:15px;\n"
"\n"
"\n"
"")
        self.login_btn.setObjectName("login_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Yahoo"))
        self.lineEdit.setPlaceholderText(_translate("Form", "File Name"))
        self.comboBox.setItemText(0, _translate("Form", "Without_Proxy"))
        self.comboBox.setItemText(1, _translate("Form", "Proxy"))
        self.checkBox_4.setText(_translate("Form", "Keyboard Action"))
        self.checkBox_5.setText(_translate("Form", "Random Action"))
        self.checkBox_6.setText(_translate("Form", "Mouse action"))
        self.login_btn.setText(_translate("Form", "Login"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
