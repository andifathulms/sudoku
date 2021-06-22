import sys
import numpy as np
import time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

def possible(y,x,n):
        global grid
        for i in range(0,9):
            if grid[y][i] == n :
                return False
        for i in range(0,9):
            if grid[i][x] == n :
                return False
        x0 = (x//3) * 3
        y0 = (y//3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == n :
                    return False
        return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        #solve()
                        grid[y][x] = 0    
                return
        #app = QApplication(sys.argv)
        #widget = QtWidgets.QStackedWidget()
        #screen = mainWindow()
        #widget.addWidget(screen)
        #widget.show()
        #try:
        #    sys.exit(app.exec_())
        #except:
        #    print("Exiting")
    print(np.matrix(grid))
    #input("More?")

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        loadUi("sudoku.ui", self)
        self.writeToScreen()
        #self.solve()
        while not(self.isComplete()):
            self.solve()
            self.writeToScreen()

    def writeToScreen(self):
        print("write")
        global grid
        label = [[self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19],
                 [self.label21,self.label22,self.label23,self.label24,self.label25,self.label26,self.label27,self.label28,self.label29],
                 [self.label31,self.label32,self.label33,self.label34,self.label35,self.label36,self.label37,self.label38,self.label39],
                 [self.label41,self.label42,self.label43,self.label44,self.label45,self.label46,self.label47,self.label48,self.label49],
                 [self.label51,self.label52,self.label53,self.label54,self.label55,self.label56,self.label57,self.label58,self.label59],
                 [self.label61,self.label62,self.label63,self.label64,self.label65,self.label66,self.label67,self.label68,self.label69],
                 [self.label71,self.label72,self.label73,self.label74,self.label75,self.label76,self.label77,self.label78,self.label79],
                 [self.label81,self.label82,self.label83,self.label84,self.label85,self.label86,self.label87,self.label88,self.label89],
                 [self.label91,self.label92,self.label93,self.label94,self.label95,self.label96,self.label97,self.label98,self.label99]]
        
        for i in range(9):
            for j in range(9):
                if grid[j][i] == 0 :
                    label[j][i].setText("")
                else:
                    label[j][i].setText(str(grid[j][i]))

    def isComplete(self):
        label = [[self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19],
                 [self.label21,self.label22,self.label23,self.label24,self.label25,self.label26,self.label27,self.label28,self.label29],
                 [self.label31,self.label32,self.label33,self.label34,self.label35,self.label36,self.label37,self.label38,self.label39],
                 [self.label41,self.label42,self.label43,self.label44,self.label45,self.label46,self.label47,self.label48,self.label49],
                 [self.label51,self.label52,self.label53,self.label54,self.label55,self.label56,self.label57,self.label58,self.label59],
                 [self.label61,self.label62,self.label63,self.label64,self.label65,self.label66,self.label67,self.label68,self.label69],
                 [self.label71,self.label72,self.label73,self.label74,self.label75,self.label76,self.label77,self.label78,self.label79],
                 [self.label81,self.label82,self.label83,self.label84,self.label85,self.label86,self.label87,self.label88,self.label89],
                 [self.label91,self.label92,self.label93,self.label94,self.label95,self.label96,self.label97,self.label98,self.label99]]
        for lbl in label:
            for lb in lbl:
                if lb.text() == "":
                    return False
        return True

    def possible(self,y,x,n):
        global grid
        for i in range(0,9):
            if grid[y][i] == n :
                return False
        for i in range(0,9):
            if grid[i][x] == n :
                return False
        x0 = (x//3) * 3
        y0 = (y//3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == n :
                    return False
        return True

    def solve(self):
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y,x,n):
                            grid[y][x] = n
                            #solve()
                            grid[y][x] = 0    
                    return
        print(np.matrix(grid))
        #input("More?")

if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #widget = QtWidgets.QStackedWidget()
    #screen = mainWindow()
    #widget.addWidget(screen)
    #widget.show()
    solve()
    #try:
    #    sys.exit(app.exec_())
    #except:
    #    print("Exiting")
