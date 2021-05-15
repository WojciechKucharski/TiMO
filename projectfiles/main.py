from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from windowsetup import *
from functools import partial

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.HM = HM()
        self.functions = {"Simple function": "x1^2+x2^2"}
        self.functions_obj = []
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

    def retranslateUi(self, MainWindow):
        wrapper_retranslateUi(self, MainWindow)

    def hookfunctions(self):
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton2.clicked.connect(self.draw_plots)
        for i, x in enumerate(self.functions_obj):
            x.triggered.connect(partial(self.example, self.functions_list[i]))

        """self.actionPrzyklad1.triggered.connect(partial(self.example, "camel"))
        self.actionPrzyklad2.triggered.connect(partial(self.example, "himmel"))
        self.actionPrzyklad3.triggered.connect(partial(self.example, "goldstein"))
        self.actionPrzyklad4.triggered.connect(partial(self.example, "ackley"))
        self.actionPrzyklad5.triggered.connect(partial(self.example, "cross"))"""

    def example(self, no):
        self.text_in.setPlainText(self.functions[no])

    def getValues(self):
        args = []
        args.append(self.text_in.toPlainText()) #fun
        args.append(self.bar_HMCR.value())
        args.append(self.bar_PAR.value())
        args.append(self.bar_HMSize.value())
        args.append(self.bar_maxIter.value())
        args.append(self.bar_bw.value())
        args.append(self.checkBox.isChecked())
        cube = []
        for x in range(1,6):
            new = []
            new.append(min(eval(f"self.x1l_{x}.value()"), eval(f"self.x1u_{x}.value()")))
            new.append(max(eval(f"self.x1l_{x}.value()"), eval(f"self.x1u_{x}.value()")))
            cube.append(new)
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

        x = self.HM.HarmonySearch(fun=args[0],
                            HMCR = args[1],
                            PAR = args[2],
                            HMSize = args[3],
                            maxIter = args[4],
                            BW = args[5],
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
