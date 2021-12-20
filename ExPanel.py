from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QStackedLayout
from PyQt5.QtGui import QMovie
from ExProgramUtils import *
from data import *

class ExPanel(QWidget):

    todayPragram = []
    day = "01"
    exNameLabel = ""
    exPictureLabel = ""
    exTimerLabel = ""
    startButton = ""
    animationWidth = 400
    animationHeight = 400
    layout = QStackedLayout()
    userData = data()
    start = "Start"
    load = "Load today program"
    next = "Next exercise"
    finish = "Finish"
    currentExStep = 0
    timer = QtCore.QTimer()
    steps = 0


    def __init__(self):
        super(ExPanel, self).__init__()
        layout = QVBoxLayout()
        
        self.exNameLabel = QLabel("Exercise",self)
        self.exPictureLabel = QMovieLabel("exgif/plank.gif")
        self.exTimerLabel = QLabel("00",self)
        self.startButton = QPushButton(self.load,self)

        self.exNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exNameLabel.setStyleSheet("font-size: 40px; text-align: center")
        self.exTimerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exTimerLabel.setStyleSheet("font-size: 40px; text-align: center")
        
        self.startButton.clicked.connect(self.buttonAction)

        layout.addWidget(self.exNameLabel)
        layout.addWidget(self.exPictureLabel, 5)
        layout.addWidget(self.exTimerLabel)
        layout.addWidget(self.startButton)

        self.setLayout(layout)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.repaintExTimerLabel)

    def setTodayProgram(self, program):
        for i in range(program.__len__()):
            print(str(program[i]))
        self.todayPragram = program
        firstProgram = self.todayPragram[0]
        programName = firstProgram[3]
        programDuration = firstProgram[2]
        movie = QMovie("exgif/"+programName + ".gif")
        movie.start()
        self.exPictureLabel.setMovie(movie)
        s=movie.currentImage().size()
        self.animationWidth = s.width()
        self.animationHeight = s.height()
        self.exNameLabel.setText(programName.capitalize())
        self.exTimerLabel.setText(programDuration)

    def setNextProgram(self):
        nextProgram = self.todayPragram[self.currentExStep]
        programName = nextProgram[3]
        programDuration = nextProgram[2]
        movie = QMovie("exgif/"+programName + ".gif")
        movie.start()
        self.exPictureLabel.setMovie(movie)
        s=movie.currentImage().size()
        self.animationWidth = s.width()
        self.animationHeight = s.height()
        self.exNameLabel.setText(programName.capitalize())
        self.exTimerLabel.setText(programDuration)
    
    def buttonAction(self):
        if(self.startButton.text() == self.load):
            #ใช้ data หา f, day
            programDay = str(int(self.userData.latestDay) +1 )
            if(programDay.__len__() < 2):
                programDay = "0" + programDay
            program = ExProgramUtils().getDailyProgram(self.userData.program, programDay)
            self.steps = program.__len__()
            print("" + programDay)
            self.setTodayProgram(program)
            self.startButton.setText(self.start)
        elif(self.startButton.text() == self.start):
            self.countDown()
        elif(self.startButton.text() == self.next):
            self.nextEx()
        else:
            self.finishEx()

    def getAnimationWidth(self):
        return self.animationWidth

    def getAnimationHeight(self):
        return self.animationHeight

    def addLayout(self, stackedLayout):
        self.layout = stackedLayout

    def addUserData(self, userData):
        self.userData = userData
    
    def countDown(self):
        exTimeText = self.exTimerLabel.text()
        print(exTimeText)
        self.timer.start(1000)
        self.currentExStep += 1

    def nextEx(self):
        self.setNextProgram()
        self.startButton.setText(self.start)

    def repaintExTimerLabel(self):
        exTime = int(self.exTimerLabel.text())
        self.exTimerLabel.setText(str(exTime -1))
        if(exTime == 1):
            self.timer.stop()
        if(self.currentExStep < self.steps):
            self.startButton.setText(self.next)
        else:
            self.startButton.setText(self.finish)

    def finishEx(self):
        self.layout.setCurrentIndex(4)


        
        


class QMovieLabel(QLabel):
    def __init__(self, fileName):
        QLabel.__init__(self)
        m = QMovie(fileName)
        m.start()
        self.setMovie(m)

    def setMovie(self, movie):
        QLabel.setMovie(self, movie)
        s=movie.currentImage().size()
        self._movieWidth = s.width()
        self._movieHeight = s.height()