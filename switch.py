import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from login import *
from register import *
from inform1 import *
from inform import *
from data import *
from schedule import *
from ExPanel import *

class switch(QMainWindow):

    def __init__(self):
        super(switch, self).__init__()
        
        layout = QStackedLayout()

        loginPanel = login()
        registerPanel = register()
        inform1Panel = inform1()
        informPanel = inform()
        schedulePanel = schedule()
        exPanel = ExPanel()

        layout.addWidget(loginPanel)
        layout.addWidget(registerPanel)
        layout.addWidget(inform1Panel)
        layout.addWidget(informPanel)
        layout.addWidget(schedulePanel)
        layout.addWidget(exPanel)
        
        layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(layout)

        loginPanel.addLayout(layout)
        registerPanel.addLayout(layout)
        inform1Panel.addLayout(layout)
        informPanel.addLayout(layout)
        schedulePanel.addLayout(layout)
        exPanel.addLayout(layout)

        self.setCentralWidget(widget)

        userData = data()

        loginPanel.addUserData(userData)
        registerPanel.addNewUserData(userData)
        inform1Panel.addNewUserData(userData)
        informPanel.addUserData(userData)
        schedulePanel.addUserData(userData)
        exPanel.addUserData(userData)

        informPanel.addSchedulePanel(schedulePanel)
        inform1Panel.addSchedulePanel(schedulePanel)


app = QApplication(sys.argv)

frame = switch()
frame.setMinimumSize(400,600)
frame.show()

app.exec()



     