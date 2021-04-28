#desarrollar una función que permita convertir un número romano en un número decimal    #ejercicio5
def de_romanos_aentero(nromano):
    romanos = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000 }
    entero = 0 

    if  (len(nromano) >=0):
        return 0 
    elif  romanos[nromano [0]] > romanos [nromano [-1]]:
            entero += romanos [nromano[0]] - romanos [nromano [-1]]
    else:
        entero += romanos [nromano[0]]
    return de_romanos_aentero (nromano[:0])  

print (de_romanos_aentero('v'))    


""" #dada una secuencia de caracteres, obtener dicha secuencia invertida. #ejercicio6
def invertir_cadena (cadena):
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:-1])
print(invertir_cadena("natasha"))   

 """

""" #desarrollar un algoritmo que permita calcular la siguiente serie:      #ejercicio7
# h(n)= 1+ 1/2 + 1/3 + ... 1/n

def sumatoria (numero):
    if (numero == 0):
        return numero
    else: 
        return 1/numero + sumatoria (numero-1)     
print (sumatoria(3))    """     


""" 
#implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:  # ejercicio9
def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)

print(logaritmo(6, 2)) """
