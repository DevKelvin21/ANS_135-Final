import sympy as Sympy
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth
from numpy.polynomial import Polynomial as P
from sympy.simplify.radsimp import numer

x, e, y, z = Sympy.symbols('x e y z')

#Función para validar que los valores inicales de algunas funciones sean numeros
def Validar_Valores_Iniciales(x):
    variable_de_control = 0
    try:
        salida = float(x)
        variable_de_control = 1
    except:
        variable_de_control = 0
    if variable_de_control == 1:
        return salida
    else:
        return "Error"

#Valida que las cifras significativas sea un numero entero
def Validar_Cifras_Significativas(cifras):
    variable_de_control = 0
    while variable_de_control == 0:
        try:
            cifras = int(cifras)
            variable_de_control = 1
        except:
            variable_de_control = 0
        if variable_de_control == 1:
            return cifras
        else:
            return "Error"

#Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):
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
        return "Error"

#Devuelve los coeficientes del polinomio que se pase como parametros, utiliza RegEx para hacerlo
def Obtener_Coeficientes(entrada):
    regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
    c = {}
    for coef, x, exp in re.findall(regexp, entrada):
        # print(coef, x, exp)
        if not coef and not x:
            continue
        if x and not coef:
            coef = '1'
        if x and coef == "-":
            coef = "-1"
        if x and not exp:
            exp = '1'
        if coef and not x:
            exp = '0'
        exp = ord(exp) & 0x000F
        c[exp] = float(coef)
    grado = max(c)
    coeficientes = [0.0] * (grado+1)
    for g, v in c.items():
        coeficientes[g] = v
    return coeficientes
