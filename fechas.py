# Proyecto Agape - fechas.py

"""
Biblioteca  fechas: funciones para trabajar con fechas (dia del anio, dias
transcurridos, dias que faltan para un cumpleanios y nombre de un mes).
Se usa un anio de 365 dias, sin bisiestos.
"""

from constantes import DIAS_DEL_ANIO


def dia_del_anio(dia, mes):
    """
    (uso de condicionales, uso de funciones)
    recibe: dia (valor numerico entero),
    mes (valor numerico entero del 1 al 12)
    suma los dias de los meses anteriores al mes dado y le suma el dia
    (se usa un anio de 365 dias, sin bisiestos)
    devuelve: numero de dia del anio entre 1 y 365, (entero)
    """
    if mes == 1:
        acumulado = 0
    elif mes == 2:
        acumulado = 31
    elif mes == 3:
        acumulado = 59
    elif mes == 4:
        acumulado = 90
    elif mes == 5:
        acumulado = 120
    elif mes == 6:
        acumulado = 151
    elif mes == 7:
        acumulado = 181
    elif mes == 8:
        acumulado = 212
    elif mes == 9:
        acumulado = 243
    elif mes == 10:
        acumulado = 273
    elif mes == 11:
        acumulado = 304
    else:
        acumulado = 334
    return acumulado + dia


def dia_absoluto(dia, mes, anio):
    """
    (uso de operadores, uso de funciones)
    recibe: dia, mes, anio (enteros)
    cuenta los dias transcurridos desde el anio 1 hasta la fecha dada,
    usando anios de 365 dias; sirve para restar dos fechas de anios
    distintos
    devuelve: numero de dia absoluto, (entero)
    """
    return (anio - 1) * DIAS_DEL_ANIO + dia_del_anio(dia, mes)


def dias_en_mes(mes):
    """
    (uso de condicionales, uso de funciones)
    recibe: mes (entero del 1 al 12)
    revisa cuantos dias tiene el mes (febrero con 28, sin bisiestos)
    devuelve: dias del mes, (entero)
    """
    if mes == 2:
        return 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    else:
        return 31


def nombre_del_mes(mes):
    """
    (uso de condicionales, uso de funciones)
    recibe: mes (entero del 1 al 12)
    revisa que numero de mes es y elige su nombre
    devuelve: nombre del mes, (string)
    """
    if mes == 1:
        return "enero"
    elif mes == 2:
        return "febrero"
    elif mes == 3:
        return "marzo"
    elif mes == 4:
        return "abril"
    elif mes == 5:
        return "mayo"
    elif mes == 6:
        return "junio"
    elif mes == 7:
        return "julio"
    elif mes == 8:
        return "agosto"
    elif mes == 9:
        return "septiembre"
    elif mes == 10:
        return "octubre"
    elif mes == 11:
        return "noviembre"
    else:
        return "diciembre"


def dias_sin_hablar(dia_actual, mes_actual, anio_actual,
                    dia_ultima, mes_ultima, anio_ultima):
    """
    (uso de operadores, uso de funciones)
    recibe: fecha de hoy y fecha de la ultima interaccion
    (dia, mes y anio de cada una, enteros)
    resta el dia absoluto de la ultima interaccion al de hoy
    devuelve: dias transcurridos, (entero, negativo si la ultima
    interaccion es posterior a hoy)
    """
    hoy = dia_absoluto(dia_actual, mes_actual, anio_actual)
    ultima = dia_absoluto(dia_ultima, mes_ultima, anio_ultima)
    return hoy - ultima


def dias_para_cumple(dia_actual, mes_actual, dia_cumple, mes_cumple):
    """
    (uso de operadores, uso de condicionales, uso de funciones)
    recibe: dia_actual, mes_actual, dia_cumple, mes_cumple (enteros)
    resta el dia del anio de hoy al dia del anio del cumpleanios;
    si el resultado es negativo, el cumpleanios ya paso y se cuenta el
    del anio siguiente sumando 365
    devuelve: dias que faltan para el cumpleanios, (entero)
    """
    hoy = dia_del_anio(dia_actual, mes_actual)
    cumple = dia_del_anio(dia_cumple, mes_cumple)
    faltan = cumple - hoy
    if faltan < 0:
        faltan = faltan + DIAS_DEL_ANIO
    return faltan