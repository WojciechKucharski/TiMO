from PyQt5 import QtCore, QtGui, QtWidgets

def setupGUI_(self, MainWindow):
    ########################################### Main Window
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(520, 520)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "TiMO - Harmony Search"))

    ########################################### Float Parameters
    for i in range(3):
        self.parameters_obj.append(QtWidgets.QDoubleSpinBox(self.centralwidget))
        self.parameters_obj[-1].setGeometry(QtCore.QRect(90, 60 + i * 30, 62, 22))
        self.parameters_obj[-1].setMaximum(1.0)
        self.parameters_obj[-1].setSingleStep(0.05)
        self.parameters_obj[-1].setProperty("value", 0.95)

    ########################################### Int Parameters
    for i in range(2):
        st_value = [10, 250]
        self.parameters_obj.append(QtWidgets.QSpinBox(self.centralwidget))
        self.parameters_obj[-1].setGeometry(QtCore.QRect(90, 150 + i * 30, 61, 22))
        self.parameters_obj[-1].setMaximum(999999999)
        self.parameters_obj[-1].setProperty("value", st_value[i])

    ########################################### Parameters Labels
    for i, x in enumerate(["HCMR", "PAR", "bw", "HMSize", "maxIter"]):
        self.parameters_labels.append(QtWidgets.QLabel(self.centralwidget))
        self.parameters_labels[-1].setGeometry(QtCore.QRect(30, 60 + i * 30, 47, 16))
        self.parameters_labels[-1].setText(_translate("MainWindow", x))

    ########################################### Cube Input
    for i in range(5):
        ########################################### Cube Labels
        self.cube_obj[1].append(QtWidgets.QLabel(self.centralwidget))
        self.cube_obj[1][-1].setGeometry(QtCore.QRect(240, 60 + i * 30, 47, 13))
        self.cube_obj[1][-1].setText(_translate("MainWindow", f"<=x{i + 1}<="))
        ########################################### Cube Input
        for j in [0, 2]:
            self.cube_obj[j].append(QtWidgets.QDoubleSpinBox(self.centralwidget))
            self.cube_obj[j][-1].setGeometry(QtCore.QRect(180 + j * 55, 60 + i * 30, 51, 22))
            self.cube_obj[j][-1].setMinimum(-999999.0)
            self.cube_obj[j][-1].setMaximum(999999.0)
            self.cube_obj[j][-1].setSingleStep(0.5)
            self.cube_obj[j][-1].setProperty("value", 5.0 * (j - 1))

    ########################################### Check Box
    self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
    self.checkBox.setGeometry(QtCore.QRect(360, 120, 70, 17))
    self.checkBox.setChecked(True)
    self.checkBox.setText(_translate("MainWindow", "Wykresy"))

    ########################################### Push Buttons
    for i, x in enumerate(["Uruchom Algorytm", "Pokaż wykresy"]):
        self.push_obj.append(QtWidgets.QPushButton(self.centralwidget))
        self.push_obj[-1].setGeometry(QtCore.QRect(360, 60 + i * 30, 111, 23))
        self.push_obj[-1].setText(_translate("MainWindow", x))

    ########################################### Function Input
    self.text_in = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.text_in.setGeometry(QtCore.QRect(90, 10, 381, 31))
    self.text_in.setPlainText(_translate("MainWindow", "x1^2+x2^2"))

    ########################################### Alg. Output
    self.text_out = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.text_out.setGeometry(QtCore.QRect(90, 220, 381, 241))
    self.text_out.setPlainText(_translate("MainWindow", "Wynik"))

    ########################################### Function Input Label
    self.label_fun = QtWidgets.QLabel(self.centralwidget)
    self.label_fun.setGeometry(QtCore.QRect(30, 20, 47, 13))
    self.label_fun.setText(_translate("MainWindow", "Funkcja"))

    ########################################### MENU

    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)

    MainWindow.setStatusBar(self.statusbar)
    self.menuBar = QtWidgets.QMenuBar(MainWindow)
    self.menuBar.setGeometry(QtCore.QRect(0, 0, 517, 21))

    self.menuFunkcje = QtWidgets.QMenu(self.menuBar)
    self.menuBar.addAction(self.menuFunkcje.menuAction())

    self.menuFunkcje.setTitle(_translate("MainWindow", "Funkcje"))
    MainWindow.setMenuBar(self.menuBar)

    ########################################### Menu Options

    for i, x in enumerate([x for x in self.functions.keys()]):
        self.functions_obj.append(QtWidgets.QAction(MainWindow))
        self.functions_obj[-1].setObjectName(f"actionPrzyklad{i + 1}")
        self.functions_obj[-1].setText(_translate("MainWindow", x))
        self.menuFunkcje.addAction(self.functions_obj[-1])

    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    self.hookfunctions()
