#Utilizando operaciones de cola y pila, invertir el contenido de una cola.
from pila import Pila
from cola import Cola
from random import randint

cola_datos = Cola()
pila_datos = Pila()

for i in range(0,10):  
    numeros = randint (0,20)   
    cola_datos.arribo(numeros) #cargamos los elemenos 

print('cola original')  

while (not cola_datos.cola_vacia()): #vaciamos la cola y lo pasamos a la pila  y por definicion de la estructura van a quedar alreves
    x = cola_datos.atencion()
    print(x)
    pila_datos.apilar(x) #saco uno, lo paso al otro, cuando esta vacio lo vuelvo a hacer a la inversa 
 
while (not pila_datos.pila_vacia()):
    x = pila_datos.desapilar()
    cola_datos.arribo(x)  


print('cola invertida')
cantidad_elementos = 0 #mostramos la pila dada vuelta
while(cantidad_elementos < cola_datos.tamanio()):      
    x = cola_datos.mover_al_final()
    print(x)    
    cantidad_elementos += 1





# datos = Cola()
# datos_aux = Pila()

# for i in range(1,10):
#     numero = randint (0,20)
#     datos.arribo(numero) #cargamos los elemenos 
#     print (numero)

# print()

# while (not datos.cola_vacia()): #vaciamos la cola y lo pasamos a la pila  y por definicion de la estructura van a quedar alreves
#     datos_aux.apilar(datos.atencion()) #saco uno, lo paso al otro, cuando esta vacio lo vuelvo a hacer a la inversa 
 
# while (not datos_aux.pila_vacia()):
#     datos.arribo(datos_aux.desapilar())  

# cantidad_elementos = 0 
# while(cantidad_elementos < datos.tamanio()):
#     datos = datos.mover_al_final()
#     print(datos)    
#     cantidad_elementos += 1    
  