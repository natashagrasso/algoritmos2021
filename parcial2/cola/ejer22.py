""" se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino 
F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes. """

from cola import Cola

class PersonajesMCU(object):
    def __init__ (self, nombre_personaje, nombre_superheroe, genero): 
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

cola_personajesMCU = Cola()
cola_aux = Cola()

personajes_MCU = PersonajesMCU('Tony Stark','Scott Lang','M')
cola_personajesMCU.arribo(personajes_MCU)
personajes_MCU = PersonajesMCU('Steve Rogers','Capitán América','M')
cola_personajesMCU.arribo(personajes_MCU)
personajes_MCU = PersonajesMCU('Natasha Romanoff','Black Widow','F')
cola_personajesMCU.arribo(personajes_MCU)
personajes_MCU = PersonajesMCU('Carol Susan','capitana marvel','F')
cola_personajesMCU.arribo(personajes_MCU)

cont_femenino = ''
cont_masculino = ''

cantidad_elementos = 0

while(cantidad_elementos < cola_personajesMCU.tamanio()):
    dato = cola_personajesMCU.mover_al_final() 

    if (dato.nombre_superheroe == 'capitana marvel'): #puntoA
        print('el nombre de la capitana marvel es ', dato.nombre_personaje) 
    
    if (dato.genero == 'F'): #puntoB
        cont_femenino += dato.nombre_personaje

    if (dato.genero == 'M'):
        cont_masculino += dato.nombre_personaje #puntoC
    
    if (dato.nombre_personaje == 'Scott Lang'):
        print('l nombre del superhéroe del personaje', dato.nombre_superheroe) 
    
    if (dato.nombre_personaje[0] == 's'.lower()):
        print('personajes que comienzan con c',dato.nombre_personaje)

    cantidad_elementos += 1 

print(' nombres femeninos: ', cont_femenino) 
print(' nombres masculinos : ', cont_masculino)