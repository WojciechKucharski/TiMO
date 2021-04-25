from PyQt5 import QtCore, QtGui, QtWidgets
from harmony import HM
from function1 import f

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.bar_HMCR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bar_HMCR.setGeometry(QtCore.QRect(90, 90, 62, 22))
        self.bar_HMCR.setMaximum(1.00)
        self.bar_HMCR.setSingleStep(0.1)
        self.bar_HMCR.setValue(0.95)
        self.bar_HMCR.setObjectName("bar_HMCR")


        self.bar_PAR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bar_PAR.setGeometry(QtCore.QRect(90, 120, 62, 22))
        self.bar_PAR.setMaximum(1.00)
        self.bar_PAR.setSingleStep(0.1)
        self.bar_PAR.setValue(0.95)
        self.bar_PAR.setObjectName("bar_PAR")


        self.bar_bw = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bar_bw.setGeometry(QtCore.QRect(90, 150, 62, 22))
        self.bar_bw.setMaximum(5.00)
        self.bar_bw.setSingleStep(0.1)
        self.bar_bw.setValue(1.00)
        self.bar_bw.setObjectName("bar_bw")


        self.label_HMCR = QtWidgets.QLabel(self.centralwidget)
        self.label_HMCR.setGeometry(QtCore.QRect(30, 90, 47, 16))
        self.label_HMCR.setObjectName("label_HMCR")


        self.label_PAR = QtWidgets.QLabel(self.centralwidget)
        self.label_PAR.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.label_PAR.setObjectName("label_PAR")


        self.label_bw = QtWidgets.QLabel(self.centralwidget)
        self.label_bw.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_bw.setObjectName("label_bw")


        self.label_fun = QtWidgets.QLabel(self.centralwidget)
        self.label_fun.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_fun.setObjectName("label_fun")


        self.bar_HMSize = QtWidgets.QSpinBox(self.centralwidget)
        self.bar_HMSize.setGeometry(QtCore.QRect(230, 90, 101, 22))
        self.bar_HMSize.setMaximum(999)
        self.bar_HMSize.setValue(10)
        self.bar_HMSize.setObjectName("bar_HMSize")


        self.label_HMSize = QtWidgets.QLabel(self.centralwidget)
        self.label_HMSize.setGeometry(QtCore.QRect(180, 90, 47, 13))
        self.label_HMSize.setObjectName("label_HMSize")


        self.label_Radius = QtWidgets.QLabel(self.centralwidget)
        self.label_Radius.setGeometry(QtCore.QRect(180, 120, 47, 13))
        self.label_Radius.setObjectName("label_Radius")


        self.label_maxIter = QtWidgets.QLabel(self.centralwidget)
        self.label_maxIter.setGeometry(QtCore.QRect(180, 150, 47, 13))
        self.label_maxIter.setObjectName("label_maxIter")


        self.bar_maxIter = QtWidgets.QSpinBox(self.centralwidget)
        self.bar_maxIter.setGeometry(QtCore.QRect(230, 150, 101, 22))
        self.bar_maxIter.setMaximum(999999999)
        self.bar_maxIter.setObjectName("bar_maxIter")
        self.bar_maxIter.setValue(2500)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 90, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)

        self.bar_Radius = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bar_Radius.setGeometry(QtCore.QRect(230, 120, 101, 22))
        self.bar_Radius.setValue(5)
        self.bar_Radius.setObjectName("bar_Radius")


        self.text_in = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_in.setGeometry(QtCore.QRect(80, 40, 391, 31))
        self.text_in.setObjectName("text_in")


        self.text_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_out.setGeometry(QtCore.QRect(80, 290, 390, 290))
        self.text_out.setObjectName("text_out")


        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def clicked(self):
        a = HM()
        x = a.HarmonySearch(fun=self.text_in.toPlainText())
        self.text_out.setPlainText(x)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TiMO - Harmony Search"))

        self.label_HMCR.setText(_translate("MainWindow", "HMCR"))
        self.label_PAR.setText(_translate("MainWindow", "PAR"))
        self.label_bw.setText(_translate("MainWindow", "bw"))
        self.label_fun.setText(_translate("MainWindow", "Funkcja"))
        self.label_HMSize.setText(_translate("MainWindow", "HMSize"))
        self.label_Radius.setText(_translate("MainWindow", "Radius"))
        self.label_maxIter.setText(_translate("MainWindow", "maxIter"))
        self.pushButton.setText(_translate("MainWindow", "Uruchom Algorytm"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.text_in.setPlainText(_translate("MainWindow", "x1^2+x2^2"))
        self.text_out.setPlainText(_translate("MainWindow", "Wynik"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

