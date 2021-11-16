#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire 
#strikes back” y la otra los del episodio VII “The force awakens”. 
# Desarrollar un algoritmo que  permita obtener la intersección de ambas pilas, 
#es decir los personajes que aparecen en ambos episodios.

from pila import Pila

pila_episodioV = Pila()
pila_episodioVII = Pila()
pila_aux= Pila()
pila_aux2 = Pila()


personajes_the_empire = ['han solo', 'yoda', 'luke', 'lando']
personajes_the_force_awakens = ['R2-D2', 'Lobot', 'dengar', 'yoda', 'luke']


for i in personajes_the_empire:
    pila_episodioV.apilar(i)


for i in personajes_the_force_awakens:
    pila_episodioVII.apilar(i)

while(not pila_episodioV.pila_vacia()):
    x = pila_episodioV.desapilar() 

    while(not pila_episodioVII.pila_vacia()):
        y = pila_episodioVII.desapilar() 
        pila_aux2.apilar(y)  
        if (x == y):
            pila_aux.apilar(y)

    while(not pila_aux2.pila_vacia()):
        y = pila_aux2.desapilar()  
        pila_episodioVII.apilar(y)
            

print('los personajes en comun son')

while(not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()  
    print(x)           




    
