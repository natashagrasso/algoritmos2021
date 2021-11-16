""" El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
resolver los siguientes requerimientos:
1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
distintos, los códigos no pueden ser repetidos (tenga cuidado);
2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
código;
3. realizar un barrido en orden del árbol ordenado por nombre;
4. mostrar toda la información del dinosaurio 792;
5. mostrar toda la información de todos los T-Rex que hay en la isla;
6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
cargado, su nombre correcto es Stygimoloch;
7. mostrar la ubicación de todos los Raptores que hay en la isla;
8. contar cuantos Diplodocus hay en el parque;
9. debe cargar al menos 15 elementos. """

from arbol_binario import Arbol

arbol1 = Arbol( )
arbol2 = Arbol( )


dinosaurios = {'nombre': 'Diplodocus', 'codigo_5_digitos': '5B', 'zona_ubicacion': 'isla nublar' }
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)

dinosaurios = {'nombre': 'T-Rex', 'codigo_5_digitos': '7A', 'zona_ubicacion': 'zona central'}
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)

dinosaurios = {'nombre': 'Sgimoloch', 'codigo_5_digitos': '7A', 'zona_ubicacion': 'isla sorna'}
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)

dinosaurios = {'nombre': 'Pterrandon', 'codigo_5_digitos': '792', 'zona_ubicacion': 'zona central'}
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)

dinosaurios = {'nombre': 'T-Rex', 'codigo_5_digitos': '5UU', 'zona_ubicacion': 'isla nublar'}
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)

dinosaurios = {'nombre': 'Sgimoloch', 'codigo_5_digitos': '5UU', 'zona_ubicacion': 'isla nublar'}
arbol1 = arbol1.insertar_nodo(dinosaurios['nombre'], dinosaurios)
arbol2 = arbol2.insertar_nodo(dinosaurios['codigo_5_digitos'], dinosaurios)



#PUNTO3
""" print('Arbol ordenado por nombre')   
arbol.inorden() """

#PUNTO5


""" print("info de todos los T-Rex es:") 
arbol1.barrido_rex() """

#punto4
""" 
buscado= '792'              
pos=arbol2.busqueda(buscado)
if pos:
    print("info del dinosaurio 792 es : ",buscado,"",pos.datos)
    print() 
 """

#punto6

""" buscado = input('ingrese el nombre que desea modificar ')
pos = arbol1.busqueda(buscado)
if(pos):

    nuevo_nombre = input('ingrese el nuevo nombre ')
    nombre, dinosaurios = arbol1.eliminar_nodo(buscado)
    dinosaurios['nombre'] = nuevo_nombre
    arbol = arbol1.insertar_nodo(nuevo_nombre, dinosaurios)
    print() """





#PUNTO7
""" buscado="Raptores"                 #puntoC
pos=arbol1.busqueda(buscado)
if pos:
    print("la ubicacion de los raptores es ",buscado,"",pos.datos)
    print() """


#PUNTO8
""" dic = {}
arbol1.contar_Diplodocus(dic)
print(dic)

def ordenar(item):
    return item[1] """