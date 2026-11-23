# Proyecto Agape - matrices.py

"""
Biblioteca matrices: funciones para crear matrices y para armar y mostrar el
calendario del mes como una matriz de 6 renglones (semanas) por 7
columnas (dias de la semana, de lunes a domingo).
"""

import calendar
from constantes import (CALENDARIO_RENGLONES, CALENDARIO_COLUMNAS,
                        DIA_CUMPLE, MES_CUMPLE)
import fechas


def crear_matriz(renglones, columnas, valor):
    """
    (uso de listas anidadas, ciclos anidados, uso de funciones)
    recibe: renglones (entero), columnas (entero), valor (cualquier dato)
    crea una matriz de renglones x columnas con el valor en cada celda;
    cada renglon se arma por separado para que sean listas distintas
    devuelve: matriz, (lista de listas)
    """
    matriz = []
    for ren in range(renglones):
        renglon = []
        for col in range(columnas):
            renglon.append(valor)
        matriz.append(renglon)
    return matriz


def crear_calendario(mes, anio):
    """
    (uso de matrices, ciclo for, uso de condicionales, uso de funciones)
    recibe: mes (entero del 1 al 12), anio (entero)
    crea una matriz de 6 renglones (semanas) x 7 columnas (lunes a
    domingo) y coloca cada dia del mes en su celda; las celdas sin dia
    quedan en 0. La biblioteca calendar solo se usa para saber en que
    dia de la semana empieza el mes (0 = lunes) y cuantos dias tiene
    devuelve: calendario, (matriz de enteros)
    """
    primer_dia, total_dias = calendar.monthrange(anio, mes)
    calendario = crear_matriz(CALENDARIO_RENGLONES,
                              CALENDARIO_COLUMNAS, 0)
    renglon = 0
    columna = primer_dia
    for dia in range(1, total_dias + 1):
        calendario[renglon][columna] = dia
        columna = columna + 1
        if columna == CALENDARIO_COLUMNAS:
            columna = 0
            renglon = renglon + 1
    return calendario


def hay_cumple_en_dia(amigos, dia, mes):
    """
    (uso de listas, ciclo for, uso de funciones)
    recibe: amigos (lista de listas), dia y mes (enteros)
    revisa si algun amigo cumple anios en esa fecha
    devuelve: True si hay alguno, False si no (booleano)
    """
    for amigo in amigos:
        if amigo[DIA_CUMPLE] == dia and amigo[MES_CUMPLE] == mes:
            return True
    return False


def mostrar_calendario(calendario, amigos, mes, anio):
    """
    (uso de matrices, ciclos anidados, condicionales, uso de funciones)
    recibe: calendario (matriz de enteros), amigos (lista de listas),
    mes y anio (enteros)
    imprime la matriz como cuadricula de lunes a domingo y marca con un
    asterisco los dias en que algun amigo cumple anios
    no devuelve nada
    """
    print("\n" + fechas.nombre_del_mes(mes) + " " + str(anio))
    print("Lu  Ma  Mi  Ju  Vi  Sa  Do")
    for ren in range(CALENDARIO_RENGLONES):
        linea = ""
        for col in range(CALENDARIO_COLUMNAS):
            dia = calendario[ren][col]
            if dia == 0:
                celda = "    "
            elif hay_cumple_en_dia(amigos, dia, mes):
                celda = str(dia).rjust(2) + "* "
            else:
                celda = str(dia).rjust(2) + "  "
            linea = linea + celda
        if linea.strip() != "":
            print(linea.rstrip())
    print("* = cumpleanios")