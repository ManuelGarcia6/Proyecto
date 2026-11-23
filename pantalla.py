# Proyecto Agape - pantalla.py

"""
Biblioteca pantalla: funciones que solo imprimen informacion en la pantalla
(el menu principal y el expediente de un amigo). No piden datos al
usuario.
"""

from constantes import (ANCHO_DEL_MENU, NOMBRE, GUSTOS, ALERGIAS,
                        REGALOS, META)
import mensajes


def mostrar_menu():
    """
    (uso de funciones)
    no recibe nada
    imprime las opciones del menu principal
    no devuelve nada
    """
    print("\n" + "=" * ANCHO_DEL_MENU)
    print("       PROYECTO AGAPE: MENU PRINCIPAL")
    print("=" * ANCHO_DEL_MENU)
    print("1. Resumen de conexiones")
    print("2. Ver calendario de cumpleanios")
    print("3. Agregar nuevo amigo")
    print("4. Actualizar informacion del amigo")
    print("5. Registrar conversacion o saludo")
    print("6. Ver expediente del amigo")
    print("7. Salir")
    print("=" * ANCHO_DEL_MENU)


def mostrar_expediente(amigo):
    """
    (uso de listas, uso de funciones)
    recibe: amigo (lista con los 10 campos del registro)
    imprime la informacion personal guardada del amigo (gustos, alergias,
    regalos y meta; el cumpleanios y los dias sin hablar se consultan en
    las opciones 1 y 2)
    no devuelve nada
    """
    print("\n" + "-" * ANCHO_DEL_MENU)
    print("EXPEDIENTE DE " + amigo[NOMBRE])
    print("-" * ANCHO_DEL_MENU)
    print("Gustos: " + mensajes.texto_o_vacio(amigo[GUSTOS]))
    print("Alergias o restricciones: "
          + mensajes.texto_o_vacio(amigo[ALERGIAS]))
    print("Regalos pasados: " + mensajes.texto_o_vacio(amigo[REGALOS]))
    print("Meta actual: " + mensajes.texto_o_vacio(amigo[META]))
    print("-" * ANCHO_DEL_MENU)