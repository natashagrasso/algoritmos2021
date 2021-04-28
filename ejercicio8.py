#desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario

def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num//2) + str(num % 2)  
        print('el numero binario es')
print(decimal_a_binario(234))