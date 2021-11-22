""" 16. Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determinado país teniendo en cuenta los siguientes requerimientos:
a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Atenas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Artemisa (Éfeso) y Teatro de Dionisio (Acrópolis)
c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
el templo de Apolo, en Delfos."""

from GrafoTDA import Grafo

templo = Grafo(dirigido=False)
#PUNTO-A 
#PUNTO-B
templo.insertar_vertice('Ateneas', data= {'latitud':20.9, 'longitud':43.0})
templo.insertar_vertice('Zeus', data= {'latitud':30.2, 'longitud':53.1})
templo.insertar_vertice('Hera', data= {'latitud':98.1, 'longitud':23.4})
templo.insertar_vertice('Apolo', data= {'latitud':21.8, 'longitud':78.5})
templo.insertar_vertice('Poseidon', data= {'latitud':56.6, 'longitud':49.0})
templo.insertar_vertice('Artemisa', data= {'latitud':28.9, 'longitud':76.0})
templo.insertar_vertice('Teatro de Dionisio', data= {'latitud':22.9, 'longitud':122.5})

#insertar atenea
templo.insertar_arista(1.1, 'Ateneas','Zeus')
templo.insertar_arista(11.2, 'Ateneas','Hera')
templo.insertar_arista(20.2, 'Ateneas','Apolo')
templo.insertar_arista(15.8, 'Ateneas','Poseidon')
templo.insertar_arista(21.9, 'Ateneas','Artemisa')
templo.insertar_arista(17.8, 'Ateneas','Teatro de Dionisio')

#insertar Zeus
templo.insertar_arista(22.4, 'Zeus','Hera')
templo.insertar_arista(12.9, 'Zeus','Apolo')
templo.insertar_arista(20.4, 'Zeus','Poseidon')
templo.insertar_arista(21.4, 'Zeus','Artemisa')
templo.insertar_arista(99.2, 'Zeus','Teatro de Dionisio')

#insertar Hera
templo.insertar_arista(12.9, 'Hera','Apolo')
templo.insertar_arista(20.4, 'Hera','Poseidon')
templo.insertar_arista(21.4, 'Hera','Artemisa')
templo.insertar_arista(99.2, 'Hera','Teatro de Dionisio')

#insertar Apolo 
templo.insertar_arista(56.4, 'Apolo','Poseidon')
templo.insertar_arista(23.4, 'Apolo','Artemisa')
templo.insertar_arista(21.2, 'Apolo','Teatro de Dionisio')

#insertar Poseidon 
templo.insertar_arista(223.4, 'Poseidon','Artemisa')
templo.insertar_arista(933.2, 'Poseidon','Teatro de Dionisio')

#insertar Artemisa 
templo.insertar_arista(993.2, 'Artemisa','Teatro de Dionisio')




#PUNTO-C
""" bosque = templo.prim()
print('--ARBOL DE EXPANSION--')
peso = 0
for elemento in bosque:
    print(elemento[1][0], '-', elemento[1][1])
    peso += elemento[0]
print('costo total', peso)
print() """

#PUNTO-D
""" atenea = 'Ateneas'
origen = templo.buscar_vertice('Ateneas')

apolo = 'Apolo'
destino = templo.buscar_vertice('Apolo')

camino = templo.dijkstra(origen,destino)
print("Camino mas corto para ir desde el templo Atenea(el Partenón) hasta el templo de Apolo(en Delfos)")
destino = apolo
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino es :', costo)
print() """