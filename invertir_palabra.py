def invertir (palabra, pos):
    if (pos == 0):
        return palabra[pos]
    else:
        return palabra[pos]+invertir(palabra,pos-1)

palabra = 'hola'
posicion = (len(palabra)-1)   

print(invertir(palabra,posicion))