from cola import Cola 
from random import randint

cola_datos = Cola()
#cola_aux = Cola()

for i in range (0,10):
    num = randint(0,100) 
    cola_datos.arribo(num)
    print(num)

print() 

cantidad_elementos = 0 #con esto se obtiene el mismo resultado que usando una cola auxiliar

while(cantidad_elementos < cola_datos.tamanio()): 
    dato = (cola_datos.mover_al_final()) # esta funcion toma el elemento, lo mueve al final y lo devuelve 
    print (dato) 
    cantidad_elementos += 1 


""" while(not cola_datos.cola_vacia()): 
    dato = (cola_datos.atencion())
    cola_aux.arribo(dato) """

""" while(not cola_aux.cola_vacia()): 
    dato = (cola_aux.atencion())    #de esta manera, con la cola auxiliar nos vamos a perder los elementos
    cola_datos.arribo(dato) """


print('tamanio: ', cola_datos.tamanio()) #como realizamos todas las atenciones la cola queda vacia

#si queremos hacer un barrido y concervar esos valores, hacemos una cola auxiliar 

#otra manera es, omitir usar la cola auxiliar 

