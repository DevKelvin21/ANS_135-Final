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
        Analisis_Numerico.resize(1043, 630)
        Analisis_Numerico.setWindowIcon(QtGui.QIcon('docs/images/python.png'))
        Analisis_Numerico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Analisis_Numerico)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 50, 801, 551))
        self.frame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(246, 247, 251);\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnCalcular = QtWidgets.QPushButton(self.frame)
        self.btnCalcular.setGeometry(QtCore.QRect(300, 170, 101, 51))
        self.btnCalcular.setStyleSheet("\n"
"QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/Calcular.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/Calcular_bn.png);\n"
"\n"
"}")
        self.btnCalcular.setText("")
        self.btnCalcular.setObjectName("btnCalcular")
        self.btnLimpiar = QtWidgets.QPushButton(self.frame)
        self.btnLimpiar.setGeometry(QtCore.QRect(420, 170, 101, 51))
        self.btnLimpiar.setStyleSheet("QPushButton {\n"
"    border-radius: 0px;\n"
"    background-color: rgb(246, 247, 251);\n"
"    background-image: url(:/images/images/Limpiar.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 16px;\n"
"    background-image: url(:/images/images/Limpiar_bn.png);\n"
"}\n"
"")
        self.btnLimpiar.setText("")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 250, 711, 251))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 671, 211))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 221, 111))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 41))
        self.label.setStyleSheet("background-image: url(:/images/ingreselafuncion.png);\n"
"background-image: url(:/images/images/ingreselafuncion.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.txtfuncion = QtWidgets.QLineEdit(self.frame_3)
        self.txtfuncion.setGeometry(QtCore.QRect(20, 70, 181, 21))
        self.txtfuncion.setStyleSheet("background-image: url(:/images/barra2.png);\n"
"background-image: url(:/images/images/barra2.png);\n"
"border: 0px;")
        self.txtfuncion.setObjectName("txtfuncion")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(260, 20, 281, 111))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 201, 61))
        self.label_2.setStyleSheet("background-image: url(:/images/valoresiniciales.png);\n"
"background-image: url(:/images/images/valoresiniciales.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.txtX1 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX1.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.txtX1.setStyleSheet("background-image: url(:/images/images/barra.png);\n"
"border: 0px;")
        self.txtX1.setObjectName("txtX1")
        self.txtX2 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX2.setGeometry(QtCore.QRect(130, 60, 41, 21))
        self.txtX2.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;")
        self.txtX2.setObjectName("txtX2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 31, 31))
        self.label_3.setStyleSheet("background-image: url(:/images/x1.png);\n"
"background-image: url(:/images/images/x1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 31, 31))
        self.label_4.setStyleSheet("background-image: url(:/images/images/x2.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.txtX2_2 = QtWidgets.QLineEdit(self.frame_4)
        self.txtX2_2.setGeometry(QtCore.QRect(220, 60, 41, 21))
        self.txtX2_2.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;")
        self.txtX2_2.setObjectName("txtX2_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(190, 60, 31, 31))
        self.label_7.setStyleSheet("background-image: url(:/images/images/x3.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(560, 20, 221, 111))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 201, 61))
        self.label_5.setStyleSheet("background-image: url(:/images/cifras.png);\n"
"background-image: url(:/images/images/cifras.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lblunidad = QtWidgets.QLabel(self.centralwidget)
        self.lblunidad.setGeometry(QtCore.QRect(440, 20, 171, 16))
        self.lblunidad.setObjectName("lblunidad")
        self.txtcifras = QtWidgets.QLineEdit(self.frame_5)
        self.txtcifras.setGeometry(QtCore.QRect(70, 60, 91, 21))
        self.txtcifras.setStyleSheet("background-image: url(:/images/barra.png);\n"
"background-image: url(:/images/images/barra.png);\n"
"border: 0px;")
        self.txtcifras.setObjectName("txtcifras")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(20, 10, 771, 151))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_2.setGeometry(QtCore.QRect(140, 20, 611, 111))
        self.tableWidget_2.setStyleSheet("background-color: rgb(246, 247, 251);")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btnAgregarFIla = QtWidgets.QPushButton(self.frame_6)
        self.btnAgregarFIla.setGeometry(QtCore.QRect(20, 20, 100, 50))
        self.btnAgregarFIla.setStyleSheet("QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/anadir-fila.png);\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"    \n"
"    background-color: rgb(246, 247, 251);\n"
"    background-image: url(:/images/images/anadir-fila.png);\n"
"\n"
"}")
        self.btnAgregarFIla.setText("")
        self.btnAgregarFIla.setObjectName("btnAgregarFIla")
        self.btnEliminarFila = QtWidgets.QPushButton(self.frame_6)
        self.btnEliminarFila.setGeometry(QtCore.QRect(20, 80, 100, 50))
        self.btnEliminarFila.setStyleSheet("QPushButton {\n"
"    border-radius: 0px;\n"
"    background-image: url(:/images/images/eliminar-fila.png);\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"    \n"
"    background-color: rgb(246, 247, 251);\n"
"    background-image: url(:/images/images/eliminar-fila.png);\n"
"\n"
"}")
        self.btnEliminarFila.setText("")
        self.btnEliminarFila.setObjectName("btnEliminarFila")
        self.frame_6.raise_()
        self.btnCalcular.raise_()
        self.btnLimpiar.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.cmbMetodos = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMetodos.setGeometry(QtCore.QRect(530, 10, 181, 22))
        self.cmbMetodos.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(246, 247, 251);")
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
        self.radioButton.setGeometry(QtCore.QRect(800, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(900, 10, 101, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        Analisis_Numerico.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Analisis_Numerico)
        self.statusbar.setObjectName("statusbar")
        Analisis_Numerico.setStatusBar(self.statusbar)

        self.retranslateUi(Analisis_Numerico)
        QtCore.QMetaObject.connectSlotsByName(Analisis_Numerico)

    def retranslateUi(self, Analisis_Numerico):
        _translate = QtCore.QCoreApplication.translate
        Analisis_Numerico.setWindowTitle(_translate("Analisis_Numerico", "Trabajo final ANS-135"))
        self.cmbMetodos.setItemText(0, _translate("Analisis_Numerico", "> Seleccione una unidad <"))
        self.radioButton.setText(_translate("Analisis_Numerico", "Ver polinomio"))
        self.radioButton_2.setText(_translate("Analisis_Numerico", "No ver polinomio"))
        self.cmbMetodos.activated[str].connect(self.Filtrar_Objects)
        #Asignamos funciones a los botones.
        self.btnCalcular.clicked.connect(self.Resolverlo)
        self.btnLimpiar.clicked.connect(self.Limpiar_Objects)
        self.btnAgregarFIla.clicked.connect(self.agregarColumna)
        self.btnEliminarFila.clicked.connect(self.eliminarColumna)
        #Botones unidades.
        self.btnUnidad1.clicked.connect(lambda: self.unidades("0"))
        self.btnUnidad1.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad2.clicked.connect(lambda: self.unidades("1"))
        self.btnUnidad2.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad3.clicked.connect(lambda: self.unidades("2"))
        self.btnUnidad3.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        self.btnUnidad4.clicked.connect(lambda: self.unidades("3"))
        self.btnUnidad4.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        #self.btnUnidad5.clicked.connect(self.Filtrar_llenado_cmbMetodos)
        #Ocultamos todos los componetes para filtrarlos con los btn de las unidades.
        self.frame.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        #Validamos que solo acepte numeros y signos NO letras.
        
        self.txtX1.setValidator(QtGui.QDoubleValidator())
        self.txtX2.setValidator(QtGui.QDoubleValidator())
        self.txtX2_2.setValidator(QtGui.QDoubleValidator())
        self.txtcifras.setValidator(QtGui.QDoubleValidator())

        #label que valida la unidad elegida con el btn
        self.lblunidad.setText(_translate("MainWindow", "0"))
        self.lblunidad.setVisible(False)


    def unidades(self, cual):
        self.lblunidad.setText(str(cual))

    def Filtrar_llenado_cmbMetodos(self):
        
        cual = int(self.lblunidad.text())
        self.frame.setVisible(True)
        self.frame_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        

        if cual == 0:  # Metodos de la primera unidad

            self.cmbMetodos.setGeometry(QtCore.QRect(530, 10, 181, 22))
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

          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.cmbMetodos.setVisible(True)
            


        elif cual == 1:  # Metodos de la segunda unidad
            self.cmbMetodos.setGeometry(QtCore.QRect(530, 10, 181, 22))
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


          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.cmbMetodos.setVisible(True)
            

        elif cual == 2:  # Metodos de la unidad 3
            self.cmbMetodos.setGeometry(QtCore.QRect(530, 10, 181, 22))

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

        elif cual == 3: #metodos de la unidad 4
            self.cmbMetodos.setGeometry(QtCore.QRect(530, 10, 181, 22))
            
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
            

            # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
            
            
            self.frame_4.setVisible(True)
            self.frame_5.setVisible(True)


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
                self.btnCalcular.setVisible(True)
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
                self.btnCalcular.setVisible(True)
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

            global Numero_Filas_Columnas

            # Deseleccionamos los radio button

            self.radioButton.setAutoExclusive(False)
            self.radioButton.setChecked(False)
            self.radioButton.setAutoExclusive(True)
            self.radioButton_2.setAutoExclusive(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_2.setAutoExclusive(True)

            if queMetodo == 1:
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 2:
                Numero_Filas_Columnas = 4
                self.Aplicar_Ajustes_Tabla_Unidad_3(5)
            elif queMetodo == 3:
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 4:
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 5:
                Numero_Filas_Columnas = 3
                self.Aplicar_Ajustes_Tabla_Unidad_3(4)
            elif queMetodo == 6:
                Numero_Filas_Columnas = 4
                self.Aplicar_Ajustes_Tabla_Unidad_3(5)
            elif queMetodo == 7:
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
        queMetodo = self.cmbMetodos.currentIndex()
        if queMetodo >= 0 and queMetodo <= 6 or queMetodo == 9:
            x = []
            y = []
            i = 0

            for j in range(-50, 51):
                x.append(i)
                y.append(i)

            try:
                def f1(x):
                    funcion = metodos.Sustituir_y_Evaluar_Funcion(
                        self.txtfuncion.text(), x, 0, 0)
                    return funcion

                # asignamos un rango de valores a graficar
                var = range(start=-100, stop=100, step=0.01)

                plt.plot(var, [f1(i) for i in var], label='Funcion 1')

                plt.xlim(-50, 50)
                plt.ylim(-50, 50)

                plt.plot(x, y)
                plt.axvline(0, color='r')
                plt.axhline(0, color='r')

                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.grid()
                plt.title("Representacion de la función")
                # colocamos la leyenda en la parte inferior derecha
                plt.show()
            except:
                print("Algo salio mal")

        elif queMetodo >= 7 and queMetodo <= 8 or queMetodo == 10:

            coeficientes = metodos.Obtener_Coeficientes(self.txtfuncion.text())
            coeficientes.reverse()

            print(coeficientes)

            tamanio = len(coeficientes)

            funGraficar = ""

            # Hacemos una funcion que si se pueda graficar
            for x in range(len(coeficientes)):
                if coeficientes[x] != 0:
                    if coeficientes[x] > 0:
                        if x == 0:
                            funGraficar += str(coeficientes[x]) + \
                                "*x^"+str(tamanio-1)
                            tamanio = tamanio - 1
                        else:
                            if x == (len(coeficientes)-1):
                                funGraficar += "+" + str(coeficientes[x])
                                tamanio = tamanio - 1
                            else:
                                funGraficar += "+" + \
                                    str(coeficientes[x]) + "*x^"+str(tamanio-1)
                                tamanio = tamanio - 1
                    else:
                        if x == (len(coeficientes)-1):
                            funGraficar += str(coeficientes[x])
                            tamanio = tamanio - 1
                        else:
                            funGraficar += str(coeficientes[x]) + \
                                "*x^"+str(tamanio-1)
                            tamanio = tamanio - 1
                else:
                    funGraficar += "+0*x^"+str(tamanio-1)
                    tamanio = tamanio - 1

            print(funGraficar)

            x = []
            y = []
            i = 0

            for j in range(-50, 51):
                x.append(i)
                y.append(i)

            try:
                def f1(x):
                    funcion = metodos.Sustituir_y_Evaluar_Funcion(funGraficar, x, 0, 0)
                    return funcion

                # asignamos un rango de valores a graficar
                var = range(-100, 100)

                plt.plot(var, [f1(i) for i in var], label='Funcion 1')

                plt.xlim(-50, 50)
                plt.ylim(-50, 50)

                plt.plot(x, y)
                plt.axvline(0, color='r')
                plt.axhline(0, color='r')

                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.grid()
                plt.title("Representacion de la función")
                # colocamos la leyenda en la parte inferior derecha
                plt.show()
            except:
                print("Algo salio mal")

    def agregarColumna(self):
        global Numero_Filas_Columnas
        metodo = self.cmbMetodos.currentIndex()

        if metodo == 0:
            print("Seleccione un metodo primero ")
        elif metodo == 1:
            print("Solamente se puede trabajar con 2 puntos")
        else:
            if Numero_Filas_Columnas == 13:
                print("Maximo numero de columnas alcanzado")
            else:
                self.tableWidget_2.insertColumn(Numero_Filas_Columnas+1)
                Numero_Filas_Columnas += 1

    def eliminarColumna(self):
        global Numero_Filas_Columnas
        metodo = self.cmbMetodos.currentIndex()

        if metodo == 1:  # lineal
            if Numero_Filas_Columnas == 3:
                print("Se necesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1

        elif metodo == 2:  # Cuadratica
            if Numero_Filas_Columnas == 4:
                print("Se necesitan al menos 3 puntos")
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1

        elif metodo == 3:  # Lagrange
            if Numero_Filas_Columnas == 3:
                print("Se necesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas - 1

        elif metodo == 4:  # Newton
            if Numero_Filas_Columnas == 3:
                print("Se neecesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(Numero_Filas_Columnas)
                Numero_Filas_Columnas = Numero_Filas_Columnas-1

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
                    print(f"Funcion {funcion} mayor a cuartica")
                else:
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
                        print(f"Esta {funcion} no es una funcion ")
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
                print("Seleccione una acción en los radio button")

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
                print("Seleccione una acción en los radio button")

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
                print("Seleccione una acción en los radio button")

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
                print("Seleccione una acción en los radio button")

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
                print("Seleccione una acción en los radio button")


        
    