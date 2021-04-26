from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from windowsetup import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        wrapper_setupUi(self, MainWindow)
    def retranslateUi(self, MainWindow):
        wrapper_retranslateUi(self, MainWindow)

    def hookfunctions(self):
        self.pushButton.clicked.connect(self.clicked)
        self.actionPrzyklad1.triggered.connect(self.camel)
        self.actionPrzyklad2.triggered.connect(self.himmel)
        self.actionPrzyklad3.triggered.connect(self.goldstein)
        self.actionPrzyklad4.triggered.connect(self.ackley)
        self.actionPrzyklad5.triggered.connect(self.cross)

    def camel(self):
        self.text_in.setPlainText("2*x1^2-1.05*x1^4+x1^6/6+x1*x2+x2^2")
    def goldstein(self):
        self.text_in.setPlainText("x1^2+x2^2")
    def himmel(self):
        self.text_in.setPlainText("(x1^2+x2-11)^2+(x1+x2^2-7)^2")
    def ackley(self):
        self.text_in.setPlainText("-20*exp(-0.2*sqrt(0.5*(x1^2+x2^2))-exp(0.5*(cos(2*pi*x1)+cos(2*pi*x2))+exp(1)+20")
    def cross(self):
        self.text_in.setPlainText("-0.0001*(abs(sin(x1)*sin(x2)*exp(abs(100-1/pi*sqrt(x1^2+x2^2))))+1)^0.1")

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

    def clicked(self):
        a = HM()
        args = self.getValues()

        x = a.HarmonySearch(fun=args[0],
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
