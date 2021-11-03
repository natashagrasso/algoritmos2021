""" contar la cantidad de ocurrencias de un determinado elemento en una cola,
sin utilizar ninguna estructura auxiliar. """

from cola import Cola
from random import randint

cola_datos = Cola()

for i in range(0,10):
    num = randint(1,40)
    print(num) #hago un print para contar alguna ocurrencia
    cola_datos.arribo(num)

cantidad = 0 
contar  = int(input('ingrese el numero que desea contar: '))

while(not cola_datos.cola_vacia()):
    dato = cola_datos.atencion()
    if (dato == contar ):  
        cantidad += 1    

print('cantidad de ocurrencias', cantidad)  #la cantidad de veces  que esta repetido un valor    

