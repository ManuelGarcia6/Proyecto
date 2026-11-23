# Proyecto Agape - entradas.py

"""
Biblioteca entradas: funciones que piden datos al usuario y los validan con
ciclos while (numeros dentro de un rango, textos que no esten vacios y
fechas que existan en el calendario).
"""

from constantes import MESES_DEL_ANIO, ANIO_MINIMO, ANIO_MAXIMO
import fechas


def pedir_entero(mensaje, minimo, maximo):
    """
    (uso de ciclo while, uso de funciones)
    recibe: mensaje (string), minimo (entero), maximo (entero)
    muestra el mensaje y lee un texto; mientras no sea un numero entero
    dentro del rango, avisa del error y vuelve a preguntar
    (se revisa con isdecimal() antes de convertir, asi un texto como
    "abc" o un Enter vacio no truena el programa)
    devuelve: numero valido entre minimo y maximo, (entero)
    """
    print(mensaje)
    texto = input()
    while (not texto.isdecimal()
           or int(texto) < minimo or int(texto) > maximo):
        print("Valor no valido, escribe un numero entre "
              + str(minimo) + " y " + str(maximo))
        print(mensaje)
        texto = input()
    return int(texto)


def pedir_texto(mensaje):
    """
    (uso de ciclo while, uso de funciones)
    recibe: mensaje (string)
    muestra el mensaje y lee un texto; mientras este vacio, vuelve a
    preguntar
    devuelve: texto no vacio, (string)
    """
    print(mensaje)
    texto = input()
    while texto == "":
        print("Este dato no puede quedar vacio.")
        print(mensaje)
        texto = input()
    return texto


def pedir_dia_mes(descripcion):
    """
    (uso de funciones, funcion que llama a otra funcion con while)
    recibe: descripcion (string), por ejemplo "de su cumpleanios"
    pide primero el dia (1 a 31) y despues el mes; como el dia se captura
    antes que el mes, un ciclo while revisa que el dia exista en ese mes
    y, si no, vuelve a pedir ambos
    devuelve: dia y mes validos, (dos enteros)
    """
    dia = pedir_entero("Dia " + descripcion + " (1 a 31):", 1, 31)
    mes = pedir_entero("Mes " + descripcion + " (1 a 12):",
                       1, MESES_DEL_ANIO)
    while dia > fechas.dias_en_mes(mes):
        print("Ese mes no tiene " + str(dia) + " dias, "
              + "escribe la fecha de nuevo.")
        dia = pedir_entero("Dia " + descripcion + " (1 a 31):", 1, 31)
        mes = pedir_entero("Mes " + descripcion + " (1 a 12):",
                           1, MESES_DEL_ANIO)
    return dia, mes


def pedir_fecha(descripcion):
    """
    (uso de funciones, funcion que llama a otra funcion con while)
    recibe: descripcion (string), por ejemplo "de hoy"
    pide mes, dia y anio validos de una fecha completa
    devuelve: dia, mes y anio, (tres enteros)
    """
    dia, mes = pedir_dia_mes(descripcion)
    anio = pedir_entero("Anio " + descripcion + " (ej. 2026):",
                        ANIO_MINIMO, ANIO_MAXIMO)
    return dia, mes, anio