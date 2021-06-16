import decimal
from numpy.lib.shape_base import column_stack
import sympy as Sympy
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth, ln
from numpy.polynomial import Polynomial as P
from sympy.core.function import expand
from sympy.simplify.radsimp import numer
from fractions import Fraction

x, e, y, z = Sympy.symbols('x e y z')

#♪-------------------------------------------- FUNCIONES NECESARIAS -----------------------------------------------------------------


def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada): #Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = Sympy.sympify(funcion)
                gxValor = Sympy.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = Sympy.sympify(funcion)
                gxValor = Sympy.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = Sympy.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return False

def encontrarDerivada(funcion,queDerivada):
    funcioon = Sympy.sympify(funcion)
    gxValor = Sympy.diff(funcioon, x,queDerivada)
    return gxValor

#♪-------------------------------------------- METODOS NUMERICOS VISTOS EN CLASE -----------------------------------------------------------------    
  
# <------------- Derivadas de primer orden --------------------->
def diferenciacion_numerica_adelante(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/h)


        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+(2*h),0,0)*(-1) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-3)
    
        #guardamos la segunda diferencia 
        Solucion_Listado.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)
        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]

        #primer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[2]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        print(Solucion_Listado[0])
        print(Solucion_Listado[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(h))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(4) + lista_valores[-3]

        #guardamos la segunda diferencia
        Solucion_Listado.append((numerador1)/(h*2))
        print(Solucion_Listado)

def diferenciacion_numerica_atras(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/h)


        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-2*h,0,0)
    
        #guardamos la segunda diferencia 
        Solucion_Listado.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)
        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]

        #primer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[2]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        print(Solucion_Listado[0])
        print(Solucion_Listado[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(h))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i-1])
                lista_valores.append(lista_y[i-2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(3) + lista_valores[1]*(-4) + lista_valores[2]

        #guardamos la segunda diferencia
        Solucion_Listado.append((numerador1)/(h*2))
        print(Solucion_Listado)

def diferenciacion_numerica_centrada(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(2*h))


        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-1) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(8) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-8) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-2*h,0,0)
    
        #guardamos la segunda diferencia 
        Solucion_Listado.append(numerador1/(12*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)
        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]

        #primer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[2]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        return Solucion_Listado

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(h*2))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])
                lista_valores.append(lista_y[i-2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(8) + lista_valores[2]*(-8) + lista_valores[3]

        #guardamos la segunda diferencia
        Solucion_Listado.append((numerador1)/(h*12))
        print(Solucion_Listado)

def diferenciacion_numerica_tres_puntos(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(2*h))


        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-1)
    
        #guardamos la segunda diferencia 
        Solucion_Listado.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)
        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]

        #primer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[2]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        print(Solucion_Listado[0])
        print(Solucion_Listado[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(h*2))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i+2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-3) + lista_valores[1]*(4) + lista_valores[2]*(-1) 

        #guardamos la segunda diferencia
        Solucion_Listado.append((numerador1)/(h*2))
        print(Solucion_Listado)

def diferenciacion_numerica_cinco_puntos(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-25) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(48) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-36) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)*(16) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+4*h,0,0)*(-3)
        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(12*h))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-10) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(18) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-6) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)
        #guardamos la segunda diferencia 
        Solucion_Listado.append(numerador1/(12*h))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-2*h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-8) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(8) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-1) 
        #guardamos la Tercera diferencia 
        Solucion_Listado.append(numerador1/(12*h))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-3*h,0,0)*(4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(6) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-8) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(34) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(34)
        #guardamos la cuarta diferencia 
        Solucion_Listado.append(numerador1/(12*h))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-4*h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-3*h,0,0)*(-3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-2*h,0,0)*(4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial-h,0,0)*(-36) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(25)
        #guardamos la quinta diferencia 
        Solucion_Listado.append(numerador1/(12*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)
        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]
        valor_apro3 = Solucion_Listado[2]
        valor_apro4 = Solucion_Listado[3]
        valor_apro5 = Solucion_Listado[4]

        #primer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[2]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        #tercer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        #cuarto error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro4)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100)

        #quinto error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro5)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[4]*100) 

        print(Solucion_Listado[0])
        print(Solucion_Listado[1])
        print(Solucion_Listado[2])
        print(Solucion_Listado[3])
        print(Solucion_Listado[4])

    else:
        lista_valores = []
        lista_valores_2 = []
        lista_valores_3 = []
        lista_valores_4 = []
        lista_valores_5 = []

        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:

                #valores para primera diferencia
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+3])
                lista_valores.append(lista_y[i+4])

                #valores para segunda diferencia
                lista_valores_2.append(lista_y[i-1])
                lista_valores_2.append(lista_y[i])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i+2])
                lista_valores_2.append(lista_y[i+3])

                #valores para tercera diferencia
                lista_valores_3.append(lista_y[i-2])
                lista_valores_3.append(lista_y[i-1])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i+2])

                #valores para cuarta diferencia
                lista_valores_4.append(lista_y[i-3])
                lista_valores_4.append(lista_y[i+2])
                lista_valores_4.append(lista_y[i-1])
                lista_valores_4.append(lista_y[i])
                lista_valores_4.append(lista_y[i+1])
                lista_valores_4.append(lista_y[i+2])

                #valores para quinta diferencia
                lista_valores_5.append(lista_y[i-4])
                lista_valores_5.append(lista_y[i-3])
                lista_valores_5.append(lista_y[i-2])
                lista_valores_5.append(lista_y[i-1])
                lista_valores_5.append(lista_y[i])

                
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-25) + lista_valores[1]*(48) + lista_valores[2]*(-36) + lista_valores[3]*(16) + lista_valores[4]*(-3)
        #guardamos la primera diferencia
        Solucion_Listado.append((numerador1)/(h*12))

        numerador1 = lista_valores_2[0]*(-3) + lista_valores_2[1]*(-10) + lista_valores_2[2]*(18) + lista_valores_2[3]*(-6) + lista_valores_2[4]
        #guardamos la segunda diferencia
        Solucion_Listado.append((numerador1)/(h*12))

        numerador1 = lista_valores_3[0] + lista_valores_3[1]*(-8) + lista_valores_3[2]*(8) + lista_valores_3[3]*(-1) 
        #guardamos la tercera diferencia
        Solucion_Listado.append((numerador1)/(h*12))

        numerador1 = lista_valores_4[0]*(4) + lista_valores_4[1]*(6) + lista_valores_4[2]*(-8) + lista_valores_4[3]*(34) + lista_valores_4[4]*(3)  + lista_valores_4[5]*(34)
        #guardamos la cuarta diferencia
        Solucion_Listado.append((numerador1)/(h*12))

        numerador1 = lista_valores_5[0] + lista_valores_5[1]*(-3) + lista_valores_5[2]*(4) + lista_valores_5[3]*(-36) + lista_valores_5[25]
        #guardamos la quinta diferencia
        Solucion_Listado.append((numerador1)/(h*12))

    
        print(Solucion_Listado)


# <------------- Derivadas de orden superior --------------------->

def diferenciacion_numerica_adelante_orden_superior(funcion,puntoInicial,h,tablaValores):
    Solucion_Listado = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        #<------------------ Primera doferencia ----------------------------->
        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(-2) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0) 
        Solucion_Listado.append((numerador1)/(h**2))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(-3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-1)
        Solucion_Listado.append(numerador1/(h**3))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+4*h,0,0) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)*(-4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(6) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(-4)  + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)
        Solucion_Listado.append(numerador1/(h**4))


        #<------------------ Segunda diferencia ----------------------------------->
        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)*(-1) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(4) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(-5) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(2)
        Solucion_Listado.append((numerador1)/(h**2))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+4*h,0,0)*(-3) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)*(14) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(24) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(-18) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(-5)
        Solucion_Listado.append(numerador1/(h**3))

        numerador1 = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+5*h,0,0)*(-2) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+4*h,0,0)*(11) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+3*h,0,0)*(-24) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+2*h,0,0)*(26)  + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial+h,0,0)*(-14) + Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,0,0)*(3)
        Solucion_Listado.append(numerador1/(h**4))

        #calculamos los errores para la primera y la segunda diferencia
         
        lista_errores = []
        valor_verdadero = Sustituir_y_Evaluar_Funcion(funcion,puntoInicial,1,1)

        valor_apro1 = Solucion_Listado[0]
        valor_apro2 = Solucion_Listado[1]
        valor_apro3 = Solucion_Listado[2]

        valor_apro4 = Solucion_Listado[3]
        valor_apro5 = Solucion_Listado[4]
        valor_apro6 = Solucion_Listado[5]

        # <-------------------- primera diferencia ----------------------------->

        #primer error
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[6]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[8]*100)

        #tercer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[10]*100)

         # <-------------------- segunda diferencia ----------------------------->

        #primer error
        Solucion_Listado.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[12]*100)

        #segundo error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[14]*100)

        #tercer error 
        Solucion_Listado.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        Solucion_Listado.append(Solucion_Listado[16]*100)

        print(Solucion_Listado[0])
        print(Solucion_Listado[1])
        print(Solucion_Listado[2])
        print("\n")
        print(Solucion_Listado[3])
        print(Solucion_Listado[4])
        print(Solucion_Listado[5])
        
    else:
        lista_valores = []
        lista_valores_2 = []
        lista_valores_3 = []
        lista_valores_4 = []
        lista_valores_5 = []
        lista_valores_6 = []
        
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:

                # <-------------  valores para primera diferencia ------------------------>
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])
               
                lista_valores_2.append(lista_y[i+3])
                lista_valores_2.append(lista_y[i+2])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i])

                lista_valores_3.append(lista_y[i+4])
                lista_valores_3.append(lista_y[i+3])
                lista_valores_3.append(lista_y[i+2])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i])

                # <--------------- valores para segunda diferencia ------------------------>
                lista_valores_4.append(lista_y[i+3])
                lista_valores_4.append(lista_y[i+2])
                lista_valores_4.append(lista_y[i+1])
                lista_valores_4.append(lista_y[i])

                lista_valores_5.append(lista_y[i+4])
                lista_valores_5.append(lista_y[i+3])
                lista_valores_5.append(lista_y[i+2])
                lista_valores_5.append(lista_y[i+1])
                lista_valores_5.append(lista_y[i])

                lista_valores_6.append(lista_y[i+5])
                lista_valores_6.append(lista_y[i+4])
                lista_valores_6.append(lista_y[i+3])
                lista_valores_6.append(lista_y[i+2])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        # <---------------- Primera diferencia ---------------------->

        numerador1 = lista_valores[0] + lista_valores[1]*(-2) + lista_valores[2]
        Solucion_Listado.append((numerador1)/(h**2))

        numerador1 = lista_valores[0] + lista_valores[1]*(-3) + lista_valores[2]*(3) + lista_valores[3]*(-1) 
        Solucion_Listado.append((numerador1)/(h**3))

        numerador1 = lista_valores[0] + lista_valores[1]*(-4) + lista_valores[2]*(6) + lista_valores[3]*(-4) + lista_valores[4] 
        Solucion_Listado.append((numerador1)/(h**4))

        # <---------------- segunda diferencia ---------------------->

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(4) + lista_valores[2]*(-5) + lista_valores[3]*(2)
        Solucion_Listado.append((numerador1)/(h**2))

        numerador1 = lista_valores[0]*(-3) + lista_valores[1]*(14) + lista_valores[2]*(-24) + lista_valores[3]*(18) + lista_valores[4]*(-5)
        Solucion_Listado.append((numerador1)/(h**3))

        numerador1 = lista_valores[0]*(-2) + lista_valores[1]*(11) + lista_valores[2]*(-24) + lista_valores[3]*(26) + lista_valores[4]*(-14) + lista_valores[5]*(3)  
        Solucion_Listado.append((numerador1)/(h**4))

        print(Solucion_Listado)

def diferenicacion_numerica_atras_orden_superior(funcion,puntoInicial,h,tablaValores):
    print("falta")

def diferenicacion_numerica_centrales_orden_superior(funcion,puntoInicial,h,tablaValores):
    print("falta")


# <------------- metodo de richardson --------------------->

def metodo_richardson(funcion,puntoInicial,h,nivel):

    #lista con respuestas
    listResultados = []

    #lista con los valores de h
    valores_h = []

    #llenamos la lista de valores_h soguiendo esta formula h_n = (h_n-1)/2
    for i in range(0,nivel,1):
        if i == 0:
            valores_h.append(h)
        else:
            valores_h.append((valores_h[i-1])/2)

    #lista donde se encontrara el primer nivel 
    primer_nivel = []
    for i in valores_h:
        valor = diferenciacion_numerica_centrada(funcion,puntoInicial,i,[])
        primer_nivel.append(valor[1])


    #lista que ira cambiando de tamaño con respecto al nivel en el que se encuente 
    lista_cambiante = primer_nivel

    #matriz donde estaran los demas niveles
    matriz_con_niveles = [] 
    matriz_con_niveles.append(primer_nivel)
    lista_nivel = []
    contador_nivel = 3

    for i in range(1,nivel,1):
        for j in range(1,len(lista_cambiante)):
            if i == 1:
                primer_termino = (4/3)*lista_cambiante[j]
                segundo_termino = (-1/3)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            elif i == 2:
                primer_termino = (16/15)*lista_cambiante[j]
                segundo_termino = (-1/15)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            else:
                primer_termino = ((4**contador_nivel)/((4**contador_nivel)-1))*lista_cambiante[j]
                segundo_termino = ((1)/((4**contador_nivel)-1))*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            

        matriz_con_niveles.append(lista_nivel)
        lista_cambiante = lista_nivel
        lista_nivel = []
        if i >= 3:
            contador_nivel += 1

    listResultados = matriz_con_niveles

    return listResultados

# <------------- Integración numérica --------------------->

def regla_del_trapecio_simple(funcion,a,b,tablaValores):
    Solucion_Listado = []

    if funcion != '':

        numerador = Sustituir_y_Evaluar_Funcion(funcion,a,0,0) + Sustituir_y_Evaluar_Funcion(funcion,b,0,0)
        evaluacion = (b-a)*(numerador/2)

        Solucion_Listado.append(evaluacion)

        return Solucion_Listado

    else: #Para cuando trabajamos con puntos y no con funciones 

        tamanio = len(tablaValores[0])
        listaX = tablaValores[0]
        listaY = tablaValores[1]

        if tamanio == 2:
            resultado = (listaX[1]-listaX[0])*((listaY[0]+listaY[1])/2)
            Solucion_Listado.append(resultado)
            print(Solucion_Listado)
            return Solucion_Listado

        else:
            print("Para resolver mediante el trapecio simple solo se utilizan 2 puntos")

def regla_del_trapecio_compuesta(funcion,a,b,n,tablaValores):
    
    #respuesta
    Solucion_Listado = []

    if funcion != '':

        h = Fraction((b-a),n)
        aa = a

        lista_con_valor_h = []
        lista_evaluaciones = []
        sumatoria_puntos_medios = 0

        for i in range(0,n+1,1):
            lista_con_valor_h.append(aa)
            lista_evaluaciones.append(Sustituir_y_Evaluar_Funcion(funcion,lista_con_valor_h[i],0,0))
            if i >= 1 and i <= n-1:
                sumatoria_puntos_medios += lista_evaluaciones[i]

            #Aumentamos el valor de a en h    
            aa += h

        resultado = (b-a)*((lista_evaluaciones[0] + 2*sumatoria_puntos_medios + lista_evaluaciones[n]))/(2*n)

        Solucion_Listado.append(resultado)
        return Solucion_Listado

    else:

        sumatoria_puntos_medios = 0
        listaX = tablaValores[0]
        listaY = tablaValores[1]
        tamanio = len(listaX)-1


        for i in range(0,tamanio+1,1):
            if i >= 1 and i <= tamanio-1:

                sumatoria_puntos_medios += listaY[i]

        resultado = (b-a)*(listaY[0] + 2*sumatoria_puntos_medios + listaY[tamanio])/(2*tamanio)

        Solucion_Listado.append(resultado)
        print(Solucion_Listado)
        return Solucion_Listado

def trapecio_para_dobles_y_triples(funcion,lista_a,lista_b,n,orden_integral):

    #lista con respuestas
    Solucion_Listado = []

    if orden_integral == 2: #integral doble
        a = lista_a[0]
        b = lista_b[0] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = Sympy.sympify(funcion).subs(x, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        valores_sumados_simplificados = Sympy.expand(valores_sumados)

        funcion_encontrada = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        print('primera funcion encontrada:  ------------> ',funcion_encontrada)
        funcion_encontrada = Sympy.expand(funcion_encontrada)

        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[1]
        b = lista_b[1] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = Sympy.sympify(funcion_encontrada).subs(y, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]


        resultado = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados + lista_operaciones_de_evaluarX[n])
        print('valor encontrado:  ------------>', resultado)
        Solucion_Listado.append(resultado)
    
    elif orden_integral == 3: #Integral Triple
        a = lista_a[0]
        b = lista_b[0] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = Sympy.sympify(funcion).subs(x, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        valores_sumados_simplificados = Sympy.expand(valores_sumados)

        funcion_encontrada = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        funcion_encontrada = Sympy.expand(funcion_encontrada)
        
        print('primera funcion encontrada: ------------> ',funcion_encontrada)
        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[1]
        b = lista_b[1] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = Sympy.sympify(funcion_encontrada).subs(y, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]
                
        valores_sumados_simplificados = Sympy.expand(valores_sumados)

        funcion_encontrada_2 = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        funcion_encontrada_2 = Sympy.expand(funcion_encontrada_2)
        print('segunda funcion encontrada: ------------> ',funcion_encontrada_2)

        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[2]
        b = lista_b[2] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h


        for i in range(0,n+1,1):
            resultado = Sympy.sympify(funcion_encontrada_2).subs(z, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        resultado = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados + lista_operaciones_de_evaluarX[n])
        Solucion_Listado.append(resultado)
        print('valor encontrado: ------------> ',resultado)
        return Solucion_Listado

def integracion_simpson_unTercio_simple(funcion, a, b, listaX, listaY):

    # Variables a utilizar
    puntoMedio = (a + b)/2
    respuesta = 0

    # Si el usuario solo digito una funcion se realiza por el if:
    if funcion != "":

        # Realizas la evaluacion de los puntos en la funcion
        funcion_Evaludad_En_A = Sustituir_y_Evaluar_Funcion(funcion, a, 0, 0)
        funcion_Evaludad_En_B = Sustituir_y_Evaluar_Funcion(funcion, b, 0, 0)
        funcion_Evaludad_En_PM = Sustituir_y_Evaluar_Funcion(funcion, puntoMedio, 0, 0)

        # Realizamos la formula de integracion de simpson
        respuesta = (b-a)*((funcion_Evaludad_En_A +
                           (4*funcion_Evaludad_En_PM)+funcion_Evaludad_En_B)/6)

        return respuesta

    # Si el usuario digito los valores de la tabla se realiza el else:
    else:
        # Realizamos la formula de integracion de simpson
        respuesta = (listaX[2]-listaX[0]
                     )((listaY[0]+(4*listaY[1])+listaY[2])/6)

        return respuesta

def integracion_simpson_unTercio_compuesta(funcion, a, b, n_Intervalos, valoresX, valoresY):

    # Variables a utilizar
    h = (b - a)/n_Intervalos  # Distanca de separacion entre punto y punto
    listaX = []  # Aqui guardaremos todos los x
    lista_Puntos_Medios = []
    lista_Puntos_Medios_Funciones = []
    listaX_Evaluados = []  # Aqui guardaremos todos los x evaluados en la funcion
    valor_X_Proximo = 0  # variable auxiliadora para calcular los x
    # variable auxiliadora para calcular los x evaluados en f(x)
    valor_X_Funcion_Proximo = 0
    sumatoria_Fx = 0  # aqui sumaremos todos los f(x)
    # aqui sumaremos todos los f(x) de los puentos medios
    sumatoria_Fx_Medios = 0
    respuesta = 0

    if funcion != "" and len(valoresX) == 0:
        listaX.append(a)  # Agregamos la primera x
        listaX_Evaluados.append(Sustituir_y_Evaluar_Funcion(funcion, a, 0, 0))

        # For para calcular valore de X
        for i in range(0, n_Intervalos, 1):

            valor_X_Proximo = listaX[i] + h  # Calculamos los x

            listaX.append(valor_X_Proximo)  # Agregamos los x a esta lista

        # For para calcular valore de X en la funcion
        for i in range(0, len(listaX)-1, 1):

            valor_X_Funcion_Proximo = Sustituir_y_Evaluar_Funcion(
                funcion, listaX[i+1], 0, 0)  # Calculamos los x

            # Agregamos los x a esta lista
            listaX_Evaluados.append(valor_X_Funcion_Proximo)

        # Hacemos la suma de todos los f(x) de los x
        for i in range(1, len(listaX_Evaluados)-1, 1):
            sumatoria_Fx += listaX_Evaluados[i]

        # Sacamos los puntos medios
        for i in range(0, len(listaX)-1, 1):

            lista_Puntos_Medios.append(
                (listaX[i]+listaX[i+1])/2)

        # Sacamos los valores de los puntos medios evaluadosen la funcion
        for i in range(0, len(lista_Puntos_Medios), 1):

            lista_Puntos_Medios_Funciones.append(Sustituir_y_Evaluar_Funcion(
                funcion, lista_Puntos_Medios[i], 0, 0))

            sumatoria_Fx_Medios += Sustituir_y_Evaluar_Funcion(
                funcion, lista_Puntos_Medios[i], 0, 0)

        respuesta = (b-a)*((listaX[0]+(4*sumatoria_Fx_Medios) +
                           (2*sumatoria_Fx)+listaX[len(listaX)-1])/(6*n_Intervalos))

        print(respuesta)

    else:
        # Hacemos la suma de todos los f(x) de los x
        for i in range(1, len(valoresY)-1, 1):
            sumatoria_Fx += valoresY[i]

        # Sacamos los puntos medios
        for i in range(0, len(valoresX)-1, 1):

            lista_Puntos_Medios.append(
                (valoresX[i]+valoresX[i+1])/2)

        # Sacamos los valores de los puntos medios evaluadosen la funcion
        for i in range(0, len(lista_Puntos_Medios), 1):

            lista_Puntos_Medios_Funciones.append(Sustituir_y_Evaluar_Funcion(
                funcion, lista_Puntos_Medios[i], 0, 0))

            sumatoria_Fx_Medios += Sustituir_y_Evaluar_Funcion(
                funcion, lista_Puntos_Medios[i], 0, 0)

        respuesta = (b-a)*((valoresX[0]+(4*sumatoria_Fx_Medios) +
                           (2*sumatoria_Fx)+valoresX[len(valoresX)-1])/(6*n_Intervalos))

        print(respuesta)

def integracion_simpson_tresOctavos_simple(funcion, a, b):
    # Variables a utilizar
    respuesta = 0
    h = (b - a)/3
    listaX = []

    if funcion != "":
        listaX.append(a)  # Agregamos el valor inicial de las x que es a

        # Llenamos los valores de x con sus valores + h
        for i in range(0, 3, 1):
            listaX.append(listaX[i]+h)

        respuesta = (b-a)*((Sustituir_y_Evaluar_Funcion(funcion, listaX[0], 0, 0) +
                            (3*Sustituir_y_Evaluar_Funcion(funcion, listaX[1], 0, 0)) +
                            (3*Sustituir_y_Evaluar_Funcion(funcion, listaX[2], 0, 0)) +
                            (Sustituir_y_Evaluar_Funcion(funcion, listaX[3], 0, 0)))/8)

        print(respuesta)
    else:
        print("Escriba la funcion")

def integracion_simpson_tresOctavos_compuesta(funcion, a, b, n_Intervalos):
    # Variables a utilizar
    h = (b - a)/n_Intervalos  # Distanca de separacion entre punto y punto
    listaX = []  # Aqui guardaremos todos los x

    lista_subIntervalos = []  # Tendra la sima de 1/3 a los valores de x

    sumatoria_Fx = 0  # aqui sumaremos todos los f(x)

    # aqui sumaremos todos los f(x) de los subindices
    sumatoria_Fx_Subindices = 0
    respuesta = 0

    if funcion != "":

        listaX.append(a)  # Agregamos el primer x

        # Agregamos los demas valores de x
        for i in range(0, n_Intervalos, 1):
            listaX.append(listaX[i]+h)

        # Agregamos los sub intervalos
        contador_Dos = 0  # Esta variable ira saltando de dos en dos
        for i in range(0, len(listaX)-1, 1):
            lista_subIntervalos.append(listaX[i]+(1/3))

            lista_subIntervalos.append(lista_subIntervalos[contador_Dos]+1/3)
            contador_Dos += 2

        # for para sumar los x evaluados en la funcion
        for i in range(1, len(listaX)-1, 1):
            sumatoria_Fx += Sustituir_y_Evaluar_Funcion(funcion, listaX[i], 0, 0)

        # for para sumar los subintervalos en la funcion
        for i in range(0, len(lista_subIntervalos), 1):
            sumatoria_Fx_Subindices += Sustituir_y_Evaluar_Funcion(
                funcion, lista_subIntervalos[i], 0, 0)

        respuesta = ((b-a)/(8*n_Intervalos))*(Sustituir_y_Evaluar_Funcion(funcion, listaX[0], 0, 0) +
                                              3*sumatoria_Fx_Subindices +
                                              2*sumatoria_Fx +
                                              Sustituir_y_Evaluar_Funcion(funcion, listaX[len(listaX)-1], 0, 0))

        print(respuesta)

    else:
        print("Difite una funcion")

def integracion_rosemberg(funcion,a,b,nivel):

    #lista con respuestas
    Solucion_Listado = []

    #lista donde se encontrara el primer nivel 
    primer_nivel = []
    n = 2

    for i in range(0,nivel,1):
        if i == 0:
            valor = regla_del_trapecio_simple(funcion,a,b,[])
            primer_nivel.append((valor[0]).evalf())
        else:
            valor = regla_del_trapecio_compuesta(funcion,a,b,n,[])
            primer_nivel.append(valor[0].evalf())
            n += 2

    #lista que ira cambiando de tamaño con respecto al nivel en el que se encuente 
    lista_cambiante = primer_nivel

    #matriz donde estaran los demas niveles
    matriz_con_niveles = [] 
    matriz_con_niveles.append(primer_nivel)
    lista_nivel = []
    contador_nivel = 3

    for i in range(1,nivel,1):
        for j in range(1,len(lista_cambiante)):
            if i == 1:
                primer_termino = (4/3)*lista_cambiante[j]
                segundo_termino = (-1/3)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            elif i == 2:
                primer_termino = (16/15)*lista_cambiante[j]
                segundo_termino = (-1/15)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            else:
                primer_termino = ((4**contador_nivel)/((4**contador_nivel)-1))*lista_cambiante[j]
                segundo_termino = ((1)/((4**contador_nivel)-1))*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            

        matriz_con_niveles.append(lista_nivel)
        lista_cambiante = lista_nivel
        lista_nivel = []
        if i >= 3:
            contador_nivel += 1

    Solucion_Listado = matriz_con_niveles
    for i in Solucion_Listado:
        print(i)

    return Solucion_Listado

def integracion_cuadratura_Gaussiana(funcion,a,b,n):
    #cada sub-lista va a representar un punto

    lista_Wk = [[2], [1,1], [0.555556,0.888889,0.555556], [0.347855,0.652145,-0.652145,-0.347855], [0.236927,0.478629,0.568889,0.478629,0.236927], [], [], [], [], [], [], []]

    lista_Tk = [[0], [0.57735,-0.57735], [-0.774597,0,0.774597], [-0.861136,-0.339981,0.339981,0.861136], [-0.90618,-0.538469,0,0.538469,0.90618], [], [], [], [], [], [], []]


    lista_variable_Wk = lista_Wk[n-1]
    lista_variable_Tk = lista_Tk[n-1]
    resultado = 0
    punto = 0

    for i in range(0,n,1):
        punto = ((b-a)*lista_variable_Tk[i] + (b+a))/2
        resultado += lista_variable_Wk[i]*Sustituir_y_Evaluar_Funcion(funcion,punto,0,0)

    resultado = resultado*(b-a)/2

    print(resultado)
    
def evaluar_formula_Simpson_adapatativo(a,b,funcion): #Creo que como funcion aparte es inecesaria pero xd luego se puede integrar al metodo
    puntoS=[]
    puntoS = ((b-a)/6)*(Sustituir_y_Evaluar_Funcion(funcion,a,0,0)+Sustituir_y_Evaluar_Funcion(funcion,b,0,0)+ (4 * Sustituir_y_Evaluar_Funcion(funcion, ((a+b)/2),0,0)))
    return puntoS

def integracion_simpson_unTercio_adaptativo(tolerancia,a,b,funcion):
    Solucion_Listado=[] #Aca irá respuesta final
    puntomedio=(a+b)/2
    listaintervalos=[ # en el bucle de abajo intervalo cambia entre [a,b] [a,puntomedio] [puntomedio,b] y permite elegir una coordenada del intervalo
        
        #Esta es una lista multidimensional (listas dentro de listas)
        [a,b],[a,puntomedio],[puntomedio,b]
        
    ]
    listaS_eval=[]#aca iran los S(a,b) evaluados
    contador=0 #Se utiliza mas abajo para darle nuevos valores a (a.b)
    variable_de_control=0 #se utiliza como validacion de salida 

    #agregarintervalos
    for intervalo in listaintervalos: #intervalo se convierte en una lista capaz de cambiar entre las otras listas
        listaS_eval.append(evaluar_formula_Simpson_adapatativo(intervalo[0],intervalo[1], funcion))   
    #calcular ajuste
    ajuste=(listaS_eval[contador+1]+listaS_eval[contador+2]-listaS_eval[contador])/15

    if ajuste<tolerancia: #Si se cumple la condicion del ajuste entonces se guarda en la lista de resultados para al final sumar los que cumplan
        Solucion_Listado.append((16*(listaS_eval[contador+1]+listaS_eval[contador+2])-listaS_eval[contador])/15)
    else: #Cada vez que no se cumpla un ajuste deben crearse 2 intervalos mas, partiendo de uno existente.
        a1=listaintervalos[contador+1][0]
        b1=listaintervalos[contador+1][1]
        puntomedio1=(a1+b1)/2
        a2=listaintervalos[contador+2][0]
        b2=listaintervalos[contador+2][1]
        puntomedio2=(a2+b2)/2

        while variable_de_control==0:
            listaS_eval=[]
            control=0
            #agregarintervalos
            #Para mantener el orden ys eguir la logica insertaremos los 3 intervalos (los dos nuevos y el que venia)
            listaintervalos.append([a1,b1])
            listaintervalos.append([a1,puntomedio1])
            listaintervalos.append([puntomedio1,b1])
            listaintervalos.append([a2,b2])
            listaintervalos.append([a2,puntomedio2])
            listaintervalos.append([puntomedio2,b2])
            
            for intervalo in listaintervalos:
                listaS_eval.append(evaluar_formula_Simpson_adapatativo(intervalo[0], intervalo[1], funcion))
                control+=1 #control define cual es la ultima insercion 

                '''
                EJEMPLO:

                inicialmente se tienen 3 intervalos, como no se logra solucionar con esos, se crean 6 mas 

                al momento de evaluar y obtener los S(a,b), control cuenta y guarda el numero de la ultima insercion (partiendo que inicialmente habran 3),
                con ello, definimos qué valores tomará a y b 

                SEPARAMOS a1 & a2

                la razon es que por cada ajuste fallido, se crean dos subdivisiones, entonces se destino una a,b,puntomedio  para cada rama

                '''
            #calcular ajustes
            ajuste=(listaS_eval[control-5]+listaS_eval[control-4]-listaS_eval[control-6])/15

            if ajuste<tolerancia:#Si se cumple la condicion del ajuste entonces se guarda en la lista de resultados para al final sumar los que cumplan
                Solucion_Listado.append((16*(listaS_eval[control-5]+listaS_eval[control-4])-listaS_eval[control-6])/15)
                variable_de_control=1
            else:
                variable_de_control=0
                a1=listaintervalos[control-5][0]
                b1=listaintervalos[control-5][1]
                puntomedio1=(a1+b1)/2
                a2=listaintervalos[control-4][0]
                b2=listaintervalos[control-4][1]
                puntomedio2=(a2+b2)/2
            
            ajuste=(listaS_eval[control-2]+listaS_eval[control-1]-listaS_eval[control-3])/15

            if ajuste<tolerancia:
                Solucion_Listado.append((16*(listaS_eval[control-2]+listaS_eval[control-1])-listaS_eval[control-3])/15)
                variable_de_control=1
            else:
                variable_de_control=0
                a1=listaintervalos[control-2][0]
                b1=listaintervalos[control-2][1]
                puntomedio1=(a1+b1)/2
                a2=listaintervalos[control-1][0]
                b2=listaintervalos[control-1][1]
                puntomedio2=(a2+b2)/2
    
    

    #el resultado de la integral es la suma de  los calculos de ajuste que cumplan con la condicion
    Solucion_Listado= sum(Solucion_Listado)

    return Solucion_Listado    

def integracion_Boole(a,b,funcion):  

    Solucion_Listado=[]
    h=(b-a)/4
    puntos=[]
    p=a
    for punto in range(5):
        puntos.append(p)
        p+=h
        
    Solucion_Listado = ((2*h)/45)*((7*Sustituir_y_Evaluar_Funcion(funcion, puntos[0],0,0))+(32*Sustituir_y_Evaluar_Funcion(funcion, puntos[1],0,0))+(12*Sustituir_y_Evaluar_Funcion(funcion, puntos[2],0,0))+(32*Sustituir_y_Evaluar_Funcion(funcion, puntos[3],0,0))+(7*Sustituir_y_Evaluar_Funcion(funcion, puntos[4],0,0)))
    
    return Solucion_Listado