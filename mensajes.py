# Proyecto Agape - mensajes.py

"""
Biblioteca mensajes: funciones que arman o preparan textos para mostrar al
usuario (aviso de conexion con un amigo, texto vacio y union de textos).
"""

from constantes import LIMITE_DE_DIAS_SIN_HABLAR


def mensaje_conexion(nombre, dias_transcurridos):
    """
    (uso de condicionales, uso de funciones)
    recibe: nombre (string), dias_transcurridos (valor numerico)
    si pasaron mas de 15 dias sin hablar, pone un aviso con los dias;
    si no, pone un mensaje de que la conexion esta al dia
    devuelve: mensaje, (string)
    """
    if dias_transcurridos > LIMITE_DE_DIAS_SIN_HABLAR:
        return ("Hace " + str(dias_transcurridos)
                + " dias que no hablas con " + nombre)
    else:
        return "Conexion al dia con " + nombre


def texto_o_vacio(texto):
    """
    (uso de condicionales, uso de funciones)
    recibe: texto (string)
    revisa si el texto esta vacio
    devuelve: "Sin registrar" si esta vacio, o el mismo texto si no (string)
    """
    if texto == "":
        return "Sin registrar"
    else:
        return texto


def unir_texto(texto_actual, texto_nuevo):
    """
    (uso de condicionales, uso de funciones)
    recibe: texto_actual (string), texto_nuevo (string)
    agrega el texto nuevo al final separado por coma; si el texto actual
    esta vacio, devuelve solo el nuevo
    devuelve: texto unido, (string)
    """
    if texto_actual == "":
        return texto_nuevo
    else:
        return texto_actual + ", " + texto_nuevo