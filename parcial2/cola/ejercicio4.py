#Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no
# sean primo

from cola import Cola 
from random import randint

def es_primo(numero): #funcion para saber si un numero es primo
    cantidad = 0 
    for i in range(1, numero+1):
        if (numero % i == 0 ):
            cantidad +=1
    return cantidad ==2 

cola_numeros = Cola()

for i in range(1,10):
    cola_numeros.arribo(randint(2,100))

cantidad = cola_numeros.tamanio()
i=0

while ( i < cantidad):
    numero = cola_numeros.atencion()   
    if (es_primo(numero)):
        cola_numeros.arribo(numero)
    else:
        print(numero)  
    i+=1    

print('son primos')

while(not cola_numeros.cola_vacia()):
    print(cola_numeros.atencion())