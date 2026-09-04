# Proyecto Ágape

Contexto

Cada quien tiene un grupo de amigos al que le gustaría cuidar mejor de lo que lo cuida. Se olvidan cumpleaños, se regala dos veces lo mismo, se organiza una carne asada sin acordarse de que uno del grupo es alérgico al camarón y otro no come picante. No es falta de cariño, es falta de un lugar donde esté anotado.

El problema es de memoria y de organización, no de intención. Una persona puede sostener sin esfuerzo los detalles de tres o cuatro amistades cercanas, pero en cuanto el círculo crece a quince o veinte personas la información se dispersa entre conversaciones viejas, capturas de pantalla y recuerdos vagos. Termina guardada en el peor lugar posible: la cabeza de uno.

Este programa es una agenda personal de amistades. Guarda de cada persona su cumpleaños, sus gustos, sus alergias o restricciones, y el historial de lo que ya se le ha regalado. A partir de esa información calcula cuántos días faltan para cada cumpleaños, avisa cuáles caen en el mes en curso, permite buscar a alguien por nombre o por gusto, y sugiere ideas de regalo descartando lo que ya se regaló antes. El programa corre en terminal con Python 3 y guarda todo en un archivo de texto para que la información siga ahí la próxima vez que se abra.


Intento de pseudocódigo <br>
Estado Inicial <br>
1. nombres (Lista de textos con los nombres de tus amigos)<br>
2. días (Lista de números con el día del cumpleaños) <br>
3. meses (Lista de números con el mes del cumpleaños)<br>
4. gustos (Lista de textos con cosas que le agradan) <br>
5. regalos (Lista de textos con los regalos que ya les he entregado en el pasado) <br>
6. metas_momentos (Lista de textos para recordar sus proyectos o metas personales)<br>
7. ultimas_interacciones (Lista de fechas que guarda el útlimo día que mostraste interés o editaste su información)<br>

Procesos

//no estoy 100% seguro si esto se puede hacer en python <br>
Fase 1: Inicio de Sesión e Inicialización <br>
1. El programa te da la bienvenida y te pide escribir tu contraseña de acceso <br>
2. El programa busca el archivo "amigos.txt" en tu computadora <br>
- Si existe: Usa la contraseña para descifrar el archivo. Si la clave es correcta, lee los datos y los carga en 7 listas paralelas. Si la clave es incorrecta, avisa del error y se cierra por seguridad <br>
- Si no existe: Inicializa las 7 listas completamente vacías y muestra un mensaje: "Bienvenid@ a tu primer día en Proyecto Ágape" <br>
3. Obtiene la fecha actual del sistema. Muestra de inmediato un resumen rápido de los cumpleaños del mes actual y si hay algún amigo que requiera atención urgente.<br>

Fase 2: Menú Principal<br>
El programa mostrará este menú en pantalla y esperará a que elijas una opción: <br>
PROYECTO ÁGAPE: MENÚ PRINCIPAL <br>
1. Resumen de conexiones //Indicador sutil de contacto <br>
2. Ver calendario de cumpleaños //Solo del mes actual <br>
3. Agregar nuevo amigo <br>
4. Actualizar información de un amigo // Gustos, Regalos o Metas <br>
5. Registrar conversación o saludo rápido <br>
6. Buscar amigo //Ver detalles y sugerir regalos <br>
7. Guardar y Salir <br>

Fase 3: ¿Qué hace cada parte del Menú Principal?

Operación 1: Resumen de conexiones <br>
1. El programa obtiene la fecha de hoy <br>
2. Revisa a tus amigos uno por uno utilizando un contador <br>
3. Por cada amigo, resta la fecha de hoy menos su ultima_interaccion para saber cuántos días han transcurrido <br>
4. Si han pasado más de 15 días sin contacto , el programa elige una de estas recomendaciones de forma dinámica y la imprime en pantalla: <br>
- Opción A: "Oye, no hablas con [nombre] desde hace [x] días. ¿Que tal si le preguntas cómo va con su meta de [meta]?" <br>
- Opción B: "Hace [x] días que no sabes de [nombre]. Dado que le encanta [gustos]. ¿Por qué no le regalas algo del estilo?" <br>
- Opción C: "¿Qué tal si le preguntas algo nuevo a [nombre] hoy? No interactúan desde hace [x] días."
Si han pasado menos de 15 días, solo muestra un mensaje de "Conexión al día" <br>

Operación 2: Ver el Calendario de Cumpleaños <br>
1. El programa detecta automáticamente el año y mes en curso. <br>
2. Utiliza la librería de calendario interna de Python para imprimir de forma bonita la cuadrícula de días del mes actual. <br>
3. Recorre la lista de cumpleaños (días y meses). <br>
4. Si el mes de cumpleaños de un amigo coincide con el mes actual, extrae su día. <br>
5. Imprime abajo del calendario una lista ordenada: "Cumpleaños de este mes: [nombre] - Día [día] (Faltan [x] días".

Operación 3: Agregar nuevo amigo <br>
1. Te pide ingresar de forma ordenada: Nombre, día de cumpleaños, mes de cumpleaños, gustos, historial de regalos pasados (si tiene) y sus metas actuales. <br>
2. El programa toma la fecha del día de hoy como su primera ultima_interacción. <br>
3. Añade cada uno de estos datos al final de sus respectivas listas. (haciendo crecer la lista de n a n+1 elementos). <br>

Operación 4: Actualizar información de un amigo <br>
1. El programa te pide el nombre de la persona que quieres actulizar <br>
2. Busca al amigo en la lista de nombres. <br>
3. Si lo encuentra, te pregunta qué deseas cambiar: <br>
  - Agregar un gusto nuevo <br>
  - Registrar un nuevo regalo entregado <br>
  - Actualizar o añadir una meta/momento importante. <br>
4. una vez que guardas el cambio, el programa actualiza automáticamente su ultima_interaccion con la fecha de hoy. También el sistema te muestra un mensaje confirmando: "datos actualizados. Se ha registrado esta acción como una interacción reciente con tu amigo. <br>

Operación 5: Registrar conversación o saludo rápido <br>
1. Te pide el nombre del amigo con quien acabas de hablar. <br>
2. Si lo encuentra, actualiza de forma manual su fecha en ultimas_interacciones al día de hoy. Su indicado sutil de contacto se reiniciará inmediatamente a cero. <br>

Operación 6. Buscar amigo <br>
1. Ingresas el nombre de tu amigo. <br>
2. El programa busca su posición en las listas. <br>
3. Si lo encuentra, imprime toda su información en pantalla. <br>
4. Motor de sugerencias: <br>
  - El programa tiene un "catálago interno" de regalos genéricos agrupado por temas. <br>
  - Compara las opciones que coinciden con los gustos del amigo contra los que ya tienes guardado en su lista de regalos. <br>
  - Imprime únicamente las sugerencias de regalos que sean nuevas, ocultando cualquier idea que ya se le ha regalado con anterioridad. <br>

Operación 7. Guardar y Salir <br>
1. Tomas todas las 7 listas paralelas con la información que tienes en memoria. <br>
2. Sobreescribe el archivo local amigos.txt con la nueva info. <br>
3. Muestra un mensaje de despedida y se cierra de manera segura.
