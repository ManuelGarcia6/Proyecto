"""
Proyecto Agape - avance 9

Programa principal. Pide la fecha de hoy, carga los amigos guardados en
amigos.txt y muestra el menu. Cada vez que se agrega o se cambia algo, la
lista de amigos se guarda de nuevo en el archivo.
Este es el unico archivo que se ejecuta; los demas son bibliotecas que se
traen con import (constantes, fechas, mensajes, entradas, lista_amigos,
matrices, pantalla, opciones y archivos).
"""

from constantes import OPCION_SALIR, TOTAL_OPCIONES
import entradas
import pantalla
import opciones
import archivos

# --------------- Programa Principal ---------------
print("--- Fecha de hoy ---")
dia_actual, mes_actual, anio_actual = entradas.pedir_fecha("de hoy")

# lista de listas: cada elemento es el registro de un amigo; se cargan los
# que se guardaron la ultima vez en amigos.txt
amigos = archivos.cargar_amigos()

# ciclo while del menu:
opcion = 0
while opcion != OPCION_SALIR:
    pantalla.mostrar_menu()
    opcion = entradas.pedir_entero("Elige una opcion:", 1, TOTAL_OPCIONES)

    if opcion == 1:
        opciones.resumen_conexiones(amigos, dia_actual, mes_actual,
                                    anio_actual)
    elif opcion == 2:
        opciones.ver_cumpleanios_del_mes(amigos, dia_actual, mes_actual,
                                         anio_actual)
    elif opcion == 3:
        opciones.agregar_amigo(amigos, dia_actual, mes_actual, anio_actual)
        archivos.guardar_amigos(amigos)
    elif opcion == 4:
        opciones.actualizar_amigo(amigos, dia_actual, mes_actual,
                                  anio_actual)
        archivos.guardar_amigos(amigos)
    elif opcion == 5:
        opciones.registrar_conversacion(amigos, dia_actual, mes_actual,
                                        anio_actual)
        archivos.guardar_amigos(amigos)
    elif opcion == 6:
        opciones.ver_expediente(amigos)
    elif opcion == OPCION_SALIR:
        print("Saliendo")

    if opcion != OPCION_SALIR:
        input("\nPresiona Enter para volver al menu")
