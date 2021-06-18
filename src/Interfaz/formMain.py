from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
import modulos.images_rc
import matplotlib.pyplot as plt
import math as mt
import cmath
import platform
from modulos import *
import modulos.globalfunctions as funciones
import modulos.unidaddos as unidad_dos
import modulos.unidadtres as unidad_tres
import modulos.unidadcuatro as unidad_cuatro
import modulos.unidadcinco as unidad_cinco

#Declaramos Variables Globales con valores preestablecidos
Numero_Filas_Columnas = 3
etiquetaHermite = "y'"
Numero_filas_Hermite = 2

class Ui_Analisis_Numerico(object):
    def setupUi(self, Analisis_Numerico):
        Analisis_Numerico.setObjectName("Analisis_Numerico")
        Analisis_Numerico.resize(1235, 684)
        Analisis_Numerico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Analisis_Numerico)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 50, 991, 611))
        self.frame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(246, 247, 251);\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnResolverlo = QtWidgets.QPushButton(self.frame)
        self.btnResolverlo.setGeometry(QtCore.QRect(360, 210, 131, 51))
        self.btnResolverlo.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 10pt \"SpaceMono Nerd Font\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(87, 85, 183);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    border:0px;\n"
"    \n"
"    background-color: rgb(70, 69, 149);\n"
"\n"
"}")
        self.btnResolverlo.setObjectName("btnResolverlo")
        self.btnLimpiar = QtWidgets.QPushButton(self.frame)
        self.btnLimpiar.setGeometry(QtCore.QRect(510, 210, 141, 51))
        self.btnLimpiar.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    color: rgb(87, 85, 183);\n"
"    font: 75 10pt \"SpaceMono Nerd Font\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    border:0px;\n"
"    background-color: rgb(221, 221, 221);\n"
"    \n"
"}\n"
"")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 280, 941, 281))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 921, 261))
        self.tableWidget.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(70, 30, 261, 121))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 41))
        self.label.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.label.setObjectName("label")
        self.txtfuncion = QtWidgets.QLineEdit(self.frame_3)
        self.txtfuncion.setGeometry(QtCore.QRect(40, 60, 181, 21))
        self.txtfuncion.setStyleSheet("background-image: url(:/images/barra2.png);\n"
"background-image: url(:/images/images/barra2.png);\n"
"font: 8pt \"SpaceMono Nerd Font\";\n"
"border: 0px;")
        self.txtfuncion.setObjectName("txtfuncion")
        self.lbl_mensaje_funcion = QtWidgets.QLabel(self.frame_3)
        self.lbl_mensaje_funcion.setGeometry(QtCore.QRect(30, 90, 221, 20))
        self.lbl_mensaje_funcion.setStyleSheet("font: 7pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_mensaje_funcion.setObjectName("lbl_mensaje_funcion")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(350, 30, 281, 121))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 211, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.label_2.setObjectName("label_2")
        self.txtX1 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX1.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.txtX1.setStyleSheet("background-image: url(:/images/images/barra.png);\n"
"border: 0px;\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.txtX1.setObjectName("txtX1")
        self.txtX2 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX2.setGeometry(QtCore.QRect(130, 60, 41, 21))
        self.txtX2.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.txtX2.setObjectName("txtX2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 31, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 31, 31))
        self.label_4.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.label_4.setObjectName("label_4")
        self.txtX2_2 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX2_2.setGeometry(QtCore.QRect(220, 60, 41, 21))
        self.txtX2_2.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.txtX2_2.setObjectName("txtX2_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(190, 60, 31, 31))
        self.label_7.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);;")
        self.label_7.setObjectName("label_7")
        self.lbl_mensaje_puntos = QtWidgets.QLabel(self.frame_4)
        self.lbl_mensaje_puntos.setGeometry(QtCore.QRect(20, 90, 241, 20))
        self.lbl_mensaje_puntos.setStyleSheet("font: 7pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_mensaje_puntos.setObjectName("lbl_mensaje_puntos")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(650, 30, 241, 121))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lbl_cifras_h = QtWidgets.QLabel(self.frame_5)
        self.lbl_cifras_h.setGeometry(QtCore.QRect(75, 10, 81, 61))
        self.lbl_cifras_h.setStyleSheet("font: 75 14pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.lbl_cifras_h.setObjectName("lbl_cifras_h")
        self.txtcifras = QtWidgets.QLineEdit(self.frame_5)
        self.txtcifras.setGeometry(QtCore.QRect(70, 60, 91, 21))
        self.txtcifras.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.txtcifras.setObjectName("txtcifras")
        self.lbl_mensaje_cifras_h = QtWidgets.QLabel(self.frame_5)
        self.lbl_mensaje_cifras_h.setGeometry(QtCore.QRect(20, 90, 201, 20))
        self.lbl_mensaje_cifras_h.setStyleSheet("font: 7pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_mensaje_cifras_h.setObjectName("lbl_mensaje_cifras_h")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(20, 10, 951, 161))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_2.setGeometry(QtCore.QRect(200, 10, 741, 141))
        self.tableWidget_2.setStyleSheet("background-color: rgb(246, 247, 251);\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btnAgregarFila = QtWidgets.QPushButton(self.frame_6)
        self.btnAgregarFila.setGeometry(QtCore.QRect(200, 25, 101, 51))
        self.btnAgregarFila.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 8pt \"SpaceMono Nerd Font\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 193, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(0, 136, 0);\n"
"}")
        self.btnAgregarFila.setObjectName("btnAgregarFila")
        self.btnEliminarFila = QtWidgets.QPushButton(self.frame_6)
        self.btnEliminarFila.setGeometry(QtCore.QRect(200, 80, 101, 50))
        self.btnEliminarFila.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 8pt \"SpaceMono Nerd Font\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 130, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(0, 95, 185);\n"
"}")
        self.btnEliminarFila.setObjectName("btnEliminarFila")
        self.lbl_aniadir = QtWidgets.QLabel(self.frame_6)
        self.lbl_aniadir.setGeometry(QtCore.QRect(12, 23, 50, 50))
        self.lbl_aniadir.setStyleSheet("background-image: url(:/images/images/Aniadir.png);\n"
"border-radius: 0px;")
        self.lbl_aniadir.setText("")
        self.lbl_aniadir.setObjectName("lbl_aniadir")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 50, 50))
        self.label_8.setStyleSheet("border-radius: 0px;\n"
"background-image: url(:/images/images/Eliminarr.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lblunidad = QtWidgets.QLabel(self.centralwidget)
        self.lblunidad.setGeometry(QtCore.QRect(440, 20, 171, 16))
        self.lblunidad.setObjectName("lblunidad")
        self.btnAgregarCol = QtWidgets.QPushButton(self.frame_6)
        self.btnAgregarCol.setGeometry(QtCore.QRect(70, 25, 117, 51))
        self.btnAgregarCol.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 8pt \"SpaceMono Nerd Font\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 193, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(0, 136, 0);\n"
"}")
        self.btnAgregarCol.setObjectName("btnAgregarCol")
        self.btnEliminarCol = QtWidgets.QPushButton(self.frame_6)
        self.btnEliminarCol.setGeometry(QtCore.QRect(70, 80, 117, 50))
        self.btnEliminarCol.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 8pt \"SpaceMono Nerd Font\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 130, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(0, 95, 185);\n"
"}")
        self.btnEliminarCol.setObjectName("btnEliminarCol")
        self.lbl_puntos_unidad3 = QtWidgets.QLabel(self.frame_6)
        self.lbl_puntos_unidad3.setGeometry(QtCore.QRect(20, 140, 281, 20))
        self.lbl_puntos_unidad3.setStyleSheet("font: 7pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_puntos_unidad3.setObjectName("lbl_puntos_unidad3")
        self.lbl_puntos_unidad3.raise_()
        self.btnAgregarFila.raise_()
        self.btnEliminarFila.raise_()
        self.lbl_aniadir.raise_()
        self.label_8.raise_()
        self.btnAgregarCol.raise_()
        self.btnEliminarCol.raise_()
        self.tableWidget_2.raise_()
        self.frame_hermite = QtWidgets.QFrame(self.frame)
        self.frame_hermite.setGeometry(QtCore.QRect(30, 180, 181, 80))
        self.frame_hermite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_hermite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_hermite.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_hermite.setObjectName("frame_hermite")
        self.lbl_punto_hermite = QtWidgets.QLabel(self.frame_hermite)
        self.lbl_punto_hermite.setGeometry(QtCore.QRect(30, 10, 121, 21))
        self.lbl_punto_hermite.setStyleSheet("font: 10pt \"SpaceMono Nerd Font\";\n"
"color: rgb(160, 160, 160);")
        self.lbl_punto_hermite.setObjectName("lbl_punto_hermite")
        self.txtHermitePunto = QtWidgets.QLineEdit(self.frame_hermite)
        self.txtHermitePunto.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.txtHermitePunto.setStyleSheet("border:0px;\n"
"background-image: url(:/images/images/barra2.png);")
        self.txtHermitePunto.setObjectName("txtHermitePunto")
        self.frame_trazadores = QtWidgets.QFrame(self.frame)
        self.frame_trazadores.setGeometry(QtCore.QRect(690, 180, 211, 81))
        self.frame_trazadores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_trazadores.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_trazadores.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_trazadores.setObjectName("frame_trazadores")
        self.cbmSplineGrado = QtWidgets.QComboBox(self.frame_trazadores)
        self.cbmSplineGrado.setGeometry(QtCore.QRect(30, 40, 151, 22))
        self.cbmSplineGrado.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(246, 247, 251);\n"
"font: 8pt \"SpaceMono Nerd Font\";\n"
"")
        self.cbmSplineGrado.setObjectName("cbmSplineGrado")
        self.cbmSplineGrado.addItem("")
        self.cbmSplineGrado.addItem("")
        self.cbmSplineGrado.addItem("")
        self.cbmSplineGrado.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame_trazadores)
        self.label_9.setGeometry(QtCore.QRect(40, 0, 141, 41))
        self.label_9.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";\n"
"color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.frame_6.raise_()
        self.btnResolverlo.raise_()
        self.btnLimpiar.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_hermite.raise_()
        self.frame_trazadores.raise_()
        self.cmbMetodos = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMetodos.setGeometry(QtCore.QRect(550, 10, 221, 22))
        self.cmbMetodos.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(246, 247, 251);\n"
"font: 8pt \"SpaceMono Nerd Font\";\n"
"")
        self.cmbMetodos.setObjectName("cmbMetodos")
        self.cmbMetodos.addItem("")
        self.btnUnidad1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidad1.setGeometry(QtCore.QRect(0, 120, 201, 51))
        self.btnUnidad1.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"background-image: url(:/images/images/unidad1.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/unidad1_bn.png);\n"
"\n"
"}")
        self.btnUnidad1.setText("")
        self.btnUnidad1.setObjectName("btnUnidad1")
        self.btnUnidad2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidad2.setGeometry(QtCore.QRect(0, 190, 201, 51))
        self.btnUnidad2.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"background-image: url(:/images/images/unidad2.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/unidad2_bn.png);\n"
"\n"
"}")
        self.btnUnidad2.setText("")
        self.btnUnidad2.setObjectName("btnUnidad2")
        self.btnUnidad3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidad3.setGeometry(QtCore.QRect(0, 260, 201, 51))
        self.btnUnidad3.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/unidad3.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/unidad3_bn.png);\n"
"\n"
"}")
        self.btnUnidad3.setText("")
        self.btnUnidad3.setObjectName("btnUnidad3")
        self.btnUnidad4 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidad4.setGeometry(QtCore.QRect(0, 330, 201, 51))
        self.btnUnidad4.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/unidad4.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    \n"
"    background-image: url(:/images/images/unidad4_bn.png);\n"
"\n"
"}")
        self.btnUnidad4.setText("")
        self.btnUnidad4.setObjectName("btnUnidad4")
        self.btnUnidad5 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidad5.setGeometry(QtCore.QRect(0, 400, 201, 51))
        self.btnUnidad5.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/unidad5.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/unidad5_bn.png);\n"
"\n"
"}")
        self.btnUnidad5.setText("")
        self.btnUnidad5.setObjectName("btnUnidad5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 201, 81))
        self.label_6.setStyleSheet("background-image: url(:/images/images/titulo.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(830, 10, 111, 17))
        self.radioButton.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(960, 10, 141, 17))
        self.radioButton_2.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.lbl_unidad_actual = QtWidgets.QLabel(self.centralwidget)
        self.lbl_unidad_actual.setGeometry(QtCore.QRect(230, 10, 271, 21))
        self.lbl_unidad_actual.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_unidad_actual.setObjectName("lbl_unidad_actual")
        self.lbl_radiobuttons = QtWidgets.QLabel(self.centralwidget)
        self.lbl_radiobuttons.setGeometry(QtCore.QRect(870, 30, 161, 21))
        self.lbl_radiobuttons.setStyleSheet("font: 8pt \"SpaceMono Nerd Font\";\n"
"color: rgb(255, 0, 4);")
        self.lbl_radiobuttons.setObjectName("lbl_radiobuttons")
        self.label_grafica = QtWidgets.QLabel(self.centralwidget)
        self.label_grafica.setGeometry(QtCore.QRect(10, 510, 64, 64))
        self.label_grafica.setStyleSheet("background-image: url(:/images/images/parabola.png);")
        self.label_grafica.setText("")
        self.label_grafica.setObjectName("label_grafica")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 510, 101, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    border:0px;\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(87, 85, 183);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 20px;\n"
"    \n"
"    background-color: rgb(71, 69, 150);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lbl_grafico_mensaje = QtWidgets.QLabel(self.centralwidget)
        self.lbl_grafico_mensaje.setGeometry(QtCore.QRect(10, 590, 201, 20))
        self.lbl_grafico_mensaje.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 8pt \"SpaceMono Nerd Font\";")
        self.lbl_grafico_mensaje.setObjectName("lbl_grafico_mensaje")
        self.lbl_radiobuttons.raise_()
        self.frame.raise_()
        self.cmbMetodos.raise_()
        self.btnUnidad1.raise_()
        self.btnUnidad2.raise_()
        self.btnUnidad3.raise_()
        self.btnUnidad4.raise_()
        self.btnUnidad5.raise_()
        self.label_6.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.lbl_unidad_actual.raise_()
        self.label_grafica.raise_()
        self.pushButton.raise_()
        self.lbl_grafico_mensaje.raise_()
        Analisis_Numerico.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Analisis_Numerico)
        self.statusbar.setObjectName("statusbar")
        Analisis_Numerico.setStatusBar(self.statusbar)

        self.retranslateUi(Analisis_Numerico)
        QtCore.QMetaObject.connectSlotsByName(Analisis_Numerico)

    def retranslateUi(self, Analisis_Numerico):
        _translate = QtCore.QCoreApplication.translate
        Analisis_Numerico.setWindowTitle(_translate("Analisis_Numerico", "Trabajo Final Analisis Numerico 2021"))
        self.btnResolverlo.setText(_translate("Analisis_Numerico", "Resolverlo"))
        self.btnLimpiar.setText(_translate("Analisis_Numerico", "Limpiar Campos"))
        self.label.setText(_translate("Analisis_Numerico", "Ingrese la Funcion "))
        self.lbl_mensaje_funcion.setText(_translate("Analisis_Numerico", "Mensaje Funcion"))
        self.label_2.setText(_translate("Analisis_Numerico", "Valores Iniciales"))
        self.label_3.setText(_translate("Analisis_Numerico", "X1"))
        self.label_4.setText(_translate("Analisis_Numerico", "X2"))
        self.label_7.setText(_translate("Analisis_Numerico", "X3"))
        self.lbl_mensaje_puntos.setText(_translate("Analisis_Numerico", "Mensaje puntos"))
        self.lbl_cifras_h.setText(_translate("Analisis_Numerico", "Cifras"))
        self.lbl_mensaje_cifras_h.setText(_translate("Analisis_Numerico", "Mensaje cifras"))
        self.btnAgregarFila.setText(_translate("Analisis_Numerico", "Añadir Fila"))
        self.btnEliminarFila.setText(_translate("Analisis_Numerico", "Eliminar Fila"))
        self.btnAgregarCol.setText(_translate("Analisis_Numerico", "Añadir Columna"))
        self.btnEliminarCol.setText(_translate("Analisis_Numerico", "Eliminar Columna"))
        self.lbl_puntos_unidad3.setText(_translate("Analisis_Numerico", "Mensaje puntos unidad 3 "))
        self.lbl_punto_hermite.setText(_translate("Analisis_Numerico", "Punto a Evaluar"))
        self.cbmSplineGrado.setItemText(0, _translate("Analisis_Numerico", "Grado Cero"))
        self.cbmSplineGrado.setItemText(1, _translate("Analisis_Numerico", "Grado Uno"))
        self.cbmSplineGrado.setItemText(2, _translate("Analisis_Numerico", "Grado Dos"))
        self.cbmSplineGrado.setItemText(3, _translate("Analisis_Numerico", "Grado Tres"))
        self.label_9.setText(_translate("Analisis_Numerico", "Seleccione el grado\n"
"  Funcion Spline"))
        self.cmbMetodos.setCurrentText(_translate("Analisis_Numerico", "> Seleccione una Unidad <"))
        self.cmbMetodos.setItemText(0, _translate("Analisis_Numerico", "> Seleccione una Unidad <"))
        self.radioButton.setText(_translate("Analisis_Numerico", "Ver polinomio"))
        self.radioButton_2.setText(_translate("Analisis_Numerico", "No ver polinomio"))
        self.lbl_unidad_actual.setText(_translate("Analisis_Numerico", "Unidad Actual # ninguna seleccionada"))
        self.lbl_radiobuttons.setText(_translate("Analisis_Numerico", "*Seleccione una acción"))
        self.pushButton.setText(_translate("Analisis_Numerico", "Realizar \n"
" Grafico"))
        self.lbl_grafico_mensaje.setText(_translate("Analisis_Numerico", "*Funcion incorrecta"))
        
        #Asignamos funcion que filtra los objetos respecto al item seleccionado en cmb
        self.cmbMetodos.activated[str].connect(self.Filtrar_Objects)
        #Asignamos funciones a los botones.
        self.btnResolverlo.clicked.connect(self.Resolverlo)
        self.btnLimpiar.clicked.connect(self.Limpiar_Objects)
        self.btnAgregarCol.clicked.connect(self.agregarColumna)
        self.btnEliminarCol.clicked.connect(self.eliminarColumna)
        self.pushButton.clicked.connect(self.graficar)
        #Botones unidades.
        self.btnUnidad1.clicked.connect(lambda: self.unidades(0))
        self.btnUnidad1.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad2.clicked.connect(lambda: self.unidades(1))
        self.btnUnidad2.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad3.clicked.connect(lambda: self.unidades(2))
        self.btnUnidad3.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad4.clicked.connect(lambda: self.unidades(3))
        self.btnUnidad4.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        #self.btnUnidad5.clicked.connect(self.Filtrar_llenado_cmbMetodos)

        #Ocultamos todos los componetes para filtrarlos con los btn de las unidades.
        self.frame.setVisible(False)
        self.frame_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.frame_hermite.setVisible(False)
        self.frame_trazadores.setVisible(False)
        self.lbl_grafico_mensaje.setVisible(False)
        self.lbl_mensaje_puntos.setVisible(False)
        self.lbl_mensaje_funcion.setVisible(False)
        self.lbl_puntos_unidad3.setVisible(False)
        self.lbl_mensaje_cifras_h.setVisible(False)
        self.lbl_radiobuttons.setVisible(False)

        #Validamos que solo acepte numeros y signos NO letras.
        
        self.txtX1.setValidator(QtGui.QDoubleValidator())
        self.txtX2.setValidator(QtGui.QDoubleValidator())
        self.txtX2_2.setValidator(QtGui.QDoubleValidator())
        self.txtcifras.setValidator(QtGui.QDoubleValidator())

        #label de apoyo para saber en que unidad nos encontramos
        self.lblunidad.setText(_translate("MainWindow", "0"))
        self.lblunidad.setVisible(False)


    def unidades(self, cual):
        self.lblunidad.setText(str(cual))
        cual=int(cual+1)
        self.lbl_unidad_actual.setText(f"Unidad Actual # {str(cual)}")

    def Filtrar_llenado_cmbMetodos(self):
        
        cual = int(self.lblunidad.text())
        self.frame.setVisible(True)
        self.frame_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        

        if cual == 0:  # Metodos de la primera unidad

            self.cmbMetodos.setGeometry(QtCore.QRect(550, 10, 221, 22))
            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.cmbMetodos.clear()

            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")

            self.cmbMetodos.setItemText(0, "> Seleccione un metodo <")
            self.cmbMetodos.setItemText(1,  "ln(e+x)")
            self.cmbMetodos.setItemText(2,  "e^(x^2)")
            self.cmbMetodos.setItemText(3,  "sen(x)")
            self.cmbMetodos.setItemText(4,  "cos(x)")
            self.cmbMetodos.setItemText(5,  "e^x")
            self.cmbMetodos.setItemText(6,  "sh(x)")
            self.cmbMetodos.setItemText(7,  "ch(x)")
            self.cmbMetodos.setItemText(8,  "arcsen(x)")
            self.cmbMetodos.setItemText(9,  "ln(1+x)")
            self.cmbMetodos.setItemText(10,  "1/(1+x^2)")
            self.cmbMetodos.setItemText(11,  "arctg(x)")
            self.cmbMetodos.setCurrentIndex(0)

            self.cmbMetodos.setVisible(False)
            self.frame_2.setVisible(False)
            self.label_4.setVisible(False)
            self.label_7.setVisible(False)
            self.txtX2.setVisible(False)
            self.txtX2_2.setVisible(False)
            self.frame_6.setVisible(False)
            self.frame_3.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)


          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.cmbMetodos.setVisible(True)
            


        elif cual == 1:  # Metodos de la segunda unidad
            self.cmbMetodos.setGeometry(QtCore.QRect(550, 10, 221, 22))
            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.cmbMetodos.clear()
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")

            self.cmbMetodos.setItemText(0,  "> Seleccione un metodo <")
            self.cmbMetodos.setItemText(1,  "Biseccion")
            self.cmbMetodos.setItemText(2,  "Falsa Posicion")
            self.cmbMetodos.setItemText(3,  "Punto Fijo")
            self.cmbMetodos.setItemText(4,  "Newton Raphson")
            self.cmbMetodos.setItemText(5,  "Newton Raphson Mejorado")
            self.cmbMetodos.setItemText(6,  "Secante")
            self.cmbMetodos.setItemText(7,  "Ceros de polinomios")
            self.cmbMetodos.setItemText(8,  "Horner")
            self.cmbMetodos.setItemText(9,  "Muller")
            self.cmbMetodos.setItemText(10, "Bairstown")

            self.cmbMetodos.setCurrentIndex(0)
            self.cmbMetodos.setVisible(False)
            self.frame_3.setVisible(False)
            self.frame_4.setVisible(False)
            self.frame_5.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)


          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.cmbMetodos.setVisible(True)
            

        elif cual == 2:  # Metodos de la unidad 3
            self.cmbMetodos.setGeometry(QtCore.QRect(550, 10, 221, 22))

            self.cmbMetodos.clear()
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")

            self.cmbMetodos.setItemText(0,  "> Seleccione un metodo <")
            self.cmbMetodos.setItemText(1,  "Interpolación Lineal")
            self.cmbMetodos.setItemText(2,  "Interpolación cuadratica")
            self.cmbMetodos.setItemText(3,  "Interpolación de lagrange")
            self.cmbMetodos.setItemText(4,  "Interpolación de Newton")
            self.cmbMetodos.setItemText(5,  "Diferencias Divididas")
            self.cmbMetodos.setItemText(6,  "Trazadores cubicos")
            self.cmbMetodos.setItemText(7,  "Interpolación de Hermite")

            # Mostramos el comboBox
            self.cmbMetodos.setVisible(True)
            self.cmbMetodos.setCurrentIndex(0)
            # Ocultamos todo
            self.frame_3.setVisible(False)
            self.frame_4.setVisible(False)
            self.frame_5.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)

        elif cual == 3: #metodos de la unidad 4
            self.cmbMetodos.setGeometry(QtCore.QRect(550, 10, 221, 22))
            
            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.cmbMetodos.clear()

            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")
            self.cmbMetodos.addItem("")

            self.cmbMetodos.setItemText(0, "> Seleccione un metodo <")
            self.cmbMetodos.setItemText(1,  "- Dif Numerica Hacia adelante")
            self.cmbMetodos.setItemText(2,  "- Dif Numerica Hacia atras")
            self.cmbMetodos.setItemText(3,  "- Dif Numerica Centrada")
            self.cmbMetodos.setItemText(4,  "- Dif Numerica Tres puntos")
            self.cmbMetodos.setItemText(5,  "- Dif Numerica Cinco puntos")
            self.cmbMetodos.setItemText(6,  "- Orden Superior Adelante")
            self.cmbMetodos.setItemText(7,  "- Orden Superior Atras")
            self.cmbMetodos.setItemText(8, "- Orden Superior Centrales")
            self.cmbMetodos.setItemText(9, "- Richardson")
            self.cmbMetodos.setItemText(10, "- Integracion Numerica")
            self.cmbMetodos.setItemText(11, "- Trapecio simple")
            self.cmbMetodos.setItemText(12, "- Trapecio compuesto")
            self.cmbMetodos.setItemText(13, "- Trapecio para integrales dobles y triples")
            self.cmbMetodos.setItemText(14, "- Simpson un tercio simple")
            self.cmbMetodos.setItemText(15, "- Simpson un tercio compuesta")
            self.cmbMetodos.setItemText(16, "- Simpson tres octavos simple")
            self.cmbMetodos.setItemText(17, "- Simpson tres octavos compuesta")
            self.cmbMetodos.setItemText(18, "- Rosemberg")
            self.cmbMetodos.setItemText(19, "- Cuadratura Gaussiana")
            self.cmbMetodos.setItemText(20, "- Simpson un tercio adaptativo")
            self.cmbMetodos.setItemText(21, "- Boole")
            
            # Mostramos el comboBox
            self.cmbMetodos.setVisible(True)
            self.cmbMetodos.setCurrentIndex(0)
            # Ocultamos todo
            self.frame_3.setVisible(False)
            self.frame_4.setVisible(False)
            self.frame_5.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)

    def Aplicar_Ajustes_Tabla_Unidad_3(self, columnas):
        self.frame_6.setVisible(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(55)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_2.setColumnCount(columnas)
        self.tableWidget_2.setRowCount(2)
        self.radioButton.setVisible(True)
        self.radioButton_2.setVisible(True)


        for x in range(0, 2):
            for y in range(0, 3):
                if y == 0 and x == 0:
                    salida = "    X"
                    self.tableWidget_2.setItem(
                        x, y, QtWidgets.QTableWidgetItem(salida))
                    self.tableWidget_2.setColumnWidth(y, 8)
                elif y == 0 and x == 1:
                    salida = "    Y"
                    self.tableWidget_2.setItem(
                        x, y, QtWidgets.QTableWidgetItem(salida))
                    self.tableWidget_2.setColumnWidth(y, 8)
                else:
                    salida = ""
                    self.tableWidget_2.setItem(
                        x, y, QtWidgets.QTableWidgetItem(salida))

        self.tableWidget_2.setVisible(True)

    def Filtrar_Objects(self):

        queMetodo = self.cmbMetodos.currentIndex()
        queUnidad = int(self.lblunidad.text())
        

        if queUnidad == 0: #Se refiere a la unidad 1

            self.frame_6.setVisible(False)
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)

            # <---- dejamos solo los componentes que usa la unidad 1 -------->
            
            
            self.frame_4.setVisible(True)
            self.frame_5.setVisible(True)
            self.btnResolverlo.setVisible(True)
            self.btnLimpiar.setVisible(True)
                

            # <-------- Ocultamos lo demas ------------->
            self.frame_3.setVisible(False)
            self.label_4.setVisible(False)
            self.label_7.setVisible(False)
            self.txtX2.setVisible(False)
            self.txtX2_2.setVisible(False)


        elif queUnidad == 1:
            
            
            self.frame_6.setVisible(False)
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)

            if queMetodo >= 1 and queMetodo <= 2:

                # <---- dejamos solo los componentes que usa metodo biseccion, falsa posicion y secante -->
                
                self.frame_3.setVisible(True)
                self.frame_4.setVisible(True)
                self.frame_5.setVisible(True)
                self.label_4.setVisible(True)
                self.txtX2.setVisible(True)
                self.btnResolverlo.setVisible(True)
                self.btnLimpiar.setVisible(True)
                

                # <-------- Ocultamos lo demas ------------->
                self.txtX2_2.setVisible(False)
                self.label_7.setVisible(False)

            elif queMetodo >= 3 and queMetodo <= 6:

                # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
                self.frame_3.setVisible(True)
                self.frame_4.setVisible(True)
                self.frame_5.setVisible(True)
                self.btnResolverlo.setVisible(True)
                self.btnLimpiar.setVisible(True)
                
                # <-------- Ocultamos lo demas ------------->
                self.txtX2_2.setVisible(False)
                self.txtX2.setVisible(False)
                self.label_4.setVisible(False)
                self.label_7.setVisible(False)

            elif queMetodo >= 7 and queMetodo <= 8:
                # <---- dejamos solo los componentes que usa metodo de cero de polinomios --->
                self.frame_3.setVisible(True)
                self.frame_5.setVisible(True)
                self.btnResolverlo.setVisible(True)
                self.btnLimpiar.setVisible(True)
                # <-------- ocultamos lo demas ---------->
                self.frame_4.setVisible(False)
                self.frame_5.setVisible(False)

            elif queMetodo == 9:

                # <---- dejamos solo los componentes que usa metodo muller -->
                self.frame_3.setVisible(True)
                self.frame_4.setVisible(True)
                self.frame_5.setVisible(True)
                self.label_4.setVisible(True)
                self.txtX2.setVisible(True)
                self.label_7.setVisible(True)
                self.txtX2_2.setVisible(True)

            elif queMetodo == 10:

                # <---- dejamos solo los componentes que usa metodo baristonw -->
                self.frame_3.setVisible(True)
                self.frame_4.setVisible(True)
                

                # <-------- ocultamos lo demas ---------->

                self.frame_5.setVisible(False)
                self.txtX2_2.setVisible(False)
                self.label_7.setVisible(False)

        elif queUnidad == 2:  # Configuramos la tabla para unidad 3.

            self.frame_hermite.setVisible(False)
            self.frame_trazadores.setVisible(False)

            global Numero_Filas_Columnas

            # Deseleccionamos los radio button

            self.radioButton.setAutoExclusive(False)
            self.radioButton.setChecked(False)
            self.radioButton.setAutoExclusive(True)
            self.radioButton_2.setAutoExclusive(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_2.setAutoExclusive(True)

            if queMetodo == 1:#Lineal
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 2:#Cuadratica
                Numero_Filas_Columnas = 4
                self.Aplicar_Ajustes_Tabla_Unidad_3(5)
            elif queMetodo == 3:#Lagrange
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 4:#Newton
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 5:#Dif dividida
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 6:#Spline
                Numero_Filas_Columnas = 4
                self.Aplicar_Ajustes_Tabla_Unidad_3(5)
            elif queMetodo == 7:#Hermite
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)

    def Limpiar_Objects(self, MainWindow):
        
        self.txtfuncion.setText("")
        self.txtX1.setText("")
        self.txtX2.setText("")
        self.txtX2_2.setText("")
        self.txtcifras.setText("")
        self.cmbMetodos.setCurrentIndex(0)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget_2.clear()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoExclusive(True)

    def graficar(self, MainWindow):
        Es_Unidad_dos = self.cmbMetodos.currentIndex()
        if Es_Unidad_dos==1: #Si puede graficar.Es_Unidad_dos
            try:
                funcion = str(self.txtfuncion.text())
                Graficar = ''
                title = 'Funcion: '+str(self.txtfuncion.text())

                for i in range(0, len(funcion)):
                    if funcion[i] == 'e':
                        if funcion[i+1] == '^':
                            Graficar += str(cmath.e)
                        else:
                            Graficar += funcion[i]
                    else:
                        Graficar += funcion[i]
                grafica = plot((Graficar, (x, -100, 100)), box_background='blue', show=False, line_color='#96ADEA',ylabel='Y', xlabel='X', title=title, size=(6, 5), xlim=(-25, 25), ylim=(-25, 25))
                grafica.show()
            except:
                self.lbl_grafico_mensaje.setText("*Ocurrio un problema :c")
                self.lbl_grafico_mensaje.setVisible(True)
            finally:
                self.lbl_grafico_mensaje.setVisible(False) 

        else:
            self.lbl_grafico_mensaje.setText("*disponible en unidad 2")
            self.lbl_grafico_mensaje.setVisible(True)

    def agregarColumna(self):
        global Numero_Filas_Columnas
        metodo = self.cmbMetodos.currentIndex()

        if metodo == 0:
            mesaje=("Seleccione un metodo primero ")
            self.lbl_puntos_unidad3.setText(mesaje)
            self.lbl_puntos_unidad3.setVisible(True)
        elif metodo == 1:
            mesaje=("Solamente se puede trabajar con 2 puntos")
            self.lbl_puntos_unidad3.setText(mesaje)
            self.lbl_puntos_unidad3.setVisible(True)
        else:
            if Numero_Filas_Columnas == 13:
                mesaje=("Maximo numero de columnas alcanzado")
                self.lbl_puntos_unidad3.setText(mesaje)
                self.lbl_puntos_unidad3.setVisible(True)
            else:
                self.tableWidget_2.insertColumn(Numero_Filas_Columnas+1)
                Numero_Filas_Columnas += 1
                self.lbl_puntos_unidad3.setVisible(False)

    def eliminarColumna(self):
        global Numero_Filas_Columnas
        metodo = self.cmbMetodos.currentIndex()

        if metodo == 1:  # lineal
            if Numero_Filas_Columnas == 3:
                mesaje=("Se necesitan al menos 2 puntos")
                self.lbl_puntos_unidad3.setText(mesaje)
                self.lbl_puntos_unidad3.setVisible(True)
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1
                self.lbl_puntos_unidad3.setVisible(False)

        elif metodo == 2:  # Cuadratica
            if Numero_Filas_Columnas == 4:
                mesaje=("Se necesitan al menos 3 puntos")
                self.lbl_puntos_unidad3.setText(mesaje)
                self.lbl_puntos_unidad3.setVisible(True)
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1
                self.lbl_puntos_unidad3.setVisible(False)

        elif metodo == 3:  # Lagrange
            if Numero_Filas_Columnas == 3:
                mesaje=("Se necesitan al menos 2 puntos")
                self.lbl_puntos_unidad3.setText(mesaje)
                self.lbl_puntos_unidad3.setVisible(True)
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1
                self.lbl_puntos_unidad3.setVisible(False)

        elif metodo == 4:  # Newton
            if Numero_Filas_Columnas == 3:
                mesaje=("Se necesitan al menos 2 puntos")
                self.lbl_puntos_unidad3.setText(mesaje)
                self.lbl_puntos_unidad3.setVisible(True)
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas-1
                self.lbl_puntos_unidad3.setVisible(False)

    def Validar_Datos_en_Formulario(self, MainWindow, queMetodo, funcionTXT, X1, X2,X3, cifTXT):
        # <---- Validamos que sean numeros ------->
        x1 = funciones.Validar_Valores_Iniciales(X1)
        x2 = funciones.Validar_Valores_Iniciales(X2)
        x3 = funciones.Validar_Valores_Iniciales(X3)
        control_acceso = False

        cuantasVariables = 0

        if queMetodo == 1 or queMetodo == 2 or queMetodo == 6:
            cuantasVariables = 2
        elif queMetodo == 3 or queMetodo == 4 or queMetodo == 5:
            cuantasVariables = 1
        elif queMetodo == 7:
            self.Tabla_Unidad_2(MainWindow, 7, 0, 0, 0, 0)

        if cuantasVariables == 2:
            if x1 == False or x2 == False:
                mesaje=("Los valores iniciales son incorrectos")
                self.lbl_mensaje_puntos.setText(mesaje)
                self.lbl_mensaje_puntos.setVisible(True)
            else:
                self.lbl_mensaje_puntos.setVisible(False)
                try:
                    funcion = funciones.Sustituir_y_Evaluar_Funcion(funcionTXT, 1, 0, 0)
                    control_acceso = True
                except:
                    control_acceso = False
                if control_acceso == False:
                    mesaje=("La funcion no es valida")
                    self.lbl_mensaje_funcion.setText(mesaje)
                    self.lbl_mensaje_funcion.setVisible(True)
                else:
                    self.lbl_mensaje_funcion.setVisible(False)
                    control_cifras = funciones.Validar_Cifras_Significativas(cifTXT)
                    if control_cifras == False:
                       mesaje=("Cifras incorrectas")
                       self.lbl_mensaje_cifras_h.setText(mesaje)
                       self.lbl_mensaje_cifras_h.setVisible(True)
                    else:
                        self.lbl_mensaje_cifras_h.setVisible(False)
                        if queMetodo == 1:  # Biseccion
                            self.Tabla_Unidad_2(MainWindow, 1, x1,
                                            x2, funcionTXT, control_cifras)
                        elif queMetodo == 2:  # Falsa Posicion
                            self.Tabla_Unidad_2(MainWindow, 2, x1,
                                            x2, funcionTXT, control_cifras)
                        elif queMetodo == 6:  # secante
                            self.Tabla_Unidad_2(MainWindow, 6, x1,
                                            x2, funcionTXT, control_cifras)
        if cuantasVariables == 1:
            if x1 == False :
                mesaje=("Los valores iniciales son incorrectos")
                self.lbl_mensaje_puntos.setText(mesaje)
                self.lbl_mensaje_puntos.setVisible(True)
            else:
                self.lbl_mensaje_puntos.setVisible(False)
                try:
                    funcion = funciones.Sustituir_y_Evaluar_Funcion(funcionTXT, 1, 0, 0)
                    control_acceso = True
                except:
                    control_acceso = False
                if control_acceso == False:
                    mesaje=("La funcion no es valida")
                    self.lbl_mensaje_funcion.setText(mesaje)
                    self.lbl_mensaje_funcion.setVisible(True)
                else:
                    self.lbl_mensaje_funcion.setVisible(False)    
                    control_cifras = funciones.Validar_Cifras_Significativas(cifTXT)
                    if control_cifras == False:
                        mesaje=("Cifras incorrectas")
                        self.lbl_mensaje_cifras_h.setText(mesaje)
                        self.lbl_mensaje_cifras_h.setVisible(True)
                    else:
                        self.lbl_mensaje_cifras_h.setVisible(False)
                        if queMetodo == 3:
                            # Falsa posicion
                            self.Tabla_Unidad_2(MainWindow, 3, x1,
                                            x2, funcionTXT, control_cifras)
                        elif queMetodo == 4:
                            self.Tabla_Unidad_2(MainWindow, 4, x1,
                                            x2, funcionTXT, control_cifras)  # newton
                        elif queMetodo == 5:
                            # newton mejorado
                            self.Tabla_Unidad_2(MainWindow, 5, x1,
                                            x2, funcionTXT, control_cifras)

    def Resolverlo(self, MainWindow):

        unidad = int(self.lblunidad.text())
        metodo = self.cmbMetodos.currentIndex()

        if unidad == 0:
            print("Aún falta esta parte :c")

        elif unidad == 1:  # Parte unidad 2
            if metodo == 1:  # Biseccion
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 2:  # Falsa posicion
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 3:  # Punto fijo
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 4:  # Newton
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 5:  # Newton mejorado
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 6:  # secante
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(
                ), self.txtX1.text(), self.txtX2.text(), self.txtcifras.text())
            elif metodo == 7:  # cero polinomios
                self.Validar_Datos_en_Formulario(MainWindow, metodo, self.txtfuncion.text(), 0, 0, 0)
            elif metodo == 8:  # Horner
                self.Tabla_Unidad_2(MainWindow, metodo, self.txtfuncion.text(), 0, 0, 0)
            elif metodo == 9:  # Muller
                self.Tabla_Unidad_2(MainWindow, metodo, self.txtfuncion.text(), 0, 0, 0)
            elif metodo == 10:  # Baristow
                self.Tabla_Unidad_2(MainWindow, metodo, self.txtfuncion.text(), 0, 0, 0)

        elif unidad == 2: #Metodos de la unidad 3

            if metodo == 1:# lineal
                self.Validar_Puntos_Tabla_Unidad_3(1)
            elif metodo == 2:# cuadratica
                self.Validar_Puntos_Tabla_Unidad_3(2)
            elif metodo == 3:# lagrange
                self.Validar_Puntos_Tabla_Unidad_3(3)
            elif metodo == 4:# newton
                self.Validar_Puntos_Tabla_Unidad_3(4)
            elif metodo == 5:# hermite
                self.Validar_Puntos_Tabla_Unidad_3(5)
            elif metodo == 6:# Trazadores Cubicos
                self.Validar_Puntos_Tabla_Unidad_3(6)

    def Tabla_Unidad_2(self, MainWindow, metodo, x1, x2, x3, funcion, control_cifras):
        
        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(rows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalScrollMode()
        
        unidad = int(self.lblunidad.text())
        if unidad == 1:
            if metodo == 1:
                Listado_Resultante = unidad_dos.metodoBiseccion(x1, x2, funcion, control_cifras)
            elif metodo == 2:
                Listado_Resultante = unidad_dos.metodoFalsaPosicion(x1, x2, funcion, control_cifras)
            elif metodo == 3:
                Listado_Resultante = unidad_dos.metodoPuntoFijo(x1, funcion, control_cifras)
            elif metodo == 4:
                Listado_Resultante = unidad_dos.metodoNewtonRaphson(x1, funcion, control_cifras)
            elif metodo == 5:
                Listado_Resultante = unidad_dos.metodoNewtonRaphsonMejorado(x1, funcion, control_cifras)
            elif metodo == 6:
                Listado_Resultante = unidad_dos.metodoSecante(x1, x2, funcion, control_cifras)

            elif metodo == 7:  # Metodo para crear tabla de cero de polinomios
                listaCoeficientes = funciones.Obtener_Coeficientes(self.txtfuncion.text())
                largo = len(listaCoeficientes)
                if largo > 5:
                    mesaje=(f"Funcion {funcion} mayor a cuartica")
                    self.lbl_mensaje_funcion.setText(mesaje)
                    self.lbl_mensaje_funcion.setVisible(True)
                else:
                    self.lbl_mensaje_funcion.setVisible(False)    
                    if largo == 5:
                        a = listaCoeficientes[4]
                        b = listaCoeficientes[3]
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        Listado_Resultante = unidad_dos.factorizar(a, b, c, d, e)
                    elif largo == 4:
                        a = 0
                        b = listaCoeficientes[3]
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        Listado_Resultante = unidad_dos.factorizar(a, b, c, d, e)
                    elif largo == 3:
                        a = 0
                        b = 0
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        Listado_Resultante = unidad_dos.factorizar(a, b, c, d, e)
                    elif largo == 2:
                        a = 0
                        b = 0
                        c = 0
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        Listado_Resultante = unidad_dos.factorizar(a, b, c, d, e)
                    elif largo == 1:
                        mesaje=(f"Esta {funcion} no es una funcion ")
                        self.lbl_mensaje_funcion.setText(mesaje)
                        self.lbl_mensaje_funcion.setVisible(True)
                    # Creando la tabla para cero de polinomios
                    if largo <= 5:
                        columns = len(Listado_Resultante)
                        rows = 2
                        tamanioColumnas = int(930/columns)
                        #Reseteamos parametros de la tabla
                        self.tableWidget.setColumnCount(columns)
                        self.tableWidget.setRowCount(rows)
                        self.tableWidget.verticalHeader().setVisible(False)
                        self.tableWidget.horizontalHeader().setVisible(False)                    

                        for row in range(rows):
                            for column in range(columns):
                                if row == 0:
                                    salida = "raiz #"+str(column+1)
                                    self.tableWidget.setItem(
                                        row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                    self.tableWidget.setColumnWidth(
                                        column, tamanioColumnas)
                                else:
                                    salida = str(Listado_Resultante[column])
                                    self.tableWidget.setItem(
                                        row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                    self.tableWidget.setColumnWidth(
                                        column, tamanioColumnas)

            elif metodo == 8:  # Metodo para crear tabla de horner
                lista = funciones.Obtener_Coeficientes(self.txtfuncion.text())
                print(lista)
                Listado_Resultante = unidad_dos.metodoHorner(lista, float(
                    self.txtX1.text()), float(self.txtcifras.text()))

                rows = len(Listado_Resultante)
                columns = len(Listado_Resultante[0])

                tamanioColumnas = int(930/columns)

                

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = Listado_Resultante[row][column]
                            self.tableWidget.setItem(
                                row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(
                                column, tamanioColumnas)
                        else:
                            if column == 0:
                                salida = "%.0f" % (Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

            elif metodo == 9:  # Metodo para crear tabla de müller
                # Creamos la lista completa con todas las iteraciones
                # Metodo muller me devuelve todas las iteraciones
                Listado_Resultante = unidad_dos.metodoMuller(self.txtfuncion.text(), self.txtX1.text(
                ), self.txtX2.text(), self.txtX2_2.text(), self.txtcifras.text())

                rows = len(Listado_Resultante)  # Capturamos cuantas filas hay
                columns = len(Listado_Resultante[0])  # Capturamos cuantas columnas hay

                # dividimos el ancho de la tabla entre las columnas

                

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = Listado_Resultante[row][column]
                            # Asignamos los valores del metodo en las casillas de la tabla
                            self.tableWidget.setItem(
                                row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(
                                column, tamanioColumnas)

                            # Asignamos el tamaño que necesita la columna
                        else:
                            if column == 0:
                                salida = "%.0f" % (Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

            elif metodo == 10:  # metodo para crear tabla de bairstown

                # Creamos una lista con los coeficientes de la funcion ingresada por el usuario y la ordenamos de mayor a menor
                coeficientes = funciones.Obtener_Coeficientes(self.txtfuncion.text())
                coeficientes.reverse()

                Listado_Resultante = unidad_dos.metodoBairstow(
                    coeficientes, self.txtX1.text(), self.txtX2.text(), 3)

                columns = len(Listado_Resultante)
                self.tableWidget.setRowCount(2)
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)
                tamanioColumnas = 0
                listaTamanio = []
                contadorTamanio = 0
                for x in range(0, columns):
                    listaTamanio.append(len(str(Listado_Resultante[x]))*7)
                    contadorTamanio += len(str(Listado_Resultante[x]))*7

                listaTamanio.sort()

               

                for row in range(0, 2):
                    for column in range(0, columns):
                        if row == 0:
                            salida = "Raiz #"+str(column+1)
                            self.tableWidget.setItem(
                                row, column, QtWidgets.QTableWidgetItem(salida))
                            if contadorTamanio < 930:
                                tamanioColumnas = float(
                                    listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                            else:
                                tamanioColumnas = len(str(Listado_Resultante[column]))*7
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                        else:
                            salida = str(Listado_Resultante[column])
                            self.tableWidget.setItem(
                                row, column, QtWidgets.QTableWidgetItem(salida))
                            if contadorTamanio < 930:
                                tamanioColumnas = float(
                                    listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

                            else:
                                tamanioColumnas = len(str(Listado_Resultante[column]))*7
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

            if metodo >= 1 and metodo <= 6:  # Imprime de biseccion hasta secante
                self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
                rows = len(Listado_Resultante)
                columns = len(Listado_Resultante[0])
                tamanioColumnas = int(930/columns)-3

                

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = Listado_Resultante[row][column]
                            self.tableWidget.setItem(
                                row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.item(row, column).setBackground(
                                QtGui.QColor(11, 133, 192))
                            self.tableWidget.setColumnWidth(
                                column, tamanioColumnas)
                        else:
                            if column == 0:
                                salida = (Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(Listado_Resultante[row][column])
                                self.tableWidget.setItem(
                                    row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

    def Validar_Puntos_Tabla_Unidad_3(self,metodo):
        global Numero_Filas_Columnas, Numero_filas_Hermite
        listaX = []
        listaY = []
        Puntos_Validados = []
        Sub_listaX = []
        Sub_listaY = []
        Lista_Hermite = []
        
        if metodo == 5:

            print(Numero_Filas_Columnas,Numero_filas_Hermite)
            #Agregamos los puntos a listas separadas 
            for x in range(0,Numero_Filas_Columnas+1):
                listaX = []
                Sub_listaX = []
                for j in range(1,Numero_filas_Hermite+1):
                    try:
                        listaX.append(self.tableWidget_2.item(j,x).text())
                    except:
                        listaX.append('')
                for x in listaX:
                    if x == '':
                        Sub_listaX.append(x)
                    else:
                        Sub_listaX.append(float(x))
                
                Lista_Hermite.append(Sub_listaX)

            self.Tabla_Unidad_3(5,Lista_Hermite,self.lineEdit_6.text()) 

        elif metodo == 6:
             #Agregamos los puntos a listas separadas 
            for x in range(0,2):
                for y in range(1,Numero_Filas_Columnas+1):
                    if x == 0:
                        listaX.append(self.tableWidget_2.item(x,y).text())
                    elif x == 1:
                        listaY.append(self.tableWidget_2.item(x,y).text())
                
            for i in listaX:
                Sub_listaX.append(float(i))
            
            for i in listaY:
                Sub_listaY.append(float(i))

            Puntos_Validados = [Sub_listaX,Sub_listaY]
            self.Tabla_Unidad_3(6,Puntos_Validados,self.lineEdit_6.text())
          
        else:
            #Agregamos los puntos a listas separadas 
            for x in range(0,2):
                for y in range(0,Numero_Filas_Columnas+1):
                    if x == 0:
                        if y != 0:
                            listaX.append(self.tableWidget_2.item(x,y).text())
                    elif x == 1:
                        if y != 0:
                            try:
                                listaY.append(self.tableWidget_2.item(x,y).text())
                            except:
                                listaY.append('?')
            
            #Buscamos la posicion donde se desea interpolar
            for i in range(0,len(listaY)):
                    if listaY[i] == '?':
                        macht = i

            #Lineal
            if metodo == 1: 

                lienal_Punto = []
                lienal_Punto.append(listaX[macht-1])#X0
                lienal_Punto.append(listaY[macht-1])#Y0
                lienal_Punto.append(listaX[macht+1])#X1
                lienal_Punto.append(listaY[macht+1])#Y1

                Puntos_Validados = []
                Puntos_Validados.append(lienal_Punto)

                self.Tabla_Unidad_3(1,Puntos_Validados,float(listaX[macht]))

            #Cuadratica
            elif metodo == 2:

                #Creamos las listas que serian los pares x,y
                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                Sub_listaX.append(float(listaX[i]))
                                Sub_listaY.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            Sub_listaX.append(float(listaX[i]))
                            Sub_listaY.append(float(valor))
                
                Puntos_Validados = []
                Puntos_Validados.append(Sub_listaX)
                Puntos_Validados.append(Sub_listaY)

                self.Tabla_Unidad_3(2,Puntos_Validados,listaX[macht])

            #lagrange
            elif metodo == 3:

                #Encontramos los puntos x,y
                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                Sub_listaX.append(float(listaX[i]))
                                Sub_listaY.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            Sub_listaX.append(float(listaX[i]))
                            Sub_listaY.append(float(valor))

                Puntos_Validados = []
                Puntos_Validados.append(Sub_listaX)
                Puntos_Validados.append(Sub_listaY)

                self.Tabla_Unidad_3(3,Puntos_Validados,float(listaX[macht]))

            #Newton
            elif metodo == 4:

                #Encontramos los pares x,y
                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                Sub_listaX.append(float(listaX[i]))
                                Sub_listaY.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            Sub_listaX.append(float(listaX[i]))
                            Sub_listaY.append(float(valor))
                    

                Puntos_Validados = []
                Puntos_Validados.append(Sub_listaX)
                Puntos_Validados.append(Sub_listaY)

                self.Tabla_Unidad_3(4,Puntos_Validados,float(listaX[macht]))

    def Tabla_Unidad_3(self, metodo, Puntos_Validados, valor):
        self.lbl_radiobuttons.setVisible(True)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

        if metodo == 1:  # Interpolacion Lineal

            Listado_Resultante = unidad_tres.interpolacionLineal(Puntos_Validados[0], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            # Verificamos si solo mostraremos el polinomio o el valor
            if self.radioButton.isChecked():
                self.lbl_radiobuttons.setVisible(False)
                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():
                self.lbl_radiobuttons.setVisible(False)
                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)
            else:
                self.lbl_radiobuttons.setVisible(True)

        elif metodo == 2:  # Interpolacion Cuadratica

            Listado_Resultante = unidad_tres.interpolacionCuadratica(Puntos_Validados[0], Puntos_Validados[1], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)
            else:
                self.lbl_radiobuttons.setVisible(True)

        elif metodo == 3:  # Interpolacion de lagrange

            Listado_Resultante = unidad_tres.interpolacionLagrange(Puntos_Validados[0], Puntos_Validados[1], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            else:
                self.lbl_radiobuttons.setVisible(True)

        elif metodo == 4:  # Interpolacion de newton

            Listado_Resultante = unidad_tres.interpolacionNewton(Puntos_Validados[0], Puntos_Validados[1], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            else:
                self.lbl_radiobuttons.setVisible(True)

        elif metodo == 5:# polinomio de hermite

            Listado_Resultante = unidad_tres.interpolacionHermite(Puntos_Validados, valor)

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(Listado_Resultante[1])))
                self.tableWidget.setColumnWidth(1, 830)

            else:
                self.lbl_radiobuttons.setVisible(True)
