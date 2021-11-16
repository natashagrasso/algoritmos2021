# Desarrollar un algoritmo que invierta un númeroentero sin convertirlo 
# a cadena.

def invertir_numero(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)

print(invertir_numero(791))