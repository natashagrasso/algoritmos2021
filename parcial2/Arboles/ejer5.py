""" . Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para 
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a 
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol. """

from  arbol_binario import Arbol

arbol = Arbol()
arbol_superheroe = Arbol()
arbol_villano = Arbol()

bosque = []  #es una lista en la cual tenemos cada uno de los arboles



superheroe = {'name': 'Doctor Strnge', 'villano': True, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

superheroe = {'name': 'Capitan America', 'villano': False, 'aparicion': 1946}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

superheroe = {'name': 'Capitana Marvel', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

superheroe = {'name': 'Docasdasdas', 'villano': True, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

superheroe = {'name': 'Iron Man', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

superheroe = {'name': 'Iron Hulk', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

print('arbol ordenado alfabeticamente: ')   #puntoB
arbol.inorden()

""" #puntoC
print('la cantidad de superheroes que empiezan con la letra C son: ', arbol.contar_buscados('C')) """

""" #puntoD
print('la cantidad de superheroes son: ', arbol.contar_superheroes()) """

""" #puntoE
print('nombre modificado')
arbol.modificar('Doctor Strnge')
arbol.inorden() """

#puntoF
""" print('arbol ordenado de forma descendente ')
arbol.postorden() """
#PUNTOG
arbol.separar_heroes_de_villanos(arbol_superheroe,arbol_villano)
""" print('arbol superheroe')
arbol_superheroe.inorden()

print('arbol villano')
arbol_villano.inorden() """


bosque.append(arbol_superheroe)    #insertamos el nodo arbol
bosque.append(arbol_villano)


for arbol in bosque:
    
    print('cantidad de nodos del arbol',arbol.contar_nodos()) #I
    print('arbol ordenado alfabeticamente ')#II
    arbol.inorden()
    