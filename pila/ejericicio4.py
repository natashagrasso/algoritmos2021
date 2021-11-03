#Invertir el contenido de una pila, solo puede utilizar 
# una pila auxiliar como estructura extra

from pila import Pila
from random import randint

pila_numeros = Pila()
pila_aux = Pila()

print('pila original')

for i in range(0,10):
    num = randint(1,5)
    print(num) 
    pila_numeros.apilar (num)

print('pila invertida ')

while(not pila_numeros.pila_vacia()):
    x = pila_numeros.desapilar()
    pila_aux.apilar(x)
    print(x)     

""" print('pila axuliar')

while(not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print(x)#guardo lo que desapile   """   