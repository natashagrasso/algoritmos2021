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
            
cantidad_elementos = 0 
""" while(cantidad_elementos < cola_numeros1.tamanio()):
    datos = cola_numeros1.mover_al_final()
    print(datos)    
    cantidad_elementos += 1  

print() 

cantidad_elementos = 0 
while(cantidad_elementos < cola_numeros2.tamanio()):
    datos = cola_numeros2.mover_al_final()
    print(datos)    
    cantidad_elementos += 1 
 """


""" pos = 0 """

while(not cola_numeros1.cola_vacia()):
    x = cola_numeros1.atencion() 
    """ cola_combinada.arribo(x)  """

    cantidad_elementos2 = 0

    while(cantidad_elementos2  < cola_numeros2.tamanio()):
        if x < cola_numeros2.en_frente():
            cola_numeros2.arribo(x)
        else: 
            cola_numeros2.mover_al_final()
            cola_numeros2.arribo(x)  
        cantidad_elementos += 1       
            #y = cola_numeros2.atencion()  
        """ cola_combinada.arribo(y) """ 
"""         for i in range(0,5):
            if (x > y):
                cola_combinada.arribo(x) 
                print('llega',x)
                cola_combinada.mover_al_final()            
        else:
                cola_combinada.arribo(y)
                print('este tmb',y)
                cola_combinada.en_frente() """
                         
print()
cantidad_elementos = 0 
while(cantidad_elementos < cola_numeros2.tamanio()):
    datos = cola_numeros2.mover_al_final()
    print(datos)    
    cantidad_elementos += 1           
