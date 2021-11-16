""" Dada una cola de valores enteros calcular su rango y contar 
cuántos elementos negativos hay. """

from cola import Cola
from random import randint

cola_numeros = Cola()
cola_aux = Cola()

for i in range(0,5):
    num = randint(-5,5) 
    cola_numeros.arribo(num)

cantidad_elementos = 0 
while(cantidad_elementos < cola_numeros.tamanio()):
    datos = cola_numeros.mover_al_final()
    print(datos)    
    cantidad_elementos += 1 

max = cola_numeros.en_frente()
min = cola_numeros.en_frente()
cont = 0

while (not cola_numeros.cola_vacia()):
    x = (cola_numeros.atencion())    
    if (x < min):
        min = x
    if (x > max): 
        max = x 
    if (x < 0):
        cont += 1

rango = max - min
print('el rango es ', rango)

print('el maximo es ', max) 
print('el minimo es ', min) 
print ('los numeros negativos son ', cont)
         
         


 


