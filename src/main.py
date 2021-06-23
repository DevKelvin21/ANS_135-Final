import sys
import os
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from modulos import *
from Interfaz import *
from Interfaz.formMain import Ui_Analisis_Numerico


class Analisis_Numerico(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Analisis_Numerico()       
        self.ui.setupUi(self)
    

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("docs/images/python.png"))
    Analisis_Numerico = QtWidgets.QMainWindow()
    ui = Ui_Analisis_Numerico()
    ui.setupUi(Analisis_Numerico)
    Analisis_Numerico.show()
    sys.exit(app.exec_())
  