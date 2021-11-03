#Implementar una función para calcular el producto de dos números enteros dados.

def producto (n1,n2):
    if (n2 == 0):
        return 0
    else:
        return n1 + producto(n1, n2-1)   

numero1=2
numero2=3

print('el producto es: ', producto(numero1, numero2))     