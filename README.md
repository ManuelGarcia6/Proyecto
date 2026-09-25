# Proyecto Ágape

## ¿Qué es el proyecto?

Cada quien tiene un grupo de amigos al que le gustaría cuidar mejor de lo que lo cuida. Se olvidan cumpleaños, se regala dos veces lo mismo, se organiza una carne asada sin acordarse de que uno del grupo es alérgico al camarón y otro no come picante. No es falta de cariño, es falta de un lugar donde esté anotado.

El problema es de memoria y de organización, no de intención. Una persona puede sostener sin esfuerzo los detalles de tres o cuatro amistades cercanas, pero en cuanto el círculo crece a quince o veinte personas la información se dispersa entre conversaciones viejas, capturas de pantalla y recuerdos vagos. Termina guardada en el peor lugar posible: la cabeza de uno.

Este programa es una agenda personal de amistades. Guarda de cada persona su cumpleaños, sus gustos, sus alergias o restricciones, y el historial de lo que ya se le ha regalado. A partir de esa información calcula cuántos días faltan para cada cumpleaños, avisa cuáles caen en el mes en curso y permite buscar a alguien por nombre o por gusto. El programa corre en terminal con Python 3 y guarda todo en un archivo de texto para que la información siga ahí la próxima vez que se abra.

## ¿Para qué sirve?

* **Gestión de la información personal:** Centraliza cumpleaños, gustos, alergias/restricciones y registros de regalos pasados de tu grupo de amigos.
* **Seguimiento proactivo de interacciones:** Alerta de forma automática cuando han transcurrido más de 15 días sin hablar con alguien y sugiere temas de conversación dinámicos basados en sus metas o gustos.
* **Planificación de fechas importantes:** Genera un calendario visual del mes en curso indicando los cumpleaños próximos y los días restantes para cada uno.
* **Búsqueda y sugerencias:** Permite buscar contactos por nombre o preferencias para sugerir regalos descartando los que ya fueron entregados.

## Diseño del Sistema y Pseudocódigo

### Estado Inicial (Estructura de Datos)
1. `nombres`: Lista de textos con los nombres de tus amigos.
2. `días`: Lista de números con el día del cumpleaños.
3. `meses`: Lista de números con el mes del cumpleaños.
4. `gustos`: Lista de textos con cosas que le agradan.
5. `regalos`: Lista de textos con los regalos que ya les he entregado en el pasado.
6. `metas_momentos`: Lista de textos para recordar sus proyectos o metas personales.
7. `ultimas_interacciones`: Lista de fechas que guarda el último día que mostraste interés o editaste su información.
## Especificación Lógica y Pseudocódigo

### Estructura de Datos (Estado Inicial)
Se representa cada contacto con los siguientes atributos: `nombre`, `dia_cumple`, `mes_cumple`, `gustos`, `regalos_pasados`, `metas_proyectos` y `ultima_interaccion`.

### Flujo de Ejecución

1. **Inicio de Sesión e Inicialización**:
   * Solicita contraseña de acceso.
   * Busca el archivo `amigos.txt`. Si existe, desencripta y carga la información; si no existe, inicializa la base de datos vacía.
   * Muestra resumen inicial de cumpleaños del mes y alertas de inactividad.

2. **Menú Principal de Operaciones**:
   * `1. Resumen de conexiones`: Evalúa días transcurridos desde `ultima_interaccion`. Si superan el límite (15 días), genera recomendaciones dinámicas de contacto.
   * `2. Calendario de cumpleaños`: Renderiza el mes actual y lista los cumpleaños próximos.
   * `3. Agregar nuevo amigo`: Captura datos iniciales y registra la fecha actual como primera interacción.
   * `4. Actualizar información`: Permite editar gustos, regalos o metas, actualizando automáticamente la fecha de contacto.
   * `5. Registrar conversación`: Reinicia el contador de días sin contacto a cero.
   * `6. Buscar amigo`: Muestra el expediente completo de un contacto.
   * `7. Guardar y Salir`: Persiste los cambios en el archivo local y cierra el programa.

## ¿Cómo se usa?
1. Clonar el repositorio.
2. Ejecutar desde terminal: `python main.py`
3. Introducir contraseña de acceso cuando se solicite.

## Referencias y Fuentes Consultadas
* pendiente
