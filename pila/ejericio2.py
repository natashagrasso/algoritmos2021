#eliminar de una pila todos los elementos impares, 
#es decir que en la misma solo queden números pares.

from pila import Pila 
from random import randint 


pila_numeros = Pila()
pila_aux = Pila()

print('pila original')
for i in range(0,10):   #acciones basicas:, con el for apilamos toda la pila
    num = randint(1,20)
    print(num) 
    pila_numeros.apilar (num)

while(not pila_numeros.pila_vacia()):  #con el while desapilamos esa pila y a medida que desapilamos usamos el x para guardar y hacer lo que el problema pide
    x = pila_numeros.desapilar()
    if  (x % 2 == 0):  #depende el ejercicio varia el if
         pila_aux.apilar(x)

print('pila sin numeros impares')

while(not pila_aux.pila_vacia()):#para acceder a los elementos de la pila auxiliar tenemos que desapilarla y mostrarla 
    x = pila_aux.desapilar()
    print(x)#guardo lo que desapile
    
    


       
