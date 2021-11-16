#Determinar el número de ocurrencias de un determinado elemento en una pila.

from pila import Pila 
from random import randint

pila_datos = Pila()

for i in range(0,10):
    num = randint(1,40)
    print(num) #hago un print para contar alguna ocurrencia
    pila_datos.apilar (num)

cantidad = 0 
contar  = int(input('ingrese el numero que desea contar: '))

while(not pila_datos.pila_vacia()):
    x = pila_datos.desapilar()
    if (x == contar ):  
        cantidad += 1    

print('cantidad de ocurrencias', cantidad)  #la cantidad de veces  que esta repetido un valor