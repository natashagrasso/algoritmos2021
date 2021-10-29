 #Eliminar de una cola de caracteres todas las vocales que aparecen

from cola import Cola

cola_vocal = Cola()

palabra = input('ingrese una palabra ')

for letra in palabra:
    cola_vocal.arribo(letra.lower())

vocales = ['a', 'e', 'i', 'o', 'u']
i, cantidad_letras = 0, cola_vocal.tamanio() #la i va a ser la que me va a contar la cantidad de elementos 

while (i < cantidad_letras):
    dato = cola_vocal.atencion()    
    if (not dato in vocales): #not in: si dato no esta en..
        cola_vocal.arribo(dato)
    i += 1 
cantidad_letras = 0     

while (cantidad_letras < cola_vocal.tamanio()):
    dato = cola_vocal.mover_al_final()    
    print(dato)
    cantidad_letras += 1
         

     

