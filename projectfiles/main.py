from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from windowsetup import setupGUI_
from functools import partial
import time
import sys
from _thread import *


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.HM = HM()
        ########################################### Empty Variables for Future PyQt5 Objects
        self.functions_obj = []
        self.parameters_obj = []
        self.parameters_labels = []
        self.cube_obj = [[], [], []]
        self.push_obj = []
        self.text_in = None
        self.text_out = None
        self.checkBox = None
        ########################################### Example Functions
        self.functions = {"Simple function": "x1^2+x2^2"}
        try:
            data = [str(x).replace("\n", "") for x in open("functions.txt", "r")]
            for i in range(len(data) // 2):
                self.functions[data[i * 2]] = data[i * 2 + 1]
        except Exception as e:
            pass
        self.setupGUI(MainWindow)
        start_new_thread(update, (self, ))

    def updateAll(self):
        N = getDim(self.text_in.toPlainText())
        if N != None:
            for i in range(3):
                for j in range(5):
                    self.cube_obj[i][j].visible = (j<N)


    def hookfunctions(self):
        self.push_obj[0].clicked.connect(self.clicked)
        self.push_obj[1].clicked.connect(self.draw_plots)
        for i, x in enumerate(self.functions_obj):
            x.triggered.connect(partial(self.example, [x for x in self.functions.keys()][i]))

    def getValues(self):
        args = []
        args.append(self.text_in.toPlainText()) #fun
        for x in self.parameters_obj:
            args.append(x.value())
        args.append(self.checkBox.isChecked())
        args.append([[self.cube_obj[i][x].value() for i in [0, 2]] for x in range(5)])
        return args

    def example(self, no):
        self.text_in.setPlainText(self.functions[no])

    def draw_plots(self):
        if self.HM.clear:
            return 0
        else:
            self.HM.plotHistory()
            self.HM.plotLayers()

    def clicked(self):
        args = self.getValues()
        x = self.HM.HarmonySearch(fun=args[0],
                            HMCR = args[1],
                            PAR = args[2],
                            HMSize = args[4],
                            maxIter = args[5],
                            BW = args[3],
                            draw = args[6],
                            cube = args[7]
                            )
        self.text_out.setPlainText(x)

    def setupGUI(self, MainWindow):
        setupGUI_(self, MainWindow)


def update(self):
    try:
        args = self.getValues()
        while True:
            time.sleep(0.1)
            tmp = self.getValues()
            if tmp != args:
                print("Zmiana")
                args = tmp
            self.updateAll()
    except Exception as e:
        print(e)

def getDim(fun):
    varDim = None
    try:
        for i in range(1, 6):
            if f"x{i}" in fun:
                varDim = i
        return varDim
    except Exception as e:
        return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
