# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.


from GrafoTDA import Grafo

#PUNTO.6 
equipos= Grafo(dirigido=False)
#PUNTO-1
equipos.insertar_vertice('Manjaro', data= 'PC')
equipos.insertar_vertice('Parrot', data= 'PC')
equipos.insertar_vertice('Fedora', data= 'PC')
equipos.insertar_vertice('Mint', data='PC')
equipos.insertar_vertice('Ubuntu', data='PC')
equipos.insertar_vertice('Arch', data= 'Notebook')
equipos.insertar_vertice('Red Hat', data= 'Notebook')
equipos.insertar_vertice('Debian', data= 'Notebook')
equipos.insertar_vertice('Impresora', data= 'Impresora')
equipos.insertar_vertice('Guarani', data= 'Servidor')
equipos.insertar_vertice('MongoDB', data= 'Servidor')
equipos.insertar_vertice('Switch1', data= 'Switch')
equipos.insertar_vertice('Switch2', data= 'Switch')
equipos.insertar_vertice('Router1', data= 'Router')
equipos.insertar_vertice('Router2', data= 'Router')
equipos.insertar_vertice('Router', data= 'Router')

equipos.insertar_arista(50,'Router2', 'Router3')
equipos.insertar_arista(37,'Router2', 'Router1')
equipos.insertar_arista(9,'Router2', 'guarani')
equipos.insertar_arista(25,'Router2', 'Red Hat')
equipos.insertar_arista(29,'Switch1', 'Router1')
equipos.insertar_arista(80,'Switch1', 'Mint')
equipos.insertar_arista(22,'Switch1', 'impresora')
equipos.insertar_arista(18,'Switch1', 'Ubuntu')
equipos.insertar_arista(40,'Switch2', 'Manjaro')
equipos.insertar_arista(12,'Switch2', 'Parrot')
equipos.insertar_arista(5,'Switch2', 'MongoDB')
equipos.insertar_arista(56,'Switch2', 'Arch')
equipos.insertar_arista(3,'Switch2', 'Fedora')


#PUNTO.2
Red_hat= "Red Hat"
inicio = equipos.buscar_vertice(Red_hat)

print("BARRIDO EN PROFUNDIDAD")
equipos.barrido_profundidad(inicio)
equipos.marcar_no_visitado()
print('----------------------------------')
print("BARRIDO EN AMPLITUD")
equipos.barrido_amplitud(inicio)
equipos.marcar_no_visitado()


debian= "Debian"
inicio = equipos.buscar_vertice(debian)
print("BARRIDO EN PROFUNDIDAD")
equipos.barrido_profundidad(inicio)
equipos.marcar_no_visitado()

print('----------------------------------')

print("BARRIDO EN AMPLITUD")
equipos.barrido_amplitud(inicio)
equipos.marcar_no_visitado()

arch= "Arch"
inicio = equipos.buscar_vertice(arch)
print("BARRIDO EN PROFUNDIDAD")
equipos.barrido_profundidad(inicio)
equipos.marcar_no_visitado()

print('----------------------------------')

print("BARRIDO EN AMPLITUD")
equipos.barrido_amplitud(inicio)
equipos.marcar_no_visitado() 


#PUNTO-5
equipos.eliminar_vertice('Impresora')
#equipos.eliminar_arista('Impresora')
inicio = "Ubuntu"

origen = equipos.buscar_vertice(inicio)

print('efectivamente fue borrada')
equipos.barrido_amplitud(origen)


#PUNTO-4
bosque = equipos.prim()
print('--ARBOL DE EXPANSION--')
peso = 0
for elemento in bosque:
    print(elemento[1][0], '-', elemento[1][1])
    peso += elemento[0]
print('costo total', peso)



#PUNTO-3 
debian = 'Debian'
origen = equipos.buscar_vertice(debian)

Mongo = 'MongoDB'
destino = equipos.buscar_vertice(Mongo)

camino = equipos.dijkstra(origen,destino)

print("Camino mas corto es: ")
destino = Mongo
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino desde debian a mongo es :', costo)
print()






