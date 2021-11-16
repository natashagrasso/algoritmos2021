#Determinar si una cadena de caracteres es un palíndromo.

from pila import Pila 

pila_letras = Pila()
pila_aux = Pila ()
pila_inversa = Pila ()

palabra = input('ingrese una palabra: ')

for letra in palabra: #para cada letra que esta en la palabra la voy apilando
    pila_letras.apilar(letra) 

while(not pila_letras.pila_vacia()):  
  x = pila_letras.desapilar()
  pila_aux.apilar(x)
  pila_inversa.apilar(x) 

while(not pila_aux.pila_vacia()):  
    x = pila_aux.desapilar()
    pila_letras.apilar(x)  

while(not pila_letras.pila_vacia() and pila_letras.elemento_cima() == pila_inversa.elemento_cima()):
    pila_letras.desapilar()
    pila_inversa.desapilar()

if (pila_letras.pila_vacia()):
    print('la palabra es palindromono') 
else: 
    print('la palabra no es palindromono')


