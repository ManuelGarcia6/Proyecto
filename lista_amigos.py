# Proyecto Agape - lista_amigos.py

"""
Biblioteca lista_amigos: funciones para buscar y actualizar amigos dentro de
la lista de listas, donde cada amigo es una lista y sus campos se
obtienen con las constantes de indice.
"""

from constantes import NOMBRE, DIA_ULTIMA, MES_ULTIMA, ANIO_ULTIMA
import fechas


def buscar_indice(amigos, nombre):
    """
    (uso de listas, uso de listas anidadas, ciclo for, uso de funciones)
    recibe: amigos (lista de listas), nombre (string)
    recorre la lista comparando el nombre de cada amigo con el buscado,
    sin importar mayusculas o minusculas
    devuelve: posicion del amigo en la lista, o -1 si no esta (entero)
    """
    for i in range(len(amigos)):
        if amigos[i][NOMBRE].lower() == nombre.lower():
            return i
    return -1


def pedir_indice_amigo(amigos):
    """
    (uso de listas, uso de funciones)
    recibe: amigos (lista de listas)
    pide el nombre de un amigo y lo busca en la lista; si no existe,
    avisa
    devuelve: posicion del amigo en la lista, o -1 si no esta (entero)
    """
    print("Nombre del amigo:")
    nombre = input()
    indice = buscar_indice(amigos, nombre)
    if indice == -1:
        print("No se encontro a " + nombre + ".")
    return indice


def registrar_interaccion(amigo, dia, mes, anio):
    """
    (uso de listas, uso de funciones)
    recibe: amigo (lista), dia, mes, anio (enteros)
    guarda la fecha dada como ultima interaccion del amigo
    no devuelve nada
    """
    amigo[DIA_ULTIMA] = dia
    amigo[MES_ULTIMA] = mes
    amigo[ANIO_ULTIMA] = anio


def dias_sin_hablar_amigo(amigo, dia_actual, mes_actual, anio_actual):
    """
    (uso de listas, uso de funciones)
    recibe: amigo (lista), fecha de hoy (tres enteros)
    calcula los dias desde la ultima interaccion guardada en el amigo
    devuelve: dias transcurridos, (entero)
    """
    return fechas.dias_sin_hablar(dia_actual, mes_actual, anio_actual,
                                  amigo[DIA_ULTIMA], amigo[MES_ULTIMA],
                                  amigo[ANIO_ULTIMA])