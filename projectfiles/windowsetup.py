from PyQt5 import QtCore, QtGui, QtWidgets

def wrapper_setupUi(self, MainWindow):
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
    for i in range(5):
        self.parameters_labels.append(QtWidgets.QLabel(self.centralwidget))
        self.parameters_labels[-1].setGeometry(QtCore.QRect(30, 60 + i * 30, 47, 16))

    ########################################### Cube Input
    for i in range(5):
        ########################################### Cube Labels
        self.cube_obj[1].append(QtWidgets.QLabel(self.centralwidget))
        self.cube_obj[1][-1].setGeometry(QtCore.QRect(240, 60 + i * 30, 47, 13))
        ########################################### Cube Input
        for j in [0, 2]:
            self.cube_obj[j].append(QtWidgets.QDoubleSpinBox(self.centralwidget))
            self.cube_obj[j][-1].setGeometry(QtCore.QRect(180 + j * 55, 60 + i * 30, 51, 22))
            self.cube_obj[j][-1].setMinimum(-999999.0)
            self.cube_obj[j][-1].setMaximum(999999.0)
            self.cube_obj[j][-1].setSingleStep(0.5)
            self.cube_obj[j][-1].setProperty("value", 5.0 * (j - 1))


    self.label_fun = QtWidgets.QLabel(self.centralwidget)
    self.label_fun.setGeometry(QtCore.QRect(30, 20, 47, 13))
    self.label_fun.setObjectName("label_fun")


    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton.setGeometry(QtCore.QRect(360, 60, 111, 23))
    self.pushButton.setObjectName("pushButton")

    self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton2.setGeometry(QtCore.QRect(360, 120, 111, 23))
    self.pushButton2.setObjectName("pushButton2")

    self.text_in = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.text_in.setGeometry(QtCore.QRect(90, 10, 381, 31))
    self.text_in.setObjectName("text_in")

    self.text_out = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.text_out.setGeometry(QtCore.QRect(90, 220, 381, 241))
    self.text_out.setObjectName("text_out")

    self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
    self.checkBox.setGeometry(QtCore.QRect(360, 90, 70, 17))
    self.checkBox.setObjectName("checkBox")
    self.checkBox.setChecked(True)

    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")

    MainWindow.setStatusBar(self.statusbar)
    self.menuBar = QtWidgets.QMenuBar(MainWindow)
    self.menuBar.setGeometry(QtCore.QRect(0, 0, 517, 21))
    self.menuBar.setObjectName("menuBar")

    self.menuFunkcje = QtWidgets.QMenu(self.menuBar)
    self.menuFunkcje.setObjectName("menuFunkcje")
    MainWindow.setMenuBar(self.menuBar)

    for i in range(len(self.functions_list)):
        self.functions_obj.append(QtWidgets.QAction(MainWindow))
        self.functions_obj[-1].setObjectName(f"actionPrzyklad{i+1}")
        self.menuFunkcje.addAction(self.functions_obj[-1])

    self.menuBar.addAction(self.menuFunkcje.menuAction())

    for i, x in enumerate(["HCMR", "PAR", "bw", "HMSize", "maxIter"]):
        self.parameters_labels[i].setText(_translate("MainWindow", x))

    for i in range(5):
        self.cube_obj[1][i].setText(_translate("MainWindow", f"<=x{i + 1}<="))

    for i, x in enumerate(self.functions_obj):
        x.setText(_translate("MainWindow", self.functions_list[i]))

    self.menuFunkcje.setTitle(_translate("MainWindow", "Funkcje"))
    self.text_out.setPlainText(_translate("MainWindow", "Wynik"))
    self.checkBox.setText(_translate("MainWindow", "Wykresy"))
    self.label_fun.setText(_translate("MainWindow", "Funkcja"))
    self.pushButton.setText(_translate("MainWindow", "Uruchom Algorytm"))
    self.pushButton2.setText(_translate("MainWindow", "Pokaż wykresy"))
    self.text_in.setPlainText(_translate("MainWindow", "x1^2+x2^2"))

    QtCore.QMetaObject.connectSlotsByName(MainWindow)

