#Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from pila import Pila
from random import randint

pila_numeros = Pila()
pila_aux = Pila()

ocurrencias = 5
reemplazo = 10

print('pila original')

for i in range(0,10):
    num = randint(1,5)
    print(num) 
    pila_numeros.apilar (num)

while(not pila_numeros.pila_vacia()):
    x = pila_numeros.desapilar()
    if  (x == ocurrencias):
         pila_aux.apilar(reemplazo)
    else:
        pila_aux.apilar(x)

print('pila con reemplazo ')

while(not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print(x)#guardo lo que desapile       


    