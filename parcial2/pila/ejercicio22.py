"""  Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The 
Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada 
misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, 
costo de la recompensa. Resolver las siguientes actividades:
a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
de los cazzarrecompensas;
b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos 
quien obtuvo mayor fortuna;
c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la 
que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
d. indicar la cantidad de capturas realizadas por cada cazarrecompensas. """

from pila import Pila


class Mision (object):
    planeta_visitado, capturado, recompensa = '','',0,

mision1 = Mision()
mision1.planeta_visitado = 'Ahch-To'
mision1.capturado = 'luke'
mision1.recompensa = 1000

mision2 = Mision()
mision2.planeta_visitado = 'Anoat'
mision2.capturado = 'han solo'
mision2.recompensa = 3000

mision3 = Mision()
mision3.planeta_visitado = 'Atollon'
mision3.capturado = 'leia'
mision3.recompensa = 200

mision4 = Mision()
mision4.planeta_visitado = 'Bespin'
mision4.capturado = ' Bail Organa'
mision4.recompensa = 4000

mision5 = Mision()
mision5.planeta_visitado = 'Corellia'
mision5.capturado = 'Ahsoka Tano'
mision5.recompensa = 47000

mision6 = Mision()
mision6.planeta_visitado = 'Christophsis'
mision6.capturado = 'yoda'
mision6.recompensa = 17000


pila_boba = Pila() #boba fett
pila_boba.apilar(mision1)
pila_boba.apilar(mision2)
pila_boba.apilar(mision3)
pila_boba.apilar(mision6)


pila_din = Pila() #din djarin
pila_din.apilar(mision4)
pila_din.apilar(mision5)

pila_aux1 = Pila()

total_boba = 0
total_din = 0   

print('planetas visitados por boba')
while(not pila_boba.pila_vacia()):
    x = pila_boba.desapilar()  
    total_boba += x.recompensa 
    pila_aux1.apilar(x)


while(not pila_aux1.pila_vacia()): #puntoA
    x = pila_aux1.desapilar() 
    pila_boba.apilar(x) 
    print(x.planeta_visitado)
       


print('planetas visitados por din')
while(not pila_din.pila_vacia()):
    x = pila_din.desapilar() 
    total_din += x.recompensa  
    pila_aux1.apilar(x)

while(not pila_aux1.pila_vacia()): #puntoA
    x = pila_aux1.desapilar()  
    pila_din.apilar(x)
    print(x.planeta_visitado)         


print('total recaudado por boba ', total_boba) #puntoB
print('total recaudado por din ', total_din)

if (total_boba > total_din):
    print(' quien gano mas fue boba fett' )
else:
    print(' quien gano mas fue din ' )

cont = 0
misiones_boba = pila_boba.tamanio()


while(not pila_boba.pila_vacia()):
    x = pila_boba.desapilar() 
    pila_aux1.apilar(x)
    if (x.capturado == 'han solo'):#puntoC
        nro_mision = cont
    cont += 1 

while(not pila_aux1.pila_vacia()): 
    x = pila_aux1.desapilar() 
    pila_boba.apilar(x)


ubicacion_mision = misiones_boba - nro_mision

print('han solo fue capturado en la mision nro ', ubicacion_mision)

print('la cantidad de capturas de boba son ', pila_boba.tamanio()) #puntoD
print('la cantidad de capturas de din son ', pila_din.tamanio())







    



  


   







