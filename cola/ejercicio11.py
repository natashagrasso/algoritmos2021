""" Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta 
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
b. indicar el plantea natal de Luke Skywalker y Han Solo
c. insertar un nuevo personaje antes del maestro Yoda
d. eliminar el personaje ubicado después de Jar Jar Binks """

from cola import Cola

class Personajes (object):
    def __init__ (self, personaje, planeta): 
        self.personaje = personaje
        self.planeta = planeta
        

cola_personajesSW = Cola()
cola_aux1 = Cola()

personajes = Personajes('Jar Jar Binks','Tatooine')
cola_personajesSW.arribo(personajes)
personajes = Personajes('Han Solo','Endor')
cola_personajesSW.arribo(personajes)
personajes = Personajes('Yoda','Jupiter')
cola_personajesSW.arribo(personajes)
personajes = Personajes('Luke Skywalker','Alderaan')
cola_personajesSW.arribo(personajes)

posicion_a_insertar = 3


""" while (not cola_personajesSW.cola_vacia()):

    cola_aux1.arribo(cola_personajesSW.atencion()) 
 """
cantidad_elementos = 0

while(cantidad_elementos < cola_personajesSW.tamanio()):
    dato = cola_personajesSW.mover_al_final() 

    if (dato.planeta == 'Alderaan'): #puntoA
        print ('El personaje del planeta Alderaan es ',dato.personaje)
    elif (dato.planeta == 'Endor'):
        print('El personaje del planeta Endor es ', dato.personaje)
    elif (dato.planeta == 'Tatooine'):
        print('El personaje del planeta Tatooine es ',dato.personaje)

    cantidad_elementos += 1 
    
print()

cantidad_elementos = 0 
while(cantidad_elementos < cola_personajesSW.tamanio()):

    dato = cola_personajesSW.mover_al_final() 

    if (dato.personaje == 'Luke Skywalker'): #puntoB
        print('El planeta natal de Luke Skywalker es ', dato.planeta)
    elif (dato.personaje == 'Han Solo') :
        print('El planeta natal de Han solo es ',dato.planeta)  

    cantidad_elementos += 1

while (not cola_personajesSW.cola_vacia()):
    dato = cola_personajesSW.atencion()

    if (dato.personaje == 'Yoda'):
        nuevo_nombre_personaje = input('ingrese el nombre del nuevo personaje') 
        nuevo_planeta_personaje = input('ingrese el planeta del nuevo personaje')
        personajes = Personajes(nuevo_nombre_personaje,nuevo_planeta_personaje)
        cola_aux1.arribo(personajes)
        cola_aux1.arribo(dato)
    else:
        cola_aux1.arribo(dato)    

while (not cola_aux1.cola_vacia()):
    cola_personajesSW.arribo(cola_aux1.atencion())   

cantidad_elementos = 0 
while(cantidad_elementos < cola_personajesSW.tamanio()):
    datos = cola_personajesSW.mover_al_final()
    print(datos.personaje)    
    cantidad_elementos += 1 


cont = 0

while (cont < cola_personajesSW.tamanio()):
    dato = cola_personajesSW.atencion()

    if (dato.personaje == 'Jar Jar Binks'):
        cola_aux1.arribo(dato) #lo guarda
        cont += 1
        dato2 = cola_personajesSW.atencion() #lo saca y no lo guarda
    else:
        cola_aux1.arribo(dato) 
        cont += 1 


while (not cola_aux1.cola_vacia()):
    cola_personajesSW.arribo(cola_aux1.atencion())   

cantidad_elementos = 0 
while(cantidad_elementos < cola_personajesSW.tamanio()):
    datos = cola_personajesSW.mover_al_final()
    print(datos.personaje)    
    cantidad_elementos += 1  


    

""" if (cola_personajesSW.tamanio() >= posicion_a_insertar):
    pos = 0 

    while (not cola_personajesSW.cola_vacia()and pos < posicion_a_insertar):#controla la cantidad de elementos que tengo que desplazar
        pos +=1
        cola_aux1.arribo(cola_personajesSW.atencion()) #los paso de una pila a la otra

    personajes = Personajes('Capitan America', 'Marte')
    cola_personajesSW.arribo(personajes)

    while (not cola_aux1.cola_vacia()):
        cola_personajesSW.arribo(cola_aux1.atencion())

while (not cola_personajesSW.cola_vacia()):
    print (cola_personajesSW.atencion())   """

""" pos = 0

while (not cola_personajesSW.cola_vacia()):
    dato = cola_personajesSW.atencion()
    if (dato.personaje == 'Jar Jar Binks'):
        print('oo')
        pos += 1               

    break 

print(pos)   """ 

""" while (not cola_personajesSW.cola_vacia()):
    dato = cola_personajesSW.atencion()   
    pos = 0

    if (dato.personaje == 'Jar Jar Binks'):
        print('el personaje ubicado desp de JAR Jar binks es ', dato.personaje)
        pos += 1
    else:       
        cola_aux1.arribo(dato) 

print("cola con el personaje eliminado")
while(not cola_aux1.cola_vacia()):  
    dato = cola_aux1.atencion()
    print(dato.personaje)   """        






     