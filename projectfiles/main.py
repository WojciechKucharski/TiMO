from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from windowsetup import setupGUI
from functools import partial
import time
import sys
from _thread import *
from crash_log import printError


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        ########################################### Harmony Search Object
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
        ########################################### Example Functions from File
        self.functions = {"Simple function": "x1^2+x2^2"}
        try:
            data = [str(x).replace("\n", "") for x in open("Data\\functions.txt", "r")]
            for i in range(len(data) // 2):
                self.functions[data[i * 2]] = data[i * 2 + 1]
        except:
            pass
        ########################################### GUI Setup
        setupGUI(self, MainWindow)

        ########################################### Cube Updating Thread
        start_new_thread(update, (self,))

    ########################################### Update Cube Buttons
    def updateAll(self):
        N = getDim(self.text_in.toPlainText())
        if N != None:
            for i in range(3):
                for j in range(5):
                    self.cube_obj[i][j].setVisible(j < N)
        for i in range(5):  # update number of Spin Boxes
            self.cube_obj[0][i].setMaximum(self.cube_obj[2][i].value())
            self.cube_obj[2][i].setMinimum(self.cube_obj[0][i].value())

    def hookfunctions(self):  # update limits in Spin Boxes
        self.push_obj[0].clicked.connect(self.clicked)
        self.push_obj[1].clicked.connect(self.draw_plots)
        for i, x in enumerate(self.functions_obj):
            x.triggered.connect(partial(self.example, [x for x in self.functions.keys()][i]))

    ########################################### Get All Parameters from GUI
    def getValues(self):
        args = []
        args.append(self.text_in.toPlainText())  # fun
        for x in self.parameters_obj:
            args.append(x.value())
        args.append(self.checkBox.isChecked())
        args.append([[self.cube_obj[i][x].value() for i in [0, 2]] for x in range(5)])
        return args

    ########################################### Put Example Fun. To Window
    def example(self, no):
        self.text_in.setPlainText(self.functions[no])

    ########################################### Draw Plots Again - Button
    def draw_plots(self):
        if self.HM.clear:
            return 0
        else:
            self.HM.plotHistory()
            self.HM.plotLayers()

    ########################################### Run Harmony Search - Button
    def clicked(self):
        args = self.getValues()
        x = self.HM.HarmonySearch(fun=args[0], HMCR=args[1], PAR=args[2], HMSize=args[4],
                                  maxIter=args[5], BW=args[3], drawPlots=args[6], cube=args[7])
        self.text_out.setPlainText(x)


########################################### Updating Thread
def update(self):
    try:
        args = self.getValues()
        while True:
            time.sleep(0.1)
            tmp = self.getValues()
            if tmp != args:
                args = tmp
            self.updateAll()
    except Exception as e:
        print(e)


########################################### Get FUN Dimension
def getDim(fun):
    varDim = None
    try:
        for i in range(1, 6):
            if f"x{i}" in fun:
                varDim = i
        return varDim
    except Exception as e:
        return None


########################################### MAIN
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:  # error LOG
        printError(e)
###########################################
