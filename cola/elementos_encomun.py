from cola import Cola 
from random import randint

cola_uno = Cola()
cola_dos = Cola()
cola_aux = Cola()

for i in range(0,20):
    cola_uno.arribo(randint(2,100))
    cola_dos.arribo(randint(2,100))


cantidad_repetidos = 0

while (not cola_uno.cola_vacia()): #tomo un elemento de la primera cola y lo comparo con todos los elementos de la 2da cola
    numero1 = cola_uno.atencion()
    while(not cola_dos.cola_vacia()):
        numero2 = cola_dos.atencion()
        if (numero1 == numero2):
            cantidad_repetidos += 1
        cola_aux.arribo(numero2)             #apilo ese elemento en la cola auxiliar

    while(not cola_aux.cola_vacia()):
        cola_dos.arribo(cola_aux.atencion())

print('la cantidad de repetidos son ',cantidad_repetidos)







