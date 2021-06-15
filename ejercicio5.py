#desarrollar una función que permita convertir un número romano en un número decimal    #ejercicio5
def de_romanos_aentero(nromano, entero):
    romanos = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000 }

    if  (len(nromano) <=0):
        return entero 
    elif  romanos[nromano [0]] > romanos  [nromano [-1]]:
            entero += romanos [nromano[0]] - romanos [nromano [-1]]
    else:
        entero += romanos [nromano[0]]
    return de_romanos_aentero (nromano[:0], entero)  

entero = 0 
print (de_romanos_aentero('XL', entero))    




""" #desarrollar un algoritmo que permita calcular la siguiente serie:      #ejercicio7
# h(n)= 1+ 1/2 + 1/3 + ... 1/n

def sumatoria (numero):
    if (numero == 0):
        return numero
    else: 
        return 1/numero + sumatoria (numero-1)     
print (sumatoria(3))    """     



