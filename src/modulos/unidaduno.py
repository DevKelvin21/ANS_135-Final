import cmath
import math 
import sympy as Sympy

def calcularEa(xr, xrAnterior):
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

def metodo5(punto,cifras):
    Solucion_Listado = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 1

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Solucion_Listado.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Solucion_Listado.append([iteracion,1,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Solucion_Listado.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1
            

    return Solucion_Listado

def metodo6(punto,cifras):
    Solucion_Listado = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Solucion_Listado.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Solucion_Listado.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Solucion_Listado.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Solucion_Listado

def metodo7(punto,cifras):
    Solucion_Listado = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Solucion_Listado.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Solucion_Listado.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Solucion_Listado.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Solucion_Listado

def metodo7(punto,cifras):
    Solucion_Listado = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Solucion_Listado.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Solucion_Listado.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Solucion_Listado.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Solucion_Listado