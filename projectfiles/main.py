from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from windowsetup import *
from functools import partial

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.HM = HM()
        self.functions = {"Simple function": "x1^2+x2^2"}
        self.functions_obj = []
        self.parameters_obj = []
        self.parameters_labels = []
        self.cube_obj = [[], [], []]
        try:
            data = [str(x).replace("\n", "") for x in open("functions.txt", "r")]
            for i in range(len(data) // 2):
                self.functions[data[i * 2]] = data[i * 2 + 1]
        except Exception as e:
            print(e)
        wrapper_setupUi(self, MainWindow)

    @property
    def functions_list(self):
        return [x for x in self.functions.keys()]

    def hookfunctions(self):
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton2.clicked.connect(self.draw_plots)
        for i, x in enumerate(self.functions_obj):
            x.triggered.connect(partial(self.example, self.functions_list[i]))

    def example(self, no):
        self.text_in.setPlainText(self.functions[no])

    def getValues(self):
        args = []
        args.append(self.text_in.toPlainText()) #fun
        for x in self.parameters_obj:
            args.append(x.value())
        args.append(self.checkBox.isChecked())
        cube = []
        for x in range(5):
            cube.append([self.cube_obj[i][x].value() for i in [0, 2]])
        args.append(cube)
        return args

    def draw_plots(self):
        if self.HM.clear:
            return 0
        else:
            self.HM.plotHistory()
            self.HM.plotLayers()


    def clicked(self):
        args = self.getValues()
        print(args)
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.hookfunctions()
    MainWindow.show()
    sys.exit(app.exec_())
