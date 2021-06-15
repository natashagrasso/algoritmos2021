# implementar una función para calcular la potencia dado dos números enteros,
#  el primero representa la base y segundo el exponente.

def potencia (n1,n2):
    if (n2 == 0):
        return 1
    else:
        return n1*potencia(n1, n2-1)   

numero1=2
numero2=4

print(numero1, 'elevado a', numero2, 'es', potencia(numero1, numero2))         