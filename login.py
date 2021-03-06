# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from data import *


class login(QtWidgets.QWidget):

    layout = QtWidgets.QStackedLayout()
    userData = data()

    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        #Form.setObjectName("Form")
        #Form.resize(400, 620)
        #Form.setStyleSheet("background-color: rgb(210, 237, 255);")
        #-------------
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#D2EDFF"))
        self.setPalette(palette)
        #-------------
        self.regbutton = QtWidgets.QPushButton(Form)
        self.regbutton.setGeometry(QtCore.QRect(270, 400, 93, 28))
        self.regbutton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.regbutton.setObjectName("regbutton")
        self.regbutton.clicked.connect(self.toRegisterPanel)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 81, 41))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(8, 8, 8);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 261, 151, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 151, 151, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 51, 41))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(270, 340, 93, 28))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.login)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.regbutton.setText(_translate("Form", "Register"))
        self.label_3.setText(_translate("Form", " Password"))
        self.label.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "User"))
        self.nextButton.setText(_translate("Form", "Next"))
        
    def login(self): 
        inputuser = self.lineEdit.text()
        inputpassword = self.lineEdit_2.text()
        userp = open('authen/userpassword.txt','r')
        userpp = userp.readlines()
        l = []
        userAccount = []
        userPassword = []
        for i in userpp:
            l.append(i.strip())
        userpp = l
        for i in range(len(userpp)):
            if i%2 == 0:
                userAccount.append(userpp[i])
            if i%2 == 1:
                userPassword.append(userpp[i])
        if inputuser in userAccount:
            index = userAccount.index(inputuser)
            if userPassword[index] == inputpassword:
                self.setupUserData(inputuser)
                print(self.userData.status)
                self.switchPanel(3)

            else:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
        else:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
    
    def addLayout(self, stackedLayout):
        self.layout = stackedLayout

    def toRegisterPanel(self):
        self.layout.setCurrentIndex(1)

    def switchPanel(self, p):
        self.layout.setCurrentIndex(p)

    def addUserData(self, userData):
        self.userData = userData

    def setupUserData(self, username):
        f = (open("progress/" + username,'r'))
        l = f.readline()
        x = l.split('|')
        self.userData.username = x[0]
        self.userData.program = x[1]
        self.userData.status = x[2]
        self.userData.firstDate = x[3]
        self.userData.latestDay = x[4]
        wi = f.readline()
        sw = wi.split('|')
        i = 0
        for j in sw:
            if(i%2 == 0):
                thisWt = self.userData.weight + "|" + sw[i]
                self.userData.weight = thisWt
            else:
                thisWa = self.userData.waistline + "|" + sw[i]
                self.userData.waistline = thisWa
            i = i + 1
        
        print(str(self.userData.weight))
        print(str(self.userData.waistline))

        print("Program = " + self.userData.program)



"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())"""
