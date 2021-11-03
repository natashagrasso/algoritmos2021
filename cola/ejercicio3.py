#Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
#si es un palíndromo.

from pila import Pila
from cola import Cola
from random import randint

cola_datos = Cola()
pila_datos = Pila()

palindromo = False

palabra = input('ingrese una palabra: ')
print(palabra)

for letra in palabra:
    cola_datos.arribo(letra.lower())


cantidad_elementos = 0 
while(cantidad_elementos < cola_datos.tamanio()):
    """ pila_datos.apilar(cola_datos.mover_al_final()) """  #saco uno, lo paso al otro, cuando esta vacio lo vuelvo a hacer a la inversa 
    x = cola_datos.mover_al_final()
    pila_datos.apilar(x)
    cantidad_elementos += 1

while (not pila_datos.pila_vacia()):
    dato_pila = pila_datos.desapilar()
    dato_cola= cola_datos.atencion()  

    if (dato_pila == dato_cola):
        palindromo = True
    else:
        palindromo = False 

if (palindromo == True):
    print('la palabra es palindromo ')
else: 
    print(' la palabra no es palindromo ')    
 