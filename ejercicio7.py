#Eliminar el i-ésimo elemento después del frente de la cola.

from cola import Cola 
from random import randint

cola_datos = Cola()
cola_aux = Cola()

buscado = int(input ('ingrese el elemento que quiere eliminar '))

for i in range(0,10):
    num = randint(1,10) 
    cola_datos.arribo(num)


print('cola de elementos ')
cantidad_elementos = 0 
while(cantidad_elementos < cola_datos.tamanio()):
    datos = cola_datos.mover_al_final()  
    print(datos) 
    cantidad_elementos += 1 

cont = 0
while (not cola_datos.cola_vacia()):
    if (cont != buscado):
        dato = cola_datos.atencion()
        cola_aux.arribo(dato) 
    else:
        cola_datos.atencion()

    cont += 1    
 
print('cola sin el i-esimo elemento')
cantidad_elementos = 0 
while(cantidad_elementos < cola_aux.tamanio()):
    datos = cola_aux.mover_al_final()  
    print(datos) 
    cantidad_elementos += 1 



