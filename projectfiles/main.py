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

    def getValues(self):
        print("lol")
        args = []
        args.append(self.text_in.toPlainText()) #fun
        args.append(self.bar_HMCR.value())
        args.append(self.bar_PAR.value())
        args.append(self.bar_HMSize.value())
        args.append(self.bar_maxIter.value())
        args.append(self.bar_bw.value())
        return args

    def clicked(self):
        a = HM()
        args = self.getValues()
        print(args)
        x = a.HarmonySearch(fun=args[0],
                            HMCR = args[1],
                            PAR = args[2],
                            HMSize = args[3],
                            maxIter = args[4],
                            BW = args[5]
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
