
#Implementar una función para calcular el logaritmo entero de número n en una base b.

def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)

print(logaritmo(6, 2))