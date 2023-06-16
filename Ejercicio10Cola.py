class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

# Creamos la cola con las notificaciones de redes sociales
cola_notificaciones = [
    Notificacion("10:30", "Facebook", "Hola usuario"),
    Notificacion("11:20", "Twitter", "¡Nuevo tweet sobre Python!"),
    Notificacion("11:43", "Instagram", "¡Nueva foto!"),
    Notificacion("12:15", "Facebook", "Tienes un nuevo mensaje"),
    Notificacion("14:30", "Twitter", "¿Alguien conoce Python?"),
    Notificacion("15:10", "Facebook", "Notificación de grupo"),
    Notificacion("15:57", "Twitter", "¡Nuevo seguidor!"),
    Notificacion("16:30", "Instagram", "¡Likes en tu última foto!")
]

# a. Función para eliminar las notificaciones de Facebook de la cola
def eliminar_notificaciones_facebook(cola):
    cola = [notificacion for notificacion in cola if notificacion.aplicacion != "Facebook"]
    return cola

cola_notificaciones = eliminar_notificaciones_facebook(cola_notificaciones)
print("a. Notificaciones después de eliminar las de Facebook:", [notificacion.mensaje for notificacion in cola_notificaciones])

# b. Función para mostrar las notificaciones de Twitter que contienen la palabra 'Python'
def mostrar_notificaciones_twitter_python(cola):
    notificaciones_twitter_python = [notificacion for notificacion in cola if notificacion.aplicacion == "Twitter" and "Python" in notificacion.mensaje]
    return notificaciones_twitter_python

notificaciones_twitter_python = mostrar_notificaciones_twitter_python(cola_notificaciones)
print("b. Notificaciones de Twitter con la palabra 'Python':")
for notificacion in notificaciones_twitter_python:
    print("   - Hora:", notificacion.hora)
    print("     Mensaje:", notificacion.mensaje)

# c. Utilizar una pila para almacenar temporalmente las notificaciones entre las 11:43 y las 15:57
pila_temporal = []
for notificacion in cola_notificaciones:
    if "11:43" <= notificacion.hora <= "15:57":
        pila_temporal.append(notificacion)

print("c. Cantidad de notificaciones almacenadas en la pila temporal:", len(pila_temporal))

