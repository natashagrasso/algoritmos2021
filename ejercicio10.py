""" Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, 
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, 
resolver las siguiente.s actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya 
la palabra ‘Python’, si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 
11:43 y las 15:57, y determinar cuántas son. """

from cola import Cola
from pila import Pila

class Notificaciones (object):
    def __init__ (self,app_que_emitio,mensaje, hora): 
        self.app_que_emitio = app_que_emitio
        self.mensaje = mensaje 
        self.hora = hora

cola_notificaciones = Cola()
cola_aux = Cola()
pila_notificaciones = Pila()

notificaciones = Notificaciones('twitter','python', '12:05' )
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('instagram','kjkjk', '7:30 PM')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('facebook','hoy es el cumpleaños de un amigo', '15:57')
cola_notificaciones.arribo(notificaciones)
notificaciones = Notificaciones('twitter','a un amigo le ha gustado comentario', '11:40 AM')
cola_notificaciones.arribo(notificaciones)

while(not cola_notificaciones.cola_vacia()):#puntoA
    x = cola_notificaciones.atencion() 
    if (x.app_que_emitio != 'facebook'): #lo elimina
        cola_aux.arribo(x)
 
while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion()) 
 
print('la cola sin los elementos de facebook es ')
cantidad_elementos = 0 
while(cantidad_elementos < cola_notificaciones.tamanio()):
    datos = cola_notificaciones.mover_al_final()
    print(datos.app_que_emitio)    
    cantidad_elementos += 1      


while(not cola_notificaciones.cola_vacia()):#puntoB
    x = cola_notificaciones.atencion()  #para no vaciar la cola
    if (x.app_que_emitio =='twitter'):
        mensaje = str(x.mensaje)
        buscado = 'python'
        if (mensaje.find(buscado) == 0):
            print(x.app_que_emitio, mensaje)
    cola_aux.arribo(x)        

    if (x.hora >= '11:43'and x.hora <= '15:57'):
        pila_notificaciones.apilar(x) 

while (not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion())

print('las notificaciones en ese rango de horario son ')
print(pila_notificaciones.tamanio())    
        


        

