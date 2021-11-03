""" Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno, la cima de la pila
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con c, d y g. """

from pila import Pila

class personajes (object):
    nombre_personaje, cantidad_peliculas = '',0,

personajes1 = personajes()
personajes1.nombre_personaje = 'rocket Raccoon'
personajes1.cantidad_peliculas = 8

personajes2 = personajes()
personajes2.nombre_personaje = 'daredevil'
personajes2.cantidad_peliculas = 4

personajes3 = personajes()
personajes3.nombre_personaje = 'capitan america'
personajes3.cantidad_peliculas = 6

personajes4 = personajes()
personajes4.nombre_personaje = 'groot'
personajes4.cantidad_peliculas = 7

personajes5 = personajes()
personajes5.nombre_personaje = 'la viuda negra'
personajes5.cantidad_peliculas = 9

personajes6 = personajes()
personajes6.nombre_personaje = 'carol danvers'
personajes6.cantidad_peliculas = 2


pila_marvel = Pila()
pila_marvel.apilar(personajes1)
pila_marvel.apilar(personajes2)
pila_marvel.apilar(personajes3)
pila_marvel.apilar(personajes4)
pila_marvel.apilar(personajes5)
pila_marvel.apilar(personajes6)

pila_aux  = Pila()

pos = 1
pos_rocket = 0
pos_groot = 0
cont = 0

while(not pila_marvel.pila_vacia()):
    x = pila_marvel.desapilar() 
    pila_aux.apilar(x)
    if (x.nombre_personaje == 'rocket Raccoon'):
        pos_rocket = pos
    if (x.nombre_personaje =='groot'):
        pos_groot = pos 
    pos += 1    

while(not pila_aux.pila_vacia()): #volvemos a cargar la pila de marvel 
    x = pila_aux.desapilar() 
    pila_marvel.apilar(x)
print('Rocket Raccoon se encuentran en la posicion ',pos_rocket)    
print('Groot se encuentran en la posicion ',pos_groot) 


while(not pila_marvel.pila_vacia()):  #puntoB
    x = pila_marvel.desapilar() 
    pila_aux.apilar(x)
    if (x.cantidad_peliculas > 5):
        print('El personaje ',x.nombre_personaje, 'participo en mas de 5 peliculas')
        print('Y la cantidad de pelis en las que aparecen son: ', x.cantidad_peliculas)  
    
while(not pila_aux.pila_vacia()): #volvemos a cargar la pila de marvel 
    x = pila_aux.desapilar() 
    pila_marvel.apilar(x)    


while(not pila_marvel.pila_vacia()):  
    x = pila_marvel.desapilar()
    if (x.nombre_personaje == 'la viuda negra'):  
        print('las películas en las que participo la Viuda Negra son ', x.cantidad_peliculas)     
    pila_aux.apilar(x)

while(not pila_aux.pila_vacia()): #volvemos a cargar la pila de marvel 
    x = pila_aux.desapilar() 
    pila_marvel.apilar(x)    
  
 
while(not pila_marvel.pila_vacia()):  #puntoD
    x = pila_marvel.desapilar() 
    pila_aux.apilar(x)

    if (x.nombre_personaje[0] == 'c'):
        print('personajes que comienzan con c',x.nombre_personaje)

    if (x.nombre_personaje[0] == 'd'):
        print('personajes que comienzan con d',x.nombre_personaje)  

    if (x.nombre_personaje[0] == 'g'):
        print('personajes que comienzan con g',x.nombre_personaje) 

while(not pila_aux.pila_vacia()): 
    x = pila_aux.desapilar() 
    pila_marvel.apilar(x) 


