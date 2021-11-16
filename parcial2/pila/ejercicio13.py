""" Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU)
 de los cuales se conoce el nombre del modelo, nombre de la película en la que se 
usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver 
las siguientes actividades:
a) determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, 
además mostrar el nombre de dichas películas;
b) mostrar los modelos que quedaron dañados, sin perder información de la pila.[84]
c) eliminar los modelos de los trajes destruidos mostrando su nombre;
d) un modelo de traje puede usarse en más de una película y en una película se pueden usar 
más de un modelo de traje, estos deben cargarse por separado;
e) agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos 
repetidos en una misma película;
f) mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y 
“Capitan America: Civil War”. """

from pila import Pila

class Traje (object):
    modelo, pelicula, estado_traje = '','','',

pila_trajes = Pila()
pila_aux  = Pila()
pila_spiderman = Pila() ## guarda los trajes de la pelicula Spiderman
pila_capitan = Pila() ## guarda los trajes de la pelicula Capitan America

##Creamos los trajes
#traje1 = Traje("Mark III", "Capitan America: Civil War", "Dañado")
traje1 = Traje()
traje1.modelo = "Mark III"
traje1.pelicula = "Capitan America: Civil War"
traje1.estado_traje = "Dañado"

#traje2 = Traje('Mark XLIV', 'Iron Man I', 'Destruido')
traje2 = Traje()
traje2.modelo = "Mark XLIV"
traje2.pelicula = "Iron Man I"
traje2.estado_traje = "Destruido"

#traje3 = Traje('Mark XX', 'Spider-Man: Homecoming', 'Impecable')
traje3 = Traje()
traje3.modelo = "Mark XX"
traje3.pelicula = "Spider-Man: Homecoming"
traje3.estado_traje = "Impecable"

#traje4 = Traje('Mark XVX', 'Spider-Man: Homecoming', 'Dañado')  
traje4 = Traje()
traje4.modelo = "Mark XVX"
traje4.pelicula = "Spider-Man: Homecoming"
traje4.estado_traje = "Dañado"


## Apilamos los modelos de los trajes
pila_trajes.apilar(traje1)
pila_trajes.apilar(traje2)
pila_trajes.apilar(traje3)
pila_trajes.apilar(traje4)

control_traje = True

pelicula = input("Ingrese la pelicula en la que se uso el traje Mark LXXXV: ")
## Buscamos si está el traje Mark XLIV
while (not pila_trajes.pila_vacia()):
    x = pila_trajes.desapilar()
    if (x.modelo == 'Mark XLIV'): #puntoA 
        print('el modelo Mark XLIV fue utilizado en ', x.pelicula)

    if (x.estado_traje == 'Dañado'): #puntoB
        print ('el modelo ', x.modelo, 'resulto dañado')

    #puntoc
    ## Lo elimina no apilandolo, de forma se pierde
    if (x.estado_traje == 'Destruido'):
        print('el modelo ', x.modelo , 'resulto destruido')
    else:
        pila_aux.apilar(x)  

    ##e) agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden
    #  cargar modelos repetidos en una misma película;
    ##Busca si el traje Mark LXXXV esta en la pelicula ingresada
    if (x.modelo == 'Mark LXXXV' and x.pelicula == pelicula):
        control_traje = False
        
    #Guarda los trajes de la pelicula Spiderman
    if (x.pelicula == "Spider-Man: Homecoming"):
        pila_spiderman.apilar(x.modelo)

    #Guarda los trajes de la pelicula Cap America
    if (x.pelicula == "Capitan America: Civil War"):
        pila_capitan.apilar(x.modelo)

print("La pila sin los trajes destruidos es: ")
while(not pila_aux.pila_vacia()):  
    x = pila_aux.desapilar()
    print(x.modelo)  


if (control_traje == False):
    print("El traje ya fue cargado en esa pelicula") 
else:
    traje5 = Traje()
    traje5.modelo = "Mark LXXXV"
    traje5.pelicula = pelicula
    traje5.estado_traje = "Impecable"
    pila_trajes.apilar(traje5)
    print("Modelo Mark LXXXV agregado con éxito")
      

print("Los trajes de la pelicula Spider-Man: Homecoming son: ")
while(not pila_spiderman.pila_vacia()):  
    x = pila_spiderman.desapilar()
    print(x)  

print("Los trajes de la pelicula Capitan America: ")
while(not pila_capitan.pila_vacia()):  
    x = pila_capitan.desapilar()
    print(x)