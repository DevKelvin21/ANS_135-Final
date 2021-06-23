from numpy.lib.shape_base import column_stack
import sympy as Sympy
import numpy as np
import sympy as sp
import math
import cmath
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


#♪-------------------------------------------- METODOS NUMERICOS VISTOS EN CLASE -----------------------------------------------------------------

def interpolacionLineal(puntos,xx):

    Solucion_Listado = []
    xx  = float(xx)
    x0 = float(puntos[0])
    y0 = float(puntos[1])
    x1 = float(puntos[2])
    y1 = float(puntos[3])
    polinomio = 0

    valorInterpolado = y0 + ((y1-y0)/(x1-x0))*(xx-x0)

    for i in range(0,2,1):
        if i == 0:
            polinomio = polinomio + y0
        else:
            polinomio = polinomio + ((y1-y0)/(x1-x0))*(x-x0)
    
    polinomioSimple = Sympy.expand(polinomio)
    Solucion_Listado.append(polinomioSimple)
    Solucion_Listado.append(valorInterpolado)

    return Solucion_Listado

def interpolacionCuadratica(puntosX, puntosY,valorX):

    Solucion_Listado = []

    xi = np.array(puntosX)
    fi = np.array(puntosY)
    
    xx = float(valorX)
    x0 = puntosX[0]
    x1 = puntosX[1]
    x2 = puntosX[2]
    y0 = puntosY[0]
    y1 = puntosY[1]
    y2 = puntosY[2]

    b0 = y0
    b1 = (y1-y0)/(x1-x0)
    b2 = (((y2-y1)/(x2-x1))-b1)/(x2-x0)

    n = len(xi)
    polinomio = 0
    for i in range(0,n,1):
        multiplicador = 1
        if i == 0:
            polinomio = polinomio + b0
        elif i == 1:
            polinomio = polinomio + b1*(x-x0)
        else:
            polinomio = polinomio + b2*(x-x0)*(x-x1)

    polinomioSimple = Sympy.expand(polinomio)
    salidaValor = Sustituir_y_Evaluar_Funcion(polinomioSimple, xx, 0, 0)

    Solucion_Listado.append(polinomioSimple)
    Solucion_Listado.append(salidaValor)

    return Solucion_Listado
   
def interpolacionLagrange(puntosX,puntosY,valor):

    Solucion_Listado = []

    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    polinomio = 0
    for i in range(0,n,1):
        numerador = 1
        denominador = 1
        for j in range(0,n,1):
            if i != j:
                numerador = numerador * (x-xi[j])
                denominador = denominador * (xi[i]-xi[j])
                
            termino = (numerador/denominador)*fi[i]
        polinomio = polinomio + termino 
    polinomioSimple = Sympy.expand(polinomio)

    valorSalida = Sustituir_y_Evaluar_Funcion(polinomioSimple, valor, 0, 0)
    
    Solucion_Listado.append(polinomioSimple)
    Solucion_Listado.append(valorSalida)

    return Solucion_Listado

def interpolacionNewton(puntosX,puntosY,valor):
    Solucion_Listado = []
   
 
    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    contador = 2 

    #Encontramos los valores de b
    listadeB = []
    listaApollo = []
    listaApollo2 = []
    n2 = len(xi)


    #Desde aca hasta la linea 1322 calculamos los valores de b
    for i in range(0,n,1):
        if i == 0:
            listadeB.append(fi[i])
        elif i == 1:
            #Encontramos b1
            for j in range(1,n,1):
                numerador = 1
                denominador = 1
                numerador = numerador*(fi[j]-fi[j-1])
                denominador = denominador*(xi[j]-xi[j-1])
                listaApollo.append(numerador/denominador)
                listaApollo2.append(numerador/denominador)
                
            listadeB.append(listaApollo[0])
            listaApollo = []

        else:
            for j in range(1,len(listaApollo2)):
                numerador = 1
                denominador = 1
                numerador = numerador*(listaApollo2[j]-listaApollo2[j-1])

                #Simplemente el contador ira aumentando en uno para traer los valores de la lista xi
                denominador = denominador*(xi[contador]-xi[contador-contador])
                listaApollo.append(numerador/denominador)

            #Aumentamos en uno el contador para controlar la posicion de la lista xi
            contador += 1

            listaApollo2 = []

            #Le asignamos los nuevos valores a listaApollo2
            for z in listaApollo:
                listaApollo2.append(z)

            #Agregamos el respectivo valor de b a la listadeB
            listadeB.append(listaApollo2[0])
            
            #Limpiamos la listaApollo para volver a iterar
            listaApollo = []

    #Desde aqui hasta la linea 1339 hacemos el calculo lineal de los valores de (Xn-Xn-1)---x(X0)
    listadeBLineal = []
    bLineal = 1
    contador2 = 2
    for i in range(0,n):
        if i == 0:
            listadeBLineal.append(1)
        elif i == 1:
            listadeBLineal.append((x-xi[i-1]))
        else:
            bLineal = 1
            for j in range(0,contador2):
                bLineal = bLineal*(x-xi[j])
            contador2 += 1
            listadeBLineal.append(bLineal)
    #Realizamos las multiplicaciones y generamos el polinomio simplificado como le gusta a la ing ^.^
    polinomio = 0 
    for i in range(0,len(listadeB)):
        polinomio = polinomio + listadeB[i]*listadeBLineal[i]
    polinomioSimple = Sympy.expand(polinomio)
    #Evaluamos el polinomio en el valor a interpolar 
    valorInterpolado = Sustituir_y_Evaluar_Funcion(polinomioSimple,valor,0,0) 
    Solucion_Listado.append(polinomioSimple)
    Solucion_Listado.append(valorInterpolado)

    return Solucion_Listado

def interpolacionHermite(lista_valores, punto_evaluar):
    # lista_valores contendra los valores de x,y y las derivadas ya sea la primera o la quinta
    valores_x = lista_valores[0]  # Lista de valores de x
    valores_y = lista_valores[1]  # lista de valores de y
    valores_derivadas = []  # lista de valores de derivadas dentro de una matriz
    Solucion_Listado = [] #lista que guardara el polinomio y el valor evaluado 
    # agregando derivadas a matriz: valores_derivadas
    for i in range(2, len(lista_valores), 1):
        # Si tiene una lista sera la primer derivada, si tiene 2 listas sera 1ra y 2da derivada
        valores_derivadas.append(lista_valores[i])
    # Creando tabla para sacar valores para los valores de b (b0,b1,b2)
    valores_b = []  # Se guardaran todos los valores de b (b0,b1,b2)
    columna_deX = []  # Aqui se guardaran los valores de x y sus repeticiones si tenen derivadas
    cualXEs = []  # Aqui se guardaran las posiciones de las x repetidamente, dependiendo de que fila sea
    # Se utilizara para repetir los valores de derivada que utilizaremos en la tabla mas adelante
    derivadasRepetidas = []
    columna_calculada = []  # Columna donde iran los valores calculados
    columna_siguiente = []  # valores proximos a la columna calculada
    # Agregando valores de la columna de X a columna_deX
    contador = 0
    contadorColumna = 0
    # Hasta cuantas derivadas hay de cada derivada
    for i in range(0, len(valores_derivadas[contador]), 1):
        cualXEs.append(i)
        # Agregando valores de la columna de X a columna_deX con todas sus repeticiones
        columna_deX.append(valores_x[contadorColumna])
        # Llenamos la columna_calculada con los valores de F(x) correspondientes
        columna_calculada.append(valores_y[contadorColumna])

        for j in range(0, len(valores_derivadas), 1):  # Hasta cuantas derivadas hay

            if valores_derivadas[j][i] == "":
                break
            else:
                cualXEs.append(i)
                # Agregando valores de la columna de X a columna_deX con todas sus repeticiones
                columna_deX.append(valores_x[contadorColumna])
                # Llenamos la columna_calculada con los valores de F(x) correspondientes
                columna_calculada.append(valores_y[contadorColumna])

                if j == 0:
                    # Agregamos las derivadas con sus respectivas repeticiones
                    derivadasRepetidas.append(valores_derivadas[j][i])
                    derivadasRepetidas.append(valores_derivadas[j][i])
                else:
                    derivadasRepetidas.append(valores_derivadas[j][i])

        contadorColumna += 1
        contador += 1
    # Realizamos operacion de la tabla para sacar los valores de B (b0,b1,b2 etc).

    # Variable que guardara el calculo de encontrar las operaciones de la tabla para luego asignarla a columna_siguiente
    valor = 0
    valores_b.append(columna_calculada[0])  # Agregamos b0 que es F(x0)
    contador = 1
    cualColumnaEs = 1
    cualFilaEs = 1

    for i in range(0, len(columna_deX)-1, 1):  # For para manejar columnas
        cualFilaEs = 1+i
        for j in range(0, len(columna_calculada)-1, 1):  # For para manejar filas
            # Calculamos operaciones de la tabla
            valor = 0
            try:
                if j == 0:
                    valor = (
                        columna_calculada[j+1]-columna_calculada[j])/(columna_deX[contador]-columna_deX[j])
                else:
                    valor = (
                        columna_calculada[j+1]-columna_calculada[j])/(columna_deX[contador]-columna_deX[j])
            # Si da indeterminacion colocamos el valor de su derivada/factorial(contador)
            except ZeroDivisionError:
                # Calculamos en que columna vamos para saber que derivada necesitamos
               # Operacion realizada si da 0/0
                for k in range(0, len(valores_derivadas), 1):
                    if k == (cualColumnaEs-1):
                        
                        valor = valores_derivadas[k][cualXEs[cualFilaEs]] \
                            / math.factorial(cualColumnaEs)

            if j == 0:  # Agregamos el valor inicial a los valores de b
                valores_b.append(valor)
            # Agregamos los valores de la columna siguiente
            columna_siguiente.append(valor)
            cualFilaEs += 1
            contador += 1
        contador = i+1
        # Limpiaremos la columna anterior y le asignaremos los valores de la columna siguiente
        columna_calculada = []
        for j in range(0, len(columna_siguiente), 1):
            columna_calculada.append(columna_siguiente[j])
        # Limpiamos la columna siguiente para calcularlos en la siguiente iteracion
        columna_siguiente = []
        contador += 1
        cualColumnaEs += 1
    # ------------Aca para abajo se arma el polinomio----------------- los valores de b estan en valores_b

    # Lista que tendra todas las multiplicaciones para repertirlas y armar el polinomio Ej:(x-x0)^2*(x-x1)
    multiplicaciones = []
    listaCuantos = []
    variableAyuda = 0
    polinomios = []
    contador = 0
    for i in range(0, len(valores_b), 1):  # Armando Polinomio

        if i == 0:
            # Agregamos el valor de b0 en el polinomio
            polinomio = valores_b[0]
            polinomios.append(valores_b[0])

        elif i == 1:
            variableAyuda = x-columna_deX[contador]
            polinomio = polinomio+((valores_b[i])*(x-columna_deX[contador]))
            polinomios.append((valores_b[i])*(x-columna_deX[contador]))
            contador += 1

        else:
            variableAyuda = ((variableAyuda) * (x-columna_deX[contador]))
            polinomio = polinomio+((valores_b[i])*(variableAyuda))
            polinomios.append((valores_b[i])*(variableAyuda))
            contador += 1

    polinomio2 = Sympy.expand(polinomio)
    Solucion_Listado.append(polinomio2)
    valorEvaluacion = Sustituir_y_Evaluar_Funcion(polinomio2,punto_evaluar,0,0)
    Solucion_Listado.append(valorEvaluacion)

    return Solucion_Listado
    
def resolverMatrices(lista,lista2): #metodo para resolver matrices
    #Los determinantes que usaremos
    #
    a = np.matrix(lista)
    b = np.matrix(lista2)

    Solucion_Listado = (a**-1)*b 

    return Solucion_Listado

def trazadoresCubicos(listaX, listaY, tipo,valor):

    Solucion_Listado = []
    intervalos = []
    intervalorsY = []

    n = len(listaX)
    a, b, c, d = Sympy.symbols('a b c d')

    # Creamos los intervalos con los que vamos a trabajar en sublistas
    # Esto se hace en todos los metodos entonces lo hacemos desde aqui
    for i in range(0, n-1, 1):
        intervalos.append([listaX[i], listaX[i+1]])
        intervalorsY.append([listaY[i], listaY[i+1]])

    if tipo == 0: #funcion spline grado cero
        solucionesEcuaciones = []
        for i in range(0, len(intervalos), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(listaY[i])
            solucionesEcuaciones.append(salida)

        for i in solucionesEcuaciones:
            Solucion_Listado.append(i)
        
        return Solucion_Listado

    elif tipo == 1: #funcion spline grado 1

        # Elnúmero de ecuaciones depende del numero de intervalos encontrados
        # De cada intervalo obtendremos 2 ecuaciones las cuales se resuelven entre ellas 2 de una vez

        ecuacionesSimbolicas = []
        soluciones = []

        # Encontramos los valores de a y b respectivamente
        contador = 0
        contador2 = 0

        for i in range(0, len(intervalos), 1):
            D = (intervalos[contador2][contador]*1) - \
                (intervalos[contador2][contador+1]*1)
            Dx = (intervalorsY[contador2][contador]*1) - \
                (intervalorsY[contador2][contador+1]*1)
            Dy = (intervalos[contador2][contador]*intervalorsY[contador2][contador+1]) - (
                intervalos[contador2][contador+1]*intervalorsY[contador2][contador])
            soluciones.append(Dx/D)
            soluciones.append(Dy/D)

            contador2 += 1

        contador3 = 0
        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                soluciones[contador3]*x+soluciones[contador3+1])
            contador3 += 2

        contador3 = 1
        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: ----> " +\
                    str(Sustituir_y_Evaluar_Funcion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            Solucion_Listado.append(i)
        return Solucion_Listado

    elif tipo == 2:  # Funciones spline grado 2

        # Lista que tendra ceros
        listaConCeros = []
        listaCon3Ceros = []

        # Estaran las ecuaciones finales ya con las variables (a,b,c,d) resueltas
        ecuacionesSimbolicas = []

        soluciones = []
        ecuaciones_Para_Matriz = []  # Lista con los valores de la matriz

        YParaMatriz = []  # Lista con los valores de Y para la matriz

        # Agregamos los valores de y a una lista que sera usada en la matriz
        for i in range(0, n-1, 1):
            YParaMatriz.append([listaY[i]])
            YParaMatriz.append([listaY[i+1]])
        # quitamos a0 por que la igualamos a 0
        for i in range(0, n-2, 1):
            YParaMatriz.append([0])

        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        # Agregamos una lista que tenga solamente 4 ceros
        for i in range(0, 3, 1):
            listaCon3Ceros.append(0)

        # Hacemos la lista con los datos para hacer la matriz (las variables: a b c)
        contador = 0
        columna = 0
        multiplicadorDeCeros = 0

        for i in range(0, len(intervalos)*2, 1):
            if i % 2 == 0 and i != 0:
                contador += 1
                multiplicadorDeCeros += 1
                for i in range(0, 3, 1):
                    listaConCeros.pop()

            if i < 2:
                ecuaciones_Para_Matriz.append(
                    [(intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)
            elif i >= 2:
                ecuaciones_Para_Matriz.append(
                    (listaCon3Ceros*multiplicadorDeCeros)+[(intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)

            if columna == 0:
                columna = 1
            elif columna == 1:
                columna = 0

        # Numero de variables al derivar = len(intervalos) - 1
        columna = 1
        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Primer derivada
            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [2*(intervalos[i][columna]), 1, 0, -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon3Ceros*multiplicadorDeCeros)+[2*(intervalos[i][columna]), 1, 0, -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 3, 1):
                    listaConCeros.pop()

        # Libres para igualar una variable a cero
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        # Eliminaremos a0 de ecuaciones_Para_Matriz, por que se iguala una variable a 0, entonces ya sabemos su valor
        for i in range(0, len(ecuaciones_Para_Matriz), 1):
            del ecuaciones_Para_Matriz[i][0]

        listaDeSoluciones = []  # Lista con las soluciones

        # Resolvemos la matriz llamando al metodo resolverMatrices, guardamos en soluciones
        # pero soluciones es una matriz por eso la pasamos a unas lista llamada listaDeSoluciones
        soluciones = resolverMatrices(
            ecuaciones_Para_Matriz, YParaMatriz)

        # Lista con las respuestas de las variables a b c d
        listaDeSoluciones = np.array(soluciones).flatten().tolist()

        # Le agregamos a0 que igualamos a cero antes de agregar los demas
        listaDeSoluciones[:0] = [0]

        # Aqui formamos las funciones spline ax+b
        contador3 = 0  # El contador nos servira para elegir los valores de a0 b0 c0 etc

        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                listaDeSoluciones[contador3]*x**2+listaDeSoluciones[contador3+1]*x+listaDeSoluciones[contador3+2])
            contador3 += 3

         # Aca unimos el intervalo con su funcion respectiva para mostrarlo.

        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: "+\
                    str(Sustituir_y_Evaluar_Funcion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            Solucion_Listado.append(i)
        return Solucion_Listado

    elif tipo == 3:  # Funciones spline grado 3

        # Lista que tendra ceros
        listaConCeros = []
        listaCon4Ceros = []

        # Estaran las ecuaciones finales ya con las variables (a,b,c,d) resueltas
        ecuacionesSimbolicas = []

        soluciones = []
        ecuaciones_Para_Matriz = []  # Lista con los valores de la matriz

        YParaMatriz = []  # Lista con los valores de Y para la matriz

        for i in range(0, n-1, 1):
            YParaMatriz.append([listaY[i]])
            YParaMatriz.append([listaY[i+1]])

        for i in range(0, n-1, 1):
            YParaMatriz.append([0])
            YParaMatriz.append([0])

        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        # Agregamos una lista que tenga solamente 4 ceros
        for i in range(0, 4, 1):
            listaCon4Ceros.append(0)

        # Hacemos la lista con los datos para hacer la matriz
        contador = 0
        columna = 0
        multiplicadorDeCeros = 0

        for i in range(0, len(intervalos)*2, 1):
            if i % 2 == 0 and i != 0:
                contador += 1
                multiplicadorDeCeros += 1
                for i in range(0, 4, 1):
                    listaConCeros.pop()

            if i < 2:
                ecuaciones_Para_Matriz.append(
                    [(intervalos[contador][columna]**3), (intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)
            elif i >= 2:
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[(intervalos[contador][columna]**3), (intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)

            if columna == 0:
                columna = 1
            elif columna == 1:
                columna = 0

        # Numero de variables al derivar = len(intervalos) - 1
        columna = 1
        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Primer derivada
            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [3*(intervalos[i][columna]**2), 2*(intervalos[i][columna]), 1, 0, -3*(intervalos[i+1][columna-1]**2), -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[3*(intervalos[i][columna]**2), 2*(intervalos[i][columna]), 1, 0, -3*(intervalos[i+1][columna-1]**2), -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 4, 1):
                    listaConCeros.pop()

        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Segunda derivada

            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [6*(intervalos[i][columna]), 2, 0, 0, -6*(intervalos[i+1][columna-1]), -2, 0, 0]+listaConCeros)

            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[6*(intervalos[i][columna]), 2, 0, 0, -6*(intervalos[i+1][columna-1]), -2, 0, 0]+listaConCeros)

            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 4, 1):
                    listaConCeros.pop()

        # Libres que igualamos a cero

        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        ecuaciones_Para_Matriz.append(
            [6*(intervalos[0][0]), 2, 0, 0]+listaConCeros)

        ecuaciones_Para_Matriz.append(
            listaConCeros+[6*(intervalos[len(intervalos)-1][1]), 2, 0, 0])

        listaDeSoluciones = []
        soluciones = resolverMatrices(
            ecuaciones_Para_Matriz, YParaMatriz)  # Resolvemos la matriz
        # Lista con las respuestas de las variables a b c d
        listaDeSoluciones = np.array(soluciones).flatten().tolist()

        # Aqui formamos las funciones spline ax+b
        contador3 = 0

        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                listaDeSoluciones[contador3]*x**3+listaDeSoluciones[contador3+1]*x**2+listaDeSoluciones[contador3+2]*x+listaDeSoluciones[contador3+3])
            contador3 += 4

         # Aca unimos el intervalo con su funcion respectiva para mostrarlo.
        contador3 = 1
        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: "+\
                    str(Sustituir_y_Evaluar_Funcion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            Solucion_Listado.append(i)
        return Solucion_Listado
