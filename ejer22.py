
mochila_jedi = ['lapicera' , 'manzana', 'espada', 'sable de luz' , 'capa']

def  usarlafuerza (mochila_jedi, pos):
    if(pos < len(mochila_jedi) -1):
        if (mochila_jedi [pos] == 'sable de luz'):   #condicion de fin
            print ('el sable de luz se encuentra en la posicion ', pos)
            return pos
        else:
            return usarlafuerza (mochila_jedi, pos+1)
    else:
        return -1
    print ('el sable de luz no se encuentra en la mochila')  

print(usarlafuerza(mochila_jedi, 0 ))