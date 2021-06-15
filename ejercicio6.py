#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_cadena(cadena):
    if (len(cadena)==0):
        return ''
    else:
        return cadena[-1]+invertir_cadena(cadena [0:-1])    

print(invertir_cadena('hola mundo'))        
