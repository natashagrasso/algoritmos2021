"""  Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles. """

from arbol_binario import Arbol

arbol = Arbol( )

criaturas = {'nombre': 'Ladon', 'descripcion': 'era un dragón de cien cabezas cada una de las cuales hablaba una lengua diferente', 'derrotada_por': 'Edipo', 'capturada_por': 'Heracles'}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Cerbero', 'descripcion': 'era un perro de aspecto monstruoso con tres cabezas y una cola de serpiente.', 'derrotada_por': 'Hercules', 'capturada_por': 'Heracles'}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Toro de Creta', 'descripcion': 'era un monstruo con cuerpo de hombre y cabeza de toro', 'derrotada_por': 'Perseo', 'capturada_por': 'Hercules'}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Talos', 'descripcion': 'era un colosal y espeluznante monstruo alado: su estatura era tal que podía alcanzar las estrellas', 'derrotada_por': 'Tadeo', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Cierva Cerinea', 'descripcion': 'tenía pezuñas de bronce y cornamenta de oro,', 'derrotada_por': 'Heracles', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Jabalí de Erimanto', 'descripcion':'era una criatura que por todo el contorno destrozaba las cosechas, los árboles y perseguía a los animales matando a sus crías', 'derrotada_por': '-', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Basilisco', 'descripcion': 'era una serpiente gigante cargada de veneno letal y que podía matar con la simple mirada, que consideraban el rey de las serpientes', 'derrotada_por': 'Heracles', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'sirenas', 'descipcion': 'eran híbridas con cuerpo de ave y rostro de mujer que atraían a los marineros con sus hipnóticos cantos, conduciéndolos a un destino fatal', 'derrotada_por': '-', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)

criaturas = {'nombre': 'Aves del Estínfalo', 'descipcion': 'eran híbridas con cuerpo de ave y rostro de mujer que atraían a los marineros con sus hipnóticos cantos, conduciéndolos a un destino fatal', 'derrotada_por': '-', 'capturada_por': ''}
arbol = arbol.insertar_nodo(criaturas['nombre'], criaturas)


#puntoA
# dic = {}
# arbol.contar_criaturas_derrotadas(dic)
# #print(dic)

# def ordenar(item):
#     return item[1]

# lista = list(dic.items())
# lista.sort(key=ordenar, reverse=True)
# print(lista[:3])

# for elemento in lista:
#     print(elemento)

# print('listado inorden de las criaturas : ')   #puntoA
# arbol.inorden_criaturas() 


# buscado="Talos"                 #puntoC
# pos=arbol.busqueda(buscado)
# if pos:
#     print("info de la criatura; ",buscado,"",pos.datos)
#     print()



# arbol.busqueda_proximidad2('Heracles')    #puntoE


# arbol.busqueda_proximidad2('-')   #puntoF



# lista_criaturas = ['Basilisco', 'sirenas', 'Cierva Cerinea']    #puntoJ
# for eliminado in lista_criaturas:
#     arbol.eliminar_nodo(eliminado) 

# arbol.inorden()



# arbol.inorden()       #puntoH
# lista_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea','Jabalí de Erimanto']
# for buscado in lista_criaturas:
#     pos = arbol.busqueda(buscado)
#     pos.datos['capturada_por']= 'Heracles'
#     # print(pos.datos)

# print('----------------')    
# arbol.inorden()



# arbol.inorden()#puntoL

# pos = arbol.busqueda('Ladon')   
# pos.datos['nombre']= 'Dradon Ladon'
# pos.info= 'Dradon Ladon'
# print('----------------')    
# arbol.inorden()

# arbol.barrido_por_nivel()  #puntoM

# print('las criaturas capturadas por Heracles son: ')  #puntoN
# arbol.busqueda_proximidad3('Heracles') 



""" arbol.inorden()                                         
buscado = input('ingrese lo que desa buscar ')
arbol.busqueda_proximidad(buscado)
print()
buscado = input('ingrese el nombre de la criatura que desea modificar ')
pos = arbol.busqueda(buscado)
if(pos):
    nuevo_nombre = input('ingrese el nuevo nombre ')
    nombre, criaturas = arbol.eliminar_nodo(buscado)
    criaturas['criatura'] = nuevo_nombre
    arbol = arbol.insertar_nodo(nuevo_nombre, criaturas)
    print()
arbol.inorden() """