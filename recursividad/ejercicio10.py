# . Desarrollar un algoritmo que cuente la cantidad 
# de dígitos de un número entero.

def sumar_digitos(numero):
    if(numero < 10):
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
 
print(sumar_digitos(1111111111))