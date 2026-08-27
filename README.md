# Proyecto Ágape

Contexto

Cada quien tiene un grupo de amigos al que le gustaría cuidar mejor de lo que lo cuida. Se olvidan cumpleaños, se regala dos veces lo mismo, se organiza una carne asada sin acordarse de que uno del grupo es alérgico al camarón y otro no come picante. No es falta de cariño, es falta de un lugar donde esté anotado.

El problema es de memoria y de organización, no de intención. Una persona puede sostener sin esfuerzo los detalles de tres o cuatro amistades cercanas, pero en cuanto el círculo crece a quince o veinte personas la información se dispersa entre conversaciones viejas, capturas de pantalla y recuerdos vagos. Termina guardada en el peor lugar posible: la cabeza de uno.

Este programa es una agenda personal de amistades. Guarda de cada persona su cumpleaños, sus gustos, sus alergias o restricciones, y el historial de lo que ya se le ha regalado. A partir de esa información calcula cuántos días faltan para cada cumpleaños, avisa cuáles caen en el mes en curso, permite buscar a alguien por nombre o por gusto, y sugiere ideas de regalo descartando lo que ya se regaló antes. El programa corre en terminal con Python 3 y guarda todo en un archivo de texto para que la información siga ahí la próxima vez que se abra.

Intento de pseudocódigo: <br>
nombres  = ["Ana", "Diego"] <br>
dias     = [14, 2]<br>
meses    = [9, 3]<br>
gustos   = ["chocolate", "futbol"]<br>
regalos  = ["libro", "ninguno"]<br>

Mi idea es algo así: Cuando el programa arranca, lo primero que hace es abrir el archivo donde están guardados los amigos y pasar toda esa información a las cinco listas que va a usar mientras corre. Enseguida revisa en qué mes estamos y muestra en pantalla a quiénes les toca cumpleaños este mes, como recordatorio.

Después entra a un ciclo del que no va a salir hasta que el usuario decida terminar. Dentro de ese ciclo imprime el menú con las cinco opciones disponibles y espera a que el usuario escriba un número.

Con ese número decide qué hacer. Si escribió 1, muestra la lista completa de amigos. Si escribió 2, pide los datos de una persona nueva y la agrega. Si escribió 3, pregunta un nombre y busca a esa persona. Si escribió 4, pregunta un mes y muestra quiénes cumplen años en él. Si escribió 5, guarda toda la información de vuelta en el archivo, se despide y el ciclo termina. Y si escribió cualquier otra cosa, avisa que la opción no es válida y vuelve a mostrar el menú sin hacer nada.

Mientras el usuario no elija salir, el programa repite ese proceso una y otra vez: mostrar el menú, leer la opción, ejecutar lo que corresponda, y volver a empezar.

y hasta ahí me quedé por ahorita en lo que se me ocurre como detallar
