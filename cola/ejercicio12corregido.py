""" Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
ni métodos de ordenamiento. """

from cola import Cola

cola_numeros1 = Cola()
cola_numeros2 = Cola()

numeros1 = [1,3,5,7,9]
numeros2 = [2,4,6,8,10]

for i in numeros1:
    cola_numeros1.arribo(i)

for i in numeros2:
    cola_numeros2.arribo(i)
                     

tamanio_cola2 = cola_numeros2.tamanio()

cont = 0

while(not cola_numeros1.cola_vacia()):
    x = cola_numeros1.atencion() 
    while (x > cola_numeros2.en_frente() and (cont < tamanio_cola2)):
        cola_numeros2.mover_al_final()
        cont+=1
    cola_numeros2.arribo(x)

while(cont < tamanio_cola2):
    cola_numeros2.mover_al_final()
    cont += 1 


print("La cola ordenada es")
cantidad_elementos = 0 
while(cantidad_elementos < cola_numeros2.tamanio()):
    datos = cola_numeros2.mover_al_final()
    print(datos)    
    cantidad_elementos += 1 