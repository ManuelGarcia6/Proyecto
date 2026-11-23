# Proyecto Agape - opciones.py

"""
Modulo opciones: una funcion por cada opcion del menu principal. Cada
una usa las funciones de los demas modulos (fechas, mensajes, entradas,
lista_amigos, matrices y pantalla) para pedir datos, cambiar la lista de
amigos o mostrar informacion.
"""

from constantes import (NOMBRE, DIA_CUMPLE, MES_CUMPLE, GUSTOS, REGALOS,
                        META)
import fechas
import mensajes
import entradas
import lista_amigos
import matrices
import pantalla


def resumen_conexiones(amigos, dia_actual, mes_actual, anio_actual):
    """
    (uso de listas, ciclo for, uso de funciones)
    recibe: amigos (lista de listas), fecha de hoy (tres enteros)
    recorre todos los amigos e imprime el mensaje de conexion de cada uno
    no devuelve nada
    """
    if len(amigos) == 0:
        print("Todavia no hay amigos registrados.")
    for amigo in amigos:
        transcurridos = lista_amigos.dias_sin_hablar_amigo(
            amigo, dia_actual, mes_actual, anio_actual)
        print(mensajes.mensaje_conexion(amigo[NOMBRE], transcurridos))


def ver_cumpleanios_del_mes(amigos, dia_actual, mes_actual, anio_actual):
    """
    (uso de matrices, listas, ciclo for, condicionales, uso de funciones)
    recibe: amigos (lista de listas), fecha de hoy (tres enteros)
    arma e imprime el calendario del mes actual y debajo la lista de
    amigos cuyo cumpleanios cae en ese mes, con los dias que faltan
    no devuelve nada
    """
    calendario = matrices.crear_calendario(mes_actual, anio_actual)
    matrices.mostrar_calendario(calendario, amigos, mes_actual, anio_actual)
    print("\nCumpleanios de " + fechas.nombre_del_mes(mes_actual) + ":")
    hay_alguno = False
    for amigo in amigos:
        if amigo[MES_CUMPLE] == mes_actual:
            faltan = fechas.dias_para_cumple(dia_actual, mes_actual,
                                             amigo[DIA_CUMPLE],
                                             amigo[MES_CUMPLE])
            print(amigo[NOMBRE] + " - dia " + str(amigo[DIA_CUMPLE])
                  + " (faltan " + str(faltan) + " dias)")
            hay_alguno = True
    if not hay_alguno:
        print("Nadie cumple anios este mes.")


def agregar_amigo(amigos, dia_actual, mes_actual, anio_actual):
    """
    (uso de listas, listas anidadas, append, ciclo while, funciones)
    recibe: amigos (lista de listas), fecha de hoy (tres enteros)
    pide los datos de un amigo nuevo (el nombre no se puede repetir),
    arma su registro como una lista y lo agrega al final de amigos
    no devuelve nada
    """
    nombre = entradas.pedir_texto("Nombre del nuevo amigo:")
    while lista_amigos.buscar_indice(amigos, nombre) != -1:
        print("Ya existe un amigo con ese nombre.")
        nombre = entradas.pedir_texto("Nombre del nuevo amigo:")
    dia_cumple, mes_cumple = entradas.pedir_dia_mes("de su cumpleanios")

    # repite hasta que la ultima interaccion no sea posterior a hoy
    transcurridos = -1
    while transcurridos < 0:
        dia_ultima, mes_ultima, anio_ultima = entradas.pedir_fecha(
            "de tu ultima interaccion")
        transcurridos = fechas.dias_sin_hablar(dia_actual, mes_actual,
                                               anio_actual, dia_ultima,
                                               mes_ultima, anio_ultima)
        if transcurridos < 0:
            print("La ultima interaccion no puede ser posterior a hoy.")

    print("Cuales son sus gustos? (Enter si no sabes):")
    gustos = input()
    print("Alergias o restricciones (Enter si no tiene):")
    alergias = input()
    print("Regalos que ya le diste (Enter si ninguno):")
    regalos = input()
    print("Meta o proyecto actual (Enter si no sabes):")
    meta = input()

    amigo = [nombre, dia_cumple, mes_cumple, gustos, alergias, regalos,
             meta, dia_ultima, mes_ultima, anio_ultima]
    amigos.append(amigo)
    print(nombre + " se agrego a tu lista.")


def actualizar_amigo(amigos, dia_actual, mes_actual, anio_actual):
    """
    (uso de listas, condicionales, funciones)
    recibe: amigos (lista de listas), fecha de hoy (tres enteros)
    busca al amigo y permite agregar un gusto, registrar un regalo o
    cambiar su meta; despues registra hoy como su ultima interaccion
    no devuelve nada
    """
    indice = lista_amigos.pedir_indice_amigo(amigos)
    if indice != -1:
        amigo = amigos[indice]
        print("Que quieres cambiar?")
        print("1. Agregar un gusto")
        print("2. Registrar un regalo entregado")
        print("3. Actualizar su meta")
        cambio = entradas.pedir_entero("Elige una opcion:", 1, 3)
        if cambio == 1:
            nuevo = entradas.pedir_texto("Gusto nuevo:")
            amigo[GUSTOS] = mensajes.unir_texto(amigo[GUSTOS], nuevo)
        elif cambio == 2:
            nuevo = entradas.pedir_texto("Regalo entregado:")
            amigo[REGALOS] = mensajes.unir_texto(amigo[REGALOS], nuevo)
        else:
            amigo[META] = entradas.pedir_texto("Nueva meta:")
        lista_amigos.registrar_interaccion(amigo, dia_actual, mes_actual,
                                           anio_actual)
        print("Datos actualizados. Se registro esta accion como una "
              "interaccion reciente con " + amigo[NOMBRE] + ".")


def registrar_conversacion(amigos, dia_actual, mes_actual, anio_actual):
    """
    (uso de listas, condicionales, funciones)
    recibe: amigos (lista de listas), fecha de hoy (tres enteros)
    busca al amigo y guarda hoy como su ultima interaccion
    no devuelve nada
    """
    indice = lista_amigos.pedir_indice_amigo(amigos)
    if indice != -1:
        lista_amigos.registrar_interaccion(amigos[indice], dia_actual,
                                           mes_actual, anio_actual)
        print("Conversacion registrada con " + amigos[indice][NOMBRE] + ".")


def ver_expediente(amigos):
    """
    (uso de listas, condicionales, funciones)
    recibe: amigos (lista de listas)
    busca al amigo e imprime su expediente
    no devuelve nada
    """
    indice = lista_amigos.pedir_indice_amigo(amigos)
    if indice != -1:
        pantalla.mostrar_expediente(amigos[indice])