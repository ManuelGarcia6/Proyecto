# Proyecto Agape - archivos.py

"""
Biblioteca archivos: guarda la lista de amigos en el archivo amigos.txt y la
carga de nuevo al abrir el programa. Cada campo de cada amigo se escribe
en su propia linea del archivo, por lo que cada amigo ocupa 10 lineas.
El archivo se crea en la carpeta desde la que se ejecuta el programa.
"""

from constantes import (NOMBRE, DIA_CUMPLE, MES_CUMPLE, GUSTOS, ALERGIAS,
                        REGALOS, META, DIA_ULTIMA, MES_ULTIMA, ANIO_ULTIMA)

ARCHIVO_AMIGOS = "amigos.txt"
CAMPOS_POR_AMIGO = 10


def guardar_amigos(amigos):
    """
    (uso de archivos de texto, ciclos anidados, uso de funciones)
    recibe: amigos (lista de listas)
    abre amigos.txt en modo "w" (si ya existe, lo reemplaza) y escribe
    cada campo de cada amigo en su propia linea; los numeros se pasan a
    texto con str(). Se usa utf-8 para que los acentos y la enie se
    guarden bien
    no devuelve nada
    """
    archivo = open(ARCHIVO_AMIGOS, "w", encoding="utf-8")
    for amigo in amigos:
        for campo in amigo:
            archivo.write(str(campo) + "\n")
    archivo.close()


def cargar_amigos():
    """
    (uso de archivos de texto, ciclo for, uso de funciones)
    no recibe nada
    primero abre amigos.txt en modo "a" y lo cierra, solo para asegurar
    que exista (la primera vez no existe: el modo "a" lo crea vacio y, si
    ya existia, no borra nada). Despues lee todo el archivo con read() y
    lo separa en lineas con split(); cada 10 lineas forman un amigo y los
    campos numericos se convierten de texto a entero con int()
    devuelve: amigos (lista de listas), vacia si el archivo esta vacio
    """
    archivo = open(ARCHIVO_AMIGOS, "a")
    archivo.close()

    archivo = open(ARCHIVO_AMIGOS, "r", encoding="utf-8")
    lineas = archivo.read().split("\n")
    archivo.close()

    # al final del archivo sobra una linea vacia; la division entera (//)
    # cuenta solo los amigos completos
    cantidad = len(lineas) // CAMPOS_POR_AMIGO
    amigos = []
    for i in range(cantidad):
        inicio = i * CAMPOS_POR_AMIGO
        amigo = [lineas[inicio + NOMBRE],
                 int(lineas[inicio + DIA_CUMPLE]),
                 int(lineas[inicio + MES_CUMPLE]),
                 lineas[inicio + GUSTOS],
                 lineas[inicio + ALERGIAS],
                 lineas[inicio + REGALOS],
                 lineas[inicio + META],
                 int(lineas[inicio + DIA_ULTIMA]),
                 int(lineas[inicio + MES_ULTIMA]),
                 int(lineas[inicio + ANIO_ULTIMA])]
        amigos.append(amigo)
    return amigos
