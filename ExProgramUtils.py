class ExProgramUtils():

    f1 = []
    f2 = []
    f3 = []

    def __init__(self):
        f = open("exprogram.txt", "r").readlines()
        l = []
        for i in f:
            l.append(i.split(' '))
        for i in l:
            try:
                i[3] = i[3][:-1]
            except:
                continue
        self.f1 = l[:69]
        self.f2 = l[71:148]
        self.f3 = l[150:]

    def getFullProgram(self, exProgram):
        if(exProgram == "f1"):
            return self.f1
        elif(exProgram == "f2"):
            return self.f2
        else:
            return self.f3

    def getDailyProgram(self, exProgram, day):
        fullProgram = self.getFullProgram(exProgram)
        dailyProgram = []
        i = 0
        for j in fullProgram:
            p = fullProgram[i]
            if(p[0] == day):
                dailyProgram.append(p)
                #print(dailyProgram)
            i = i + 1
        return dailyProgram        
    