import sympy as Sympy
import sympy as sp
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth
from numpy.polynomial import Polynomial as P
from sympy.simplify.radsimp import numer

x, e, y, z = Sympy.symbols('x e y z')

#♪-------------------------------------------- FUNCIONES NECESARIAS -----------------------------------------------------------------

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):#Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
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
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "Error"

def Calculo_Ea(xr, xrAnterior):#Calcula el Error absoluto
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

def ordenPolinomio(x,lista):
    listaResultados = []
    if x == 3:
        raicesFaltantes = factorizar(0, 0, lista[0], lista[1], lista[2])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])

                #Si es una funcion cubica
    elif x == 4:
        raicesFaltantes = factorizar(0,lista[0], lista[1], lista[2], lista[3])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])
        listaResultados.append(raicesFaltantes[2])

                #Si es una funcion cuadratica o bicuadrada
    elif x == 5:
        raicesFaltantes = factorizar(lista[0], lista[1], lista[2], lista[3], lista[4])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])
        listaResultados.append(raicesFaltantes[2])
        listaResultados.append(raicesFaltantes[3])

    return listaResultados
#♪-------------------------------------------- METODOS NUMERICOS VISTOS EN CLASE -----------------------------------------------------------------

def metodoBiseccion(x1, x2, func, cifr):
    
    funcion = func
    cifSig = cifr
    es = (10**(2-cifSig))/2
    ea = 0
    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "X1", "X2", "Xr", "F(x1)", "F(x2)", "F(x1)*F(Xr)", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1

    while salida == 0:
        if contador == 0:
            contador = 1
            xr = (x1 + x2) / 2
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            if fx1Porfxr == 0:
                Solucion_Listado.append(
                    [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr < 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    x2 = xr
                    valorAnterior = xr
                else:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    x1 = xr
                    valorAnterior = xr
        else:
            iteracion += 1
            xr = (x1 + x2) / 2
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            ea = Calculo_Ea(xr, valorAnterior)
            if ea < es:
                Solucion_Listado.append(
                    [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr == 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    salida = 1
                else:
                    if fx1Porfxr < 0:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                        x2 = xr
                        valorAnterior = xr
                    else:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                        x1 = xr
                        valorAnterior = xr

    return Solucion_Listado

def metodoFalsaPosicion(x1, x2, func, cifr):
    funcion = func
    cifSig = cifr
    es = (10 ** (2 - cifSig)) / 2
    ea = 0
    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "X1", "X2", "F(x1)", "F(x2)", "Xr", "F(xr)", "F(x1)*F(Xr)", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1

    while salida == 0:
        if contador == 0:
            contador += 1
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
            xr = x1-(fx1*(x1-x2)/(fx1-fx2))
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1*fxr
            if fx1Porfxr == 0:
                Solucion_Listado.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr > 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x1 = xr
                else:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x2 = xr
        else:
            iteracion += 1
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
            xr = x1 - (fx1 * (x1 - x2) / (fx1 - fx2))
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            ea = Calculo_Ea(xr, valorAnterior)
            if ea <= es:
                Solucion_Listado.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr == 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    salida = 1
                else:
                    if fx1Porfxr > 0:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x1 = xr
                    else:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x2 = xr

    return Solucion_Listado

def metodoPuntoFijo(x1, func, cif):
    funcion = func
    converge = Sustituir_y_Evaluar_Funcion(funcion, x1, 1, 1)
    converge = abs(converge)
    Solucion_Listado = []
    Solucion_Listado.append(["Iteracion", "X1", "g(x)", "Ea"])

    if converge < 1:
        cifSig = cif
        es = (10 ** (2 - cifSig)) / 2
        ea = 0
        salida = 0
        iteracion = 1

        while salida == 0:
            gx = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 1)
            if gx == 0:
                print("Surgio un problema : \n La funcion g(x) no puede ser cero")
                salida = 1
            else:
                ea = Calculo_Ea(gx, x1)
                if ea < es:
                    Solucion_Listado.append([iteracion, x1, gx, ea])
                    salida = 1
                else:
                    Solucion_Listado.append([iteracion, x1, gx, ea])
                    x1 = gx
            iteracion += 1
    else:
        return Solucion_Listado

    return Solucion_Listado

def metodoNewtonRaphson(x1, func, cif):
    funcion = func
    valorFx = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 1)
    valorFxPrima = Sustituir_y_Evaluar_Funcion(funcion, x1, 1, 1)
    valorFxPrimaSegunda = Sustituir_y_Evaluar_Funcion(funcion, x1, 1, 2)

    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "Xn", "F(Xn)", "F´(Xn)", "Xn+1", "Ea"])

    convergencia = Sympy.simplify(
        abs((valorFx*valorFxPrimaSegunda)/(valorFxPrima)**2))
    
    if (convergencia > 0 and convergencia < 1):
        cifrasSig = cif
        es = (10**(2-cifrasSig))/2

        iteracion = 1
        salida = 0
        XnMasUno = 0
        Xn = x1
        ea = 0

        while salida == 0:
            valorFx = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, Xn, 0, 0))
            valorFxPrima = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, Xn, 1, 1))
            XnMasUno = Xn - (valorFx/valorFxPrima)
            ea = Sympy.simplify(Calculo_Ea(XnMasUno, Xn))
            if ea < es:
                Solucion_Listado.append(
                    [iteracion, Xn, valorFx, valorFxPrima, XnMasUno, ea])
                salida = 1
            else:
                Solucion_Listado.append(
                    [iteracion, Xn, valorFx, valorFxPrima, XnMasUno, ea])
                iteracion += 1
                Xn = XnMasUno

        return Solucion_Listado

    else:
        return Solucion_Listado

def metodoNewtonRaphsonMejorado(x1, func, cif):
    funcion = func
    valorFx = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 1)
    valorFxPrima = Sustituir_y_Evaluar_Funcion(funcion, x1, 1, 1)
    valorFxPrimaSegunda = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, x1, 1, 2))

    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "Xn", "F(Xn)", "F´(Xn)", "Xn+1", "Xn+1", "Ea"])

    convergencia = Sympy.simplify(
        abs((valorFx*valorFxPrimaSegunda)/(valorFxPrima)**2))
    
    if (convergencia > 0 and convergencia < 1):
        cifrasSig = cif
        es = (10**(2-cifrasSig))/2
        iteracion = 1
        salida = 0
        XnMasUno = 0
        Xn = x1
        ea = 0

        while salida == 0:
            valorFx = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, Xn, 0, 0))
            valorFxPrima = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, Xn, 1, 1))
            valorFxPrimaSegunda = Sympy.simplify(
                Sustituir_y_Evaluar_Funcion(funcion, Xn, 1, 2))
            XnMasUno = Xn - ((valorFx*valorFxPrima) /
                             ((valorFxPrima**2)-(valorFx*valorFxPrimaSegunda)))
            ea = Sympy.simplify(Calculo_Ea(XnMasUno, Xn))
            
            if ea < es:
                Solucion_Listado.append(
                    [iteracion, Xn, valorFx, valorFxPrima, valorFxPrimaSegunda, XnMasUno, ea])
                salida = 1
            else:
                Solucion_Listado.append(
                    [iteracion, Xn, valorFx, valorFxPrima, valorFxPrimaSegunda, XnMasUno, ea])
                iteracion += 1
                Xn = XnMasUno

        return Solucion_Listado

    else:
        return Solucion_Listado

def metodoSecante(x1, x2, func, cif):
    funcion = func
    cifSig = cif
    es = (10 ** (2 - cifSig)) / 2
    ea = 0
    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "Xn-1", "Xn", "F(Xn-1)", "F(Xn)", "Xn+1", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1
    NmasUno = 0
    valorFuncionNmenosUno = 0
    valorFuncionN = 0

    existeRaiz = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0) * \
        Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
    if existeRaiz < 0:
        while salida == 0:
            if contador == 0:
                valorFuncionNmenosUno = Sympy.simplify(
                    Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0))
                valorFuncionN = Sympy.simplify(Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0))
                numerador = valorFuncionN*(x2-x1)
                denominador = valorFuncionN-valorFuncionNmenosUno
                NmasUno = x2-numerador/denominador
                Solucion_Listado.append(
                    [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                contador = 1
                x1 = x2
                x2 = NmasUno
                valorAnterior = NmasUno
            else:
                iteracion += 1
                valorFuncionNmenosUno = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
                valorFuncionN = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
                numerador = valorFuncionN*(x2-x1)
                denominador = valorFuncionN-valorFuncionNmenosUno
                NmasUno = x2-numerador/denominador
                ea = Calculo_Ea(NmasUno, valorAnterior)
                if ea < es:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                    salida = 1
                else:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                    x1 = x2
                    x2 = NmasUno
                    valorAnterior = NmasUno

        return Solucion_Listado
    else:
        return Solucion_Listado

def factorizacionSimple(a, b):
    Solucion_Listado = []
    raiz = (-1*b)/a
    Solucion_Listado.append(["Raiz:", raiz])
    return Solucion_Listado

def factorizarCuadratica(a, b, c):
    dd = b**2-4*a*c

    Solucion_Listado = []

    if dd == 0:  # solo una raiz
        raiz = -b/2*a
        Solucion_Listado.append(raiz)
    elif dd > 0:  # dos raices
        signo = 1
        for i in range(0, 2):
            numerador = -b+(MetRaiz(dd, 2))*signo
            denominador = 2*a
            raiz = numerador/denominador
            Solucion_Listado.append(raiz)
            signo = -1
    elif dd < 0:  # dos raices imaginarias
        signo = 1
        for i in range(0, 2):
            if dd < 0:
                if signo == 1:
                    primerTermino = -b/2*a
                    segundoTermino = (MetRaiz((dd*-1), 2))/2*a
                    salida = segundoTermino**2
                    segundoTerminoB = "%.2f" % float(salida)
                    raiz = str(primerTermino)+"+i√"+str(segundoTerminoB)
                    Solucion_Listado.append(raiz)
                else:
                    primerTermino = -b/2*a
                    segundoTermino = (MetRaiz((dd*-1), 2))/2*a
                    salida = segundoTermino**2
                    segundoTerminoB = "%.2f" % float(salida)
                    raiz = str(primerTermino)+"-i√"+str(segundoTerminoB)
                    Solucion_Listado.append(raiz)
                signo = -1

    return Solucion_Listado

def MetRaiz(radicando, indice):
    salida = float((radicando)**(1/indice))
    return salida

def factorizarBicuadradas(a, b, c):
    aa = float(a)
    bb = float(b)
    cc = float(c)

    dd = (bb**2)-4*aa*cc

    Solucion_Listado = []
    signo = 1

    if dd == 0.0:  # tenemos 2 raices que salen de una raiz
        for i in range(0, 2):
            raizNormal = -bb/2*aa
            if raizNormal < 0:
                raizNueva = (MetRaiz((raizNormal*-1), 2))*signo
                raizSalida = "%.2f" % float(raizNueva)
                salidaRaiz = "i "+str(raizSalida)
            Solucion_Listado.append(salidaRaiz)
            signo = -1

            # <------------------------------------------------------>
            # tendremos 4 raices las cuales derrivan de 2 raices al aplicar la formula cuadratica

    elif dd > 0.0:
        raices = []
        signo = 1
        Solucion_Listado = []

        # En este primer for calculamos las 2 raices iniciales:

        for i in range(0, 2):
            numerador = -bb+(dd**0.5)*signo
            denominador = 2*aa
            raiz = numerador/denominador
            if raiz < 0:
                raiz = raiz*-1
                raizSalida = "%.2f" % float(raiz)
                raices.append(raizSalida)
            else:
                raizSalida = "%.2f" % float(raiz)
                raices.append(raizSalida)

            signo = -1

        # Aqui calculamos las 4 resultantes :
        signo = 1

        for i in range(1, 5):
            if i < 3:
                if signo == 1:
                    raiz = raices[0]
                    raizNueva = "i√"+str(raiz)
                    Solucion_Listado.append(raizNueva)
                else:
                    raiz = raices[0]
                    raizNueva = "-i√"+str(raiz)
                    Solucion_Listado.append(raizNueva)
                signo = signo*-1
            else:
                if signo == 1:
                    raiz = raices[1]
                    raizNueva = "i√"+str(raiz)
                    Solucion_Listado.append(raizNueva)
                else:
                    raiz = raices[1]
                    raizNueva = "-i√"+str(raiz)
                    Solucion_Listado.append(raizNueva)
                signo = signo*-1

        return Solucion_Listado  # Hasta aqui todo funciona perfecto

        # <--------------------------------------------------------------------------->

        # Tendremos 4 raices que seran imaginarias al cuadrado por asi decirlo
    elif dd < 0.0:
        raices = []
        signo = 1
        Solucion_Listado = []

        # En este primer for calculamos las 2 raices iniciales:

        for i in range(0, 2):
            if dd < 0:
                if signo == 1:
                    primerTermino = -bb/2*aa
                    segundoTermino = (dd*-1)
                    segundoTerminoSalida = "%.2f" % float(segundoTermino)
                    raiz = str(primerTermino) + \
                        "+i√("+str(segundoTerminoSalida)+") / "+str(2*aa)
                    raices.append(raiz)
                else:
                    primerTermino = -bb/2*aa
                    segundoTermino = (dd*-1)
                    segundoTerminoSalida = "%.2f" % float(segundoTermino)
                    raiz = str(primerTermino) + \
                        "-i√("+str(segundoTerminoSalida)+") / "+str(2*aa)
                    raices.append(raiz)
                signo = -1

         # Aqui calculamos las 4 resultantes :
        signo = 1

        for i in range(1, 5):
            if i < 3:
                if signo == 1:
                    raiz = raices[0]
                    raizNueva = "i√("+str(raiz)+")"
                    Solucion_Listado.append(raizNueva)
                else:
                    raiz = raices[0]
                    raizNueva = "-i√("+str(raiz)+")"
                    Solucion_Listado.append(raizNueva)
                signo = signo*-1
            else:
                if signo == 1:
                    raiz = raices[1]
                    raizNueva = "i√("+str(raiz)+")"
                    Solucion_Listado.append(raizNueva)
                else:
                    raiz = raices[1]
                    raizNueva = "-i√("+str(raiz)+")"
                    Solucion_Listado.append(raizNueva)
                signo = signo*-1

        return Solucion_Listado

def factorizarCubicas(a, b, c, soloReal):

    Solucion_Listado = []

    p = ((3*b)-(a**2))/3
    q = (2*(a**3)-(9*a*b)+(27*c))/27

    descriminante = ((q/2)**2)+((p/3)**3)

    if(descriminante == 0):
        if(p == 0 and q == 0):
            x1 = "%.2f" % float(-a/3)
            if soloReal == 1:
                Solucion_Listado.append(x1)
            else:
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
        elif((p*q) != 0):
            x1 = "%.2f" % float((-(3*q)/(2*p))-(a/3))
            x2 = "%.2f" % float((((-4*(p**2))/9*q)-(a/3)))
            if soloReal == 1:
                Solucion_Listado.append(x1)
            else:
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x2)

    if(descriminante > 0):
        x01 = ((-q/2+(descriminante)**(0.5)))
        x02 = ((-q/2-(descriminante)**(0.5)))

        if x01 < 0:
            x01 = (x01*-1)**(1/3)*(-1)
        else:
            x01 = x01**(1/3)

        if x02 < 0:
            x02 = (x02*-1)**(1/3)*(-1)
        else:
            x02 = x02**(1/3)

        x1 = "%.5f" % float(x01+x02-(a/3))

        # solo devolvemos la raiz real para el metodo de factorizar cuarticas
        if soloReal == 1:
            Solucion_Listado.append(x1)
        else:
            u = (-q/2)+((descriminante)**(0.5))
            v = (-q/2)-((descriminante)**(0.5))

            if u < 0:
                u = (u*-1)**(1/3)*(-1)
            else:
                u = u**(1/3)

            if v < 0:
                v = (v*-1)**(1/3)*(-1)
            else:
                v = v**(1/3)

            x2 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"+" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"
            x3 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"-" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"

            Solucion_Listado.append(x1)
            Solucion_Listado.append(x2)
            Solucion_Listado.append(x3)

    if(descriminante < 0):

        teta = math.acos((-q/2)/(-(p/3)**3)**(1/2))
        x1 = 2*((-p/3)**(1/2))*math.cos((teta+2*0*math.pi)/3)-(a/3)
        x2 = 2*((-p/3)**(1/2))*math.cos((teta+2*1*math.pi)/3)-(a/3)
        x3 = 2*((-p/3)**(1/2))*math.cos((teta+2*2*math.pi)/3)-(a/3)

        if soloReal == 1:
            Solucion_Listado.append(x1)
        else:
            Solucion_Listado.append(x1)
            Solucion_Listado.append(x2)
            Solucion_Listado.append(x3)

    return Solucion_Listado

def factorizarCuarticas(a, b, c, d):
    Solucion_Listado = []
    p = ((8*b)-(3*a**2))/8
    q = ((8*c)-(4*a*b)+a**3)/8
    r = ((256*d)-(64*a*c)+(16*(a**2)*b)-(3*a**4))/256

    # Ahora vamos a resolver la ecuacion cubica : U^3-(p/2)*U^2-R*U + (4pR-Q^2)/8 = 0
    #       (p/2) = aa
    #           R = bb
    # (4pR-Q^2)/8 = cc

    aa = -p/2
    bb = -r
    cc = ((4*p*r)-q**2)/8

    u = factorizarCubicas(aa, bb, cc, 1)
    uu = float(u[0])

    v = ((2*uu)-p)**0.5
    w = (q)/(-2*v)

    # primero calcularemos si no nos dara imaginarias o si

    primerTermino = v**2-4*(uu-w)
    segundoTermino = v**2-4*(uu+w)

    if primerTermino < 0:
        primerTermino = primerTermino*-1
        x1 = str(v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x2 = str(v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x1 = (((v/2)+(primerTermino**0.5)/2))-(a/4)
        x1 = "%.2f" % float(x1)
        x2 = (((v/2)-(primerTermino**0.5)/2))-(a/4)
        x2 = "%.2f" % float(x2)

    if segundoTermino < 0:
        segundoTermino = segundoTermino*-1
        x3 = str(-v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x4 = str(-v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x3 = (((-v/2)+(segundoTermino**0.5)/2))-(a/4)
        x3 = "%.2f" % float(x3)
        x4 = (((-v/2)-(segundoTermino**0.5)/2))-(a/4)
        x4 = "%.2f" % float(x4)

    Solucion_Listado.append(x1)
    Solucion_Listado.append(x2)
    Solucion_Listado.append(x3)
    Solucion_Listado.append(x4)

    return Solucion_Listado

def factorizar(a, b, c, d, e):
    aa = float(a)  # Cuartas
    bb = float(b)  # Cubicas
    cc = float(c)  # Cuadrada
    dd = float(d)  # Normal
    ee = float(e)  # Independiente

    if aa == 0.0 and bb == 0.0 and cc == 0.0:
        factorizacionSimple(dd, ee)
    elif aa == 0.0 and bb == 0.0:
        listaResultado = factorizarCuadratica(cc, dd, ee)
    elif bb == 0.0 and dd == 0.0:
        if a != 1:
            nuevoB = cc/aa
            nuevoC = ee/aa
            listaResultado = factorizarBicuadradas(1, nuevoB, nuevoC)
        else:
            listaResultado = factorizarBicuadradas(aa, cc, ee)

    elif aa == 0.0:
        if a != 1:
            nuevoA = cc/bb
            nuevoB = dd/bb
            nuevoC = ee/bb
            listaResultado = factorizarCubicas(nuevoA, nuevoB, nuevoC, 0)
        else:
            listaResultado = factorizarCubicas(cc, dd, ee, 0)
    else:
        if a != 0.0:
            nuevoA = bb/aa
            nuevoB = cc/aa
            nuevoC = dd/aa
            nuevoD = ee/aa
            listaResultado = factorizarCuarticas(
                nuevoA, nuevoB, nuevoC, nuevoD)
        else:
            listaResultado = factorizarCuarticas(bb, cc, dd, ee)
    return listaResultado

def metodoHorner(lista, valorInicial, cifrasSignificativas):
    Solucion_Listado = []  # Lista de valores a mostrar en la lista que mira el usuario
    header = ["Iteracion", "Xi", "Xi+1", "R", "S", "Ea"]
    Solucion_Listado.append(header)
    lista.reverse()
    # La lista de coeficientes se mueve a otra lista de nombre mas claro
    listaCoeficientes = lista
    numeroMultiplicaciones = len(listaCoeficientes)
    iteracion = 0
    salida = 0
    es = 0.5*(10**(2-cifrasSignificativas))
    ea = 0
    valorAnterior = 0
    valorProximo = float(valorInicial)
    listaConResultados = []  # Lista donde se guardara el resultado de la division sintetica
    listaConResultados2 = []
    R = 0
    S = 0

    # <-----------Luego comenzamos a efectuar las divisiones sinteticas-------->

    while salida == 0:
        iteracion += 1
        listaConResultados.clear()
        listaConResultados2.clear()
        listaConResultados.append(listaCoeficientes[0])

        for i in range(1, numeroMultiplicaciones):  # Primera division sintetica
            listaConResultados.append(
                (listaConResultados[i-1] * valorProximo) + listaCoeficientes[i])
        R = "%.5f" % float(listaConResultados[len(listaConResultados)-1])

        listaConResultados2.append(listaCoeficientes[0])
        for i in range(1, numeroMultiplicaciones-1):  # Segunda division sintetica
            listaConResultados2.append(
                (listaConResultados2[i-1] * valorProximo) + listaConResultados[i])
        S = "%.5f" % float(listaConResultados2[len(listaConResultados2)-1])

        valorAnterior = valorProximo

        valorProximo = valorAnterior - (float(R)/float(S))

        ea = Calculo_Ea(valorProximo, valorAnterior)

        Solucion_Listado.append(
            [iteracion, valorAnterior, valorProximo, R, S, ea])

        if(ea <= es):
            salida = 1

    return Solucion_Listado

def metodoMuller(funcion, valor0, valor1, valor2, cifrasSignificativas):
    # Lista de valores a mostrar en la lista que mira el usuario
    Solucion_Listado = []
    header = ["Iteracion", "X0", "X1", "X2", "Xr", "EA"]
    Solucion_Listado.append(header)

    # Variables ocupadas
    iteracion = 0
    x0 = float(valor0)
    x1 = float(valor1)
    x2 = float(valor2)

    cifr = int(cifrasSignificativas)
    xr = 0.0
    ea = 0
    es = 0.5*(10**(2-cifr))
    salida = 0

    while salida == 0:
        iteracion += 1

        # Calculamos los valores iniciales en la funcion dada.
        fx0 = Sustituir_y_Evaluar_Funcion(funcion, x0, 0, 0)
        fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
        fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
        
        # Calculamos h0 y h1
        h0 = x1 - x0
        h1 = x2 - x1
        
        # Calculamos el valor del amperson
        ampersand0 = (fx1 - fx0) / h0
        ampersand1 = (fx2 - fx1) / h1
        
        # Calculamos a, b, c
        a = (ampersand1 - ampersand0) / (h1 + h0)
        b = a*h1 + ampersand1
        c = fx2

        # Calculamos el discriminante
        d = ((b**2) - (4*a*c))**(1/2)

        # Condicional para seleccionar signo del xr
        if(abs(b+d) > abs(b-d)):
            xr = x2 + ((-2*c)/(b+d))
        else:
            xr = x2 + ((-2*c)/(b-d))

        ea = Calculo_Ea(xr, x2)

        
        if(ea <= es):
            Solucion_Listado.append([iteracion, x0, x1, x2, xr, ea])
            salida = 1

        else:
            Solucion_Listado.append([iteracion, x0, x1, x2, xr, ea])
            x0 = x1
            x1 = x2
            x2 = xr

    return Solucion_Listado

def deSympyejarEcuaciones(valor1,valor2,valor3,valor4,valor5,valor6):
    #determinante total del sistema
    D = (valor1*valor5)-(valor4*valor2)

    #determinante de X
    Dx = (valor3*valor5)-(valor6*valor2)

    #determinante de Y
    Dy = (valor1*valor6)-(valor4*valor3)

    x1 = Dx/D #Primer Valor
    x2 = Dy/D #Segundo Valor

    lista = [x1,x2]
    return lista

def metodoBairstow(coeficientes,r,s,cifrasSig):

    largo = len(coeficientes)

    if largo <= 5:
        listaSalida = ordenPolinomio(largo,coeficientes)
        return listaSalida

    elif largo >5:

        try:

            #Variable salida controlara el bucle while hasta que se cumpla la condición
            salida = 0

            iteracion = 0

            #Esta lista sera la que contendra las respuestas 
            Solucion_Listado = []

            #Primero convertimos a número los valores de r y s  
            r = float(r)
            s = float(s)

            #Declaramos Ear y Eas y Es 
            E_ar = 0
            E_as = 0 
            Es = (10 ** (2 - cifrasSig)) / 2

            listaA = coeficientes #La lista a es igual a los coeficientes que acompañan a las X en la funcion
            listaB = []
            listaC = []
            #Primero creamos una variable para saber cuantas variables b y c tendremos
            while salida == 0:
                numeroVariables = len(listaA)

                #Debemos limpiar las listas siempre al inicio si no van a acumular los datos de todas las iteraciones
                listaB = []
                listaC = []

                iteracion += 1 
                #Ahora procedemos a llenar los valores de listaB 
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaB.append(listaA[i])
                    elif i == 1:
                        listaB.append(listaA[i] + r*listaB[0])
                    else:
                        listaB.append(listaA[i] + (r*listaB[i-1])+(s*listaB[i-2]))

                #Ahora procedemos a llenar los valores de listaC
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaC.append(listaB[i])
                    elif i == 1:
                        listaC.append(listaB[i] + r*listaC[0])
                    else:
                        listaC.append(listaB[i]+(r*listaC[i-1])+(s*listaC[i-2]))

                listaB.reverse()
                listaC.reverse()

                deltas = despejarEcuaciones(listaC[2], listaC[3], -1*listaB[1], listaC[1], listaC[2],-1*listaB[0])

                # Determinamos los valores actuales de R y S
                r = r + deltas[0]
                s = s + deltas[1]

                # Determinamos los errores
                E_ar = abs(deltas[0]/r)*100
                E_as = abs(deltas[1]/s)*100

                # Hacemos la validacion de si E_ar y E_as < Es salga del bucle
                if E_ar < Es and E_as < Es:

                    #Verificamos si obtendremos raices imaginarias
                    if (r**(2)+4*s) < 0:
                
                        listaA.reverse()
                        p = P(listaA)
                        raicesExtras = p.roots()
                        for x in range(len(raicesExtras)):
                            Solucion_Listado.append(raicesExtras[x])
                
                        salida = 1
                                              
                    #Si (r**2+4*s) > 0 no hay raices imaginarias 
                    else:
                        
                        x1 = "%.5f" % float((r+(r**2+4*s)**0.5)/2)
                        x2 = "%.5f" % float((r-(r**2+4*s)**0.5)/2)

                        #Las convertimos de nuevo a número
                        x1 = float(x1)
                        x2 = float(x2)

                        #Agregamos las primeras 2 raices a la lista de respuestas 
                        Solucion_Listado.append(x1)
                        Solucion_Listado.append(x2)

                        polinomioResultante = divisionSinteticaBairstown(listaA, x1, x2)                    
                        ordenPolinomioResultante = len(polinomioResultante)

                        #Si es una funcion mayor o igual a x^5
                        if ordenPolinomioResultante >= 6:

                            p = P(polinomioResultante)
                            raicesExtras = p.roots()

                            #Borramos los parentesis que nos agrega numpy y eliminamos la J cuando no es necesaria
                            tamanio = len(raicesExtras)-1
                            control = 0
                            salida2 = 1
                            

                            while salida2 == 1:
                                if control <= tamanio and control>=0 :
                                    salidaBuena = ""
                                    raizTexto = str(raicesExtras[control])

                                    for x in raizTexto:
                                        if x == "(" :
                                             salidaBuena += ""
                                        elif x == ")":
                                            salidaBuena += ""
                                        else:
                                            salidaBuena += x
                                            
                                    Solucion_Listado.append(salidaBuena)
                                    control = control + 1
                                else:
                                    salida2 = 0

                            salida = 1

                        #Si es una funcion menor o igual a x^4
                        else:
                            raiPo = ordenPolinomio(ordenPolinomioResultante, polinomioResultante)
                            for x in range(len(raiPo)):
                                Solucion_Listado.append(raiPo[x])
                            salida = 1
        except:
            print("Surgio un problema")
        #Lista con todas las raices encontradas
        return Solucion_Listado

def ordenPolinomio(x,lista):
    Solucion_Listado = []
    if x == 3:
        raicesFaltantes = factorizar(0, 0, lista[0], lista[1], lista[2])
        Solucion_Listado.append(raicesFaltantes[0])
        Solucion_Listado.append(raicesFaltantes[1])

                #Si es una funcion cubica
    elif x == 4:
        raicesFaltantes = factorizar(0,lista[0], lista[1], lista[2], lista[3])
        Solucion_Listado.append(raicesFaltantes[0])
        Solucion_Listado.append(raicesFaltantes[1])
        Solucion_Listado.append(raicesFaltantes[2])

                #Si es una funcion cuadratica o bicuadrada
    elif x == 5:
        raicesFaltantes = factorizar(lista[0], lista[1], lista[2], lista[3], lista[4])
        Solucion_Listado.append(raicesFaltantes[0])
        Solucion_Listado.append(raicesFaltantes[1])
        Solucion_Listado.append(raicesFaltantes[2])
        Solucion_Listado.append(raicesFaltantes[3])

    return Solucion_Listado
  
def divisionSinteticaBairstown(coeficientes,a,b):

    #En estas listas guardaremos los resultados al efectuar la division sintetica 
    primerosResultados = []
    segundosResultados = []

    #Numero de coeficientes del polinomio que viene desde bairstown
    numeroVariables = len(coeficientes)
    

    #Primera division 
    for i in range(0,numeroVariables-1):
        if i == 0:
            primerosResultados.append(coeficientes[i])
        else:
            primerosResultados.append((primerosResultados[i-1]*a)+coeficientes[i])

    #Segunda division
    for i in range(0,numeroVariables-2):
        if i == 0:
            segundosResultados.append(primerosResultados[i])
        else:
            segundosResultados.append((segundosResultados[i-1]*b)+primerosResultados[i])

    #La segunda lista es la que nos interesa 
    
    return segundosResultados