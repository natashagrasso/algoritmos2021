def salir_del_laberinto (matriz, F, C, senderos =[]):
    if (F >= 8 and  C <= len(matriz)-1) and (F >= 0 and C <= len(matriz[8])-1):  # condicion de fin 
        if (matriz[F] [C] == 5):
            print ("has logrado salir del laberinto!!")
            print(senderos)
        else: 
            if (matriz[F][C]== 8):
                matriz[F][C] = 1
                senderos.append([F, C])
            print ('se movio hacia la derecha')   
            salir_del_laberinto(matriz, F, C+1,senderos) 
            print ('se movio hacia la izquierda')  
            salir_del_laberinto(matriz, F, C-1, senderos) 
            print ('se movio hacia arriba') 
            salir_del_laberinto(matriz, F-1, C, senderos)  
            print ('se movio hacia abajo')
            salir_del_laberinto(matriz, F+1, C,senderos) 
            senderos.pop ()
            matriz[F][C] = 1

laberinto = [[0, 0, 8, 8, 0, 0],
             [8, 0, 8, 0, 0, 8],
             [0, 0, 8, 8, 8, 8],
             [0, 8, 8, 0, 8, 0],
             [0, 0, 0, 8, 8, 8],
             [8, 8, 0, 0, 0, 5]]

salir_del_laberinto(laberinto, 0, 0)
 






            


              
              