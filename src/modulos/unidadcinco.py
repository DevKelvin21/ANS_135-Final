import decimal
from numpy.lib.shape_base import column_stack
import sympy as sp
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth, ln
from numpy.polynomial import Polynomial as P
from sympy.core.function import expand
from sympy.simplify.radsimp import fraction, numer
from fractions import Fraction
from sympy.solvers.ode.ode import dsolve
from sympy import*

x, e, y, z, t = sp.symbols('x e y z t')

# <-------------------------------- FUNCIONES NECESARIAS ------------------------------>
def Sustituir_y_Evaluar_Funcion(funcion, valor, valor2, seDeriva, ordenDerivada): #Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e), (y, valor2)])
            return resultado
    except:
        return "Error"



def evaluarFuncionTaylor(funcion, y_valor, t_valor):
    resultado = sp.sympify(funcion).subs([(y, y_valor), (t, t_valor)])
    return resultado

def encontrarDerivada(funcion, queDerivada):
    funcioon = sp.sympify(funcion)
    gxValor = sp.diff(funcioon, x, queDerivada)
    return gxValor

def encontrarDerivadaTaylor(funcion, queDerivada):
    funcioon = sp.sympify(funcion)
    gxValor = sp.diff(funcioon, t, queDerivada)
    return gxValor

# <-------------------------------- METODOS NUMERICOS ------------------------------>

# <-------------------------------- metodos de Euler ------------------------------>
def metodo_Euler_Adelante(funcion, x_Inicial, y_Inicial, x_Final, n_intervalos):

    # Variables a utilizar
    lista_Salida_Final = []
    lista_Salida_Final.append(["Iteracion","X","Yn"])  # Lista para guardar la salida mostrada en el formulario
    lista_X = []  # Lista para almacenar los valores de x
    lista_Y = []  # Lista para almacenar los valores de y
    h = (x_Final-x_Inicial)/n_intervalos  # Pasos para el siguiente x

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)

    # Agregamos la primera iteracion de la respuesta final
    lista_Salida_Final.append([str(1),str(lista_X[0]),str(lista_Y[0])])

    # Iniciamos las siguientes iteraciones
    for i in range(1, len(lista_X), 1):
        operacion = lista_Y[i-1]+h * \
            Sustituir_y_Evaluar_Funcion(funcion, lista_X[i-1], lista_Y[i-1], 0, 0)

        lista_Y.append(operacion)

        lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

    return lista_Salida_Final


def metodo_Euler_Atras(funcion, x_Inicial, y_Inicial, x_Final, n_intervalos):

    # Variables a utilizar
    lista_Salida_Final = []  # Lista para guardar la salida mostrada en el formulario
    lista_Salida_Final.append(["Iteracion","X","Yn"])
    lista_X = []  # Lista para almacenar los valores de x
    lista_Y = []  # Lista para almacenar los valores de y
    h = (x_Final-x_Inicial)/n_intervalos  # Pasos para el siguiente x
    lista_Ysupra = []

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)

    # Empezamos las iteraciones
    for i in range(0, len(lista_X)-1, 1):
        # Sacamos el valor de ý
        lista_Ysupra.append(
            lista_Y[i]+(h*Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)))

        # Luego sacamos Y
        lista_Y.append(
            lista_Y[i]+(h*Sustituir_y_Evaluar_Funcion(funcion, (lista_X[i]+h), lista_Ysupra[i], 0, 0)))

    for i in range(0, len(lista_X), 1):
        lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

    return(lista_Salida_Final)

def metodo_Euler_Centrado(funcion, x_Inicial, y_Inicial, x_Final, n_intervalos):

    # Variables a utilizar
    lista_Salida_Final = []  # Lista para guardar la salida mostrada en el formulario
    lista_Salida_Final.append(["Iteracion","X","Yn"])
    lista_X = []  # Lista para almacenar los valores de x
    lista_Y = []  # Lista para almacenar los valores de y
    h = (x_Final-x_Inicial)/n_intervalos  # Pasos para el siguiente x

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)

    # Empezamos las iteraciones
    for i in range(0, len(lista_X)-1, 1):
        # Luego sacamos Y
        lista_Y.append(
            lista_Y[i]+(h*Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)))

    for i in range(0, len(lista_X), 1):
        lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

    return(lista_Salida_Final)

def metodo_Euler_Mejorado(funcion, x_Inicial, y_Inicial, x_Final, n_intervalos):
    # Variables a utilizar
    lista_Salida_Final = []  # Lista para guardar la salida mostrada en el formulario
    lista_Salida_Final.append(["Iteracion","X","Yn"])
    lista_X = []  # Lista para almacenar los valores de x
    lista_Y = []  # Lista para almacenar los valores de y
    lista_Yasterisco = []  # Lista para almacenar los valores de y*
    h = (x_Final-x_Inicial)/n_intervalos  # Pasos para el siguiente x

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)

    # Empezamos las iteraciones
    for i in range(0, len(lista_X)-1, 1):
        # Encontramos Y*
        lista_Yasterisco.append(
            lista_Y[i]+h*Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0))

        # Luego sacamos Y
        lista_Y.append(
            lista_Y[i]+(h*((Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)+Sustituir_y_Evaluar_Funcion(funcion, lista_X[i]+h, lista_Yasterisco[i], 0, 0))/2)))

    for i in range(0, len(lista_X), 1):
        lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

    return(lista_Salida_Final)

# <-------------------------------- metodo de Taylor ------------------------------>


def metodo_Taylor(funcion,x_Inicial,y_inicial,x_Final, h, orden):

    listaResultados = [] #Aqui guardamos las respuesta 
    header = ['T','Yn']
    listaResultados.append(header)
    lista_derivadas = [] #Aqui vamos a guardar las derivadas de orden 1,2,3...
    derivada_variable = funcion
    lista_derivadas.append(funcion) #la funcion es la primera derivada por ende devemos agregarla

    for i in range(0,orden-1,1):
        if i == 0:
            derivada_variable = sp.simplify(funcion) + encontrarDerivadaTaylor(funcion,i+1)
            lista_derivadas.append(derivada_variable)
        else:
            derivada_variable = derivada_variable + encontrarDerivadaTaylor(funcion,i+1)
            lista_derivadas.append(derivada_variable)

    #formamos el polinomio para ir evaluando luego

    polinomio_evaluar = ''
    contador = 1

    for i in range(0,orden+1,1):
        if i == 0:
            polinomio_evaluar += str(y_inicial)
        elif i == 1:
            polinomio_evaluar +=  ' + (' + str((lista_derivadas[0])) + ')*' + str(h) 
        else:
            polinomio_evaluar +=  ' + (' + str(lista_derivadas[contador]) +  ')*' + str((h**contador)/math.factorial(contador))
            contador += 1

    #Esta variable controla que las evluaciones no sobrepasen el valor de x_Final
    control_evaluacion = x_Inicial 
    lista_valores_y = []
    lista_valores_y.append(y_inicial) #Agregamos el primer valor de y
    contador_2 = 0
    listaResultados.append([control_evaluacion,lista_valores_y[0]])


    while control_evaluacion < x_Final:
        lista_valores_y.append(evaluarFuncionTaylor(polinomio_evaluar,lista_valores_y[contador_2],control_evaluacion))
        control_evaluacion += h
        listaResultados.append([control_evaluacion,lista_valores_y[contador_2+1]])
        contador_2 += 1 
        
    return listaResultados

# <-------------------------------- metodo de Runge Kutta ------------------------------>

def metodo_Runge_Kutta(funcion, x_Inicial, y_Inicial, x_Final, n_Intervalos, orden, tipoRespuesta):

    # Variables utilizadas
    lista_Salida_Final = []  # Lista para mostrar la salida final
    lista_Salida_Final.append(["Iteracion","X","Yn"])
    lista_X = []  # Lista con los valores de x
    lista_Y = []  # Lista con valores de y
    h = (x_Final-x_Inicial)/n_Intervalos  # Pasos para el siguiente x
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_Intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)

    # Condicional si el usuario digita un orden el cual no manejamos
    # Solo es permitido de 2 a 4
    if orden > 4 or orden < 2:
        print("El orden digitado no es permitido")

    else:
        if orden == 2:
            for i in range(0, len(lista_X), 1):
                # Evaluamos los K
                k1 = Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)
                k2 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h), (lista_Y[i]+(k1*h)), 0, 0)

                # Agregamos las y
                lista_Y.append(lista_Y[i]+((1/2)*h*(k1+k2)))

            # Armamos la salida final
            
            for i in range(0, len(lista_X), 1):
                lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

            return lista_Salida_Final

        elif orden == 3:
            for i in range(0, len(lista_X), 1):
                # Evaluamos los K
                k1 = Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)

                k2 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h), (lista_Y[i]+((1/2)*k1*h)), 0, 0)

                k3 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h), (lista_Y[i]-(k1*h)+(2*k2*h)), 0, 0)

                # Agregamos las y
                lista_Y.append(lista_Y[i]+((h/6)*(k1+4*k2+k3)))

            # Armamos la salida final
            
            for i in range(0, len(lista_X), 1):
                lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

            

            return lista_Salida_Final

        else:  # Orden 4

            for i in range(0, len(lista_X), 1):
                # Evaluamos los K
                k1 = Sustituir_y_Evaluar_Funcion(funcion, lista_X[i], lista_Y[i], 0, 0)

                k2 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h/2), (lista_Y[i]+(((h*k1)/2))), 0, 0)

                k3 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h/2), (lista_Y[i]+(((h*k2)/2))), 0, 0)

                k4 = Sustituir_y_Evaluar_Funcion(
                    funcion, (lista_X[i]+h), (lista_Y[i]+((h)*k3)), 0, 0)

                # Agregamos las y
                lista_Y.append(lista_Y[i]+((h/6)*(k1+(2*k2)+(2*k3)+k4)))

            # Armamos la salida final
            
            for i in range(0, len(lista_X), 1):
                lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_Y[i])])

            if tipoRespuesta == 0:
                return lista_Salida_Final
            else:
                return lista_Y

# <-------------------------------- metodos de multipasos ------------------------------>

def Adam_Bashforth_Moulton(funcion, x_Inicial, y_Inicial, x_Final, n_Intervalos, pasos):
    # Con esta condicion controlaremos que el usuario ingrese un buen paso
    if pasos > 4 or pasos < 2:
        print("el metodo para esos pasos no esta permitido")

    else:

        # Variables utilizadas
        lista_Salida_Final = []  # Lista para mostrar la salida final
        lista_Salida_Final.append(["Iteracion","X","Yn"]) 
        lista_X = []  # Lista con los valores de x
        lista_YRunge = []  # Lista con valores de y sacados con el metodo runge
        lista_YPrima = []  # Lista con valores de y prima
        lista_YMultipasos = []  # Lista con valores de y multipasos
        h = (x_Final-x_Inicial)/n_Intervalos  # Pasos para el siguiente x
        yPrediccion = 0

        # Agregamos el primer x
        lista_X.append(x_Inicial)
        # Agregamos los x faltantes
        for i in range(1, n_Intervalos+1, 1):
            lista_X.append(lista_X[i-1]+h)

        # Encontramos los valores de yRunge por el metode de Runge Kutta
        for i in metodo_Runge_Kutta(funcion, x_Inicial, y_Inicial, x_Final, n_Intervalos, 4, 1):
            lista_YRunge.append(i)

        contador = 0
        for i in lista_YRunge:
            if contador == pasos:
                break
            else:
                lista_YMultipasos.append(i)
                contador += 1

        # print(lista_YRunge)

        if pasos == 2:

            print("")

        elif pasos == 3:
            print("")

        elif pasos == 4:
            # Sacamos los valores primos de Y
            for i in range(0, pasos, 1):
                lista_YPrima.append(Sustituir_y_Evaluar_Funcion(
                    funcion, lista_X[i], lista_YRunge[i], 0, 0))

            inicio = len(lista_YMultipasos)

            for i in range(inicio, len(lista_X), 1):
                yPrediccion = lista_YMultipasos[len(lista_YMultipasos)-1] + \
                    (h/24)*(55*lista_YPrima[len(lista_YPrima)-1]-59*lista_YPrima[len(lista_YPrima)-2] +
                            37*lista_YPrima[len(lista_YPrima)-3]-9*lista_YPrima[len(lista_YPrima)-4])
                lista_YPrima.append(Sustituir_y_Evaluar_Funcion(
                    funcion, lista_X[len(lista_YMultipasos)], yPrediccion, 0, 0))
                lista_YMultipasos.append(
                    lista_YMultipasos[len(lista_YMultipasos)-1] + (h/24)*(9*lista_YPrima[len(lista_YPrima)-1]+(19*lista_YPrima[len(lista_YPrima)-2])-(5*lista_YPrima[len(lista_YPrima)-3])+lista_YPrima[len(lista_YPrima)-4]))

            # Armamos la salida final
            lista_Salida_Final.append("PASO 4:\n")
            for i in range(0, len(lista_YMultipasos), 1):
                lista_Salida_Final.append([str(i+1),str(lista_X[i]),str(lista_YMultipasos[i])])


            return lista_Salida_Final


