from lista import Lista
from heapTDA import HeapMin
from cola import Cola
from pila import Pila
from math import inf
from copy import deepcopy

#clase grafo, implementacion lista de listas de adyacencia

class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido #tmb tenemos el tamaño de nuestro grafo  
        self.inicio = Lista() #tenemos un punto de inicio, que es por donde vamos a arrancar


    def insertar_vertice(self, dato, criterio='info', data=None): #el dato es obligatorio, y el "otro" es opcional
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista(), 'data': data}, criterio)# el campo aristas es una lista
    #cada vez que se inserta un dato, se crea un vertice que va a tener esa informacion (info, visitado, y una lista de aristas, con el campo info le decimos por que campo lo vamos a ordenar


    def insertar_arista(self, peso, origen, destino, criterio='destino', data=None):#el peso nos indica si una coneccion entre dos vertices(origen y destino ) tiene algun valor
        ver_origen = self.inicio.busqueda(origen, 'info')   #para insertar una arista nos tenemos que asegurar que existan los dos vertices,entonces lo buscamos por el campo info
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1): #si origen y destino  existen, insertamos una arista

            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino, 'data': data}, criterio)
            #basicamente, la informacion que se tiene en cada arista es, el lugar, el peso etc

            if(not self.dirigido and origen != destino): #si el grafo es dirigido tenemos que hacer la insercion al reves
                data_aux = deepcopy(data)
                if(data):
                    data_aux['relacion'].reverse()
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen, 'data': data_aux}, criterio)
        else:
            print('los vertices origen o destino no estan en el grafo....', origen, destino)


    def grafo_vacio(self): #si la lista esta vacia entonces el grafo tmb
        return self.inicio.lista_vacia()

    def tamanio(self): #el tamanio nos devuelve la cant de vertices y aristas 
        return self.inicio.tamanio()
    
    def buscar_vertice(self, clave, criterio='info'):      #lo bucamos por el campo info
        return self.inicio.busqueda(clave, criterio=criterio)   #le pasamos lo que estamos buscando


    def buscar_arista(self, origen, destino, criterio='destino'):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):    #chequeamos que exista
            #una vez que sabemos donde esta, lo buscamos y a partir de èste accedo al campo arista y sobre este hacemos la busqueda, que lo hace sobre el campo destino(campo por defecto)
            return self.inicio.obtener_elemento(ver_origen)['aristas'].busqueda(destino, criterio)
        else:
            return ver_origen


    def barrido_vertices(self):  #barrido sobre los vertices
        self.inicio.barrido()


    #necesitamos saber si ese vertice es adyacente de manera directa  
    #devuelve un booleano
    #adyacente significa paso directo
    def es_adyacente(self, origen, destino):    #le pasamos el vertice(origen) y el destino
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            destino = self.buscar_arista(origen, destino)
            if(destino != -1):
                return True
            else:
                return False
        else:
            return False


    #barrido de los nodos adyacentes de un vertice origen
    #hace un barrido de todos los adyacentes
    def adyacentes(self, origen):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):   #si existen hacemos un barrido de dicho vertice
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()


    def eliminar_vertice(self, clave):  #le pasamos el grafo y el vertice que se quiere eliminar
        aux = self.inicio.eliminar(clave, criterio='info')
        for posicion in range(self.tamanio()):  #posicion va de 0 a tamaño
            origen = self.inicio.obtener_elemento(posicion)['info']
            self.eliminar_arista(origen, clave)
        return aux



    def eliminar_arista(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')   #buscamos el origen 
        if(ver_origen != -1):   #una vez que lo encontramos 
            self.inicio.obtener_elemento(ver_origen)['aristas'].eliminar(destino, 'destino') #obtenemos el vertice origen, y lo eliminamos por el campo destino
            if(not self.dirigido):
                ver_destino = self.inicio.busqueda(destino, 'info')
                if(ver_destino != -1):
                    self.inicio.obtener_elemento(ver_destino)['aristas'].eliminar(origen, 'destino')


    #el barrido en profundidad hace salteos mucho mas en profundidad 
    def barrido_profundidad(self, ver_origen):
        """Barrido en profundidad del grafo."""
        while(ver_origen < self.inicio.tamanio()):#si la cantidad de aristas es menor o igual que el tamaño, significa que tenemos aristas para recorrer
             #a partir del vertice origen, nos fijamos si esta visitado, si no esta visitado lo tengo que mostrar
           
            vertice = self.inicio.obtener_elemento(ver_origen)  #obtenemos el elemento de la posicion 0, buscamos el vertice corresp a ese
            if(not vertice['visitado']):
                vertice['visitado'] = True  #lo ponemos en visitado y cambiamos el valor a true, y se muestra el valor, donde accede a la lista de sus aristas
                print(vertice['info'])
                aristas = 0
                while(aristas < vertice['aristas'].tamanio()):
                    arista = vertice['aristas'].obtener_elemento(aristas)
                    pos_vertice = self.buscar_vertice(arista['destino'])
                    nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                    if(not nuevo_vertice['visitado']):#si nuevo vertice no esta visitado, va a barrer en profundidad
                        self.barrido_profundidad(pos_vertice)
                    aristas += 1
            ver_origen += 1


#en el barrido amplitud se barre lo que esta mas proximo al vertice, y desp salta a los demas vertices 
    def barrido_amplitud(self, ver_origen):
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(ver_origen < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                cola.arribo(vertice)
                while(not cola.cola_vacia()):
                    nodo = cola.atencion()
                    print(nodo['info'], nodo['data'])
                    aristas = 0
                    while(aristas < nodo['aristas'].tamanio()):
                        adyacente = nodo['aristas'].obtener_elemento(aristas)
                        pos_vertice = self.buscar_vertice(adyacente['destino'])
                        nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                        if(not nuevo_vertice['visitado']):
                            nuevo_vertice['visitado'] = True
                            cola.arribo(nuevo_vertice)
                        aristas += 1
            ver_origen += 1


#si no marcamos los vertices como visitados, podemos entrar en un loop y no salir mas
    def marcar_no_visitado(self):
        """Marca todos losvertices del grafo como no visitados."""
        for i in range(self.tamanio()):
            self.inicio.obtener_elemento(i)['visitado'] = False



    def existe_paso(self, ver_origen, ver_destino):
        """Barrido en profundidad del grafo."""
        resultado = False
        vertice = self.inicio.obtener_elemento(ver_origen)
        if(not vertice['visitado']):
            vertice['visitado'] = True
            aristas = 0
            while(aristas < vertice['aristas'].tamanio() and not resultado):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = self.buscar_vertice(arista['destino'])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                destino = self.inicio.obtener_elemento(ver_destino)
                if(nuevo_vertice['info'] == destino['info']):
                    return True
                else:
                    resultado = self.existe_paso(pos_vertice, ver_destino)
                aristas += 1
        return resultado


    #nos permite encontrar el camino mas corto
    def dijkstra(self, ver_origen, ver_destino):#necesitamos del heap
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        #solo sirve para trabajar con grafos con peso positivo
        no_visitados = HeapMin()
        camino = Pila() #en la lpila guardamos el camino
        aux = 0
        while(aux < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            vertice_aux = self.inicio.obtener_elemento(aux)
            vertice_aux['anterior'] = None
            if(vertice_aux['info'] == vertice['info']):
                no_visitados.arribo([vertice_aux['info'], None], 0)
            else:
                no_visitados.arribo([vertice_aux['info'], None], inf)
            aux += 1
        while(not no_visitados.vacio()):
            dato = no_visitados.atencion()
            camino.apilar(dato)
            pos_aux = self.buscar_vertice(dato[1][0])
            vertice_aux = self.inicio.obtener_elemento(pos_aux)
            aristas = 0
            while(aristas < vertice_aux['aristas'].tamanio()):
                arista = vertice_aux['aristas'].obtener_elemento(aristas)
                pos_heap = no_visitados.busqueda(arista['destino'])
                if(pos_heap is not None and no_visitados.elementos[pos_heap][0] > dato[0] + arista['peso']):
                    no_visitados.elementos[pos_heap][1][1] = dato[1][0]
                    nuevo_peso = dato[0] + arista['peso']
                    no_visitados.cambiar_prioridad(pos_heap, nuevo_peso)
                aristas += 1
        # print(no_visitados.elementos)
        return camino

    def busqueda_prim(self, bosque, buscado):
        for elemento in bosque:
            if(buscado in elemento[1]):
                return elemento


    def prim(self):
        """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = HeapMin()
        origen = self.inicio.obtener_elemento(0)
        adyac = 0
        while(adyac < origen['aristas'].tamanio()):
            arista = origen['aristas'].obtener_elemento(adyac)
            aristas.arribo([origen['info'], arista['destino']], arista['peso'])
            adyac += 1
        # print(bosque)
        # print(aristas.elementos)
        # print()
        while(len(bosque) // 2 < self.tamanio() and not aristas.vacio()):
            dato = aristas.atencion()
            if(len(bosque) == 0) or ((self.busqueda_prim(bosque, dato[1][0]) is not None) ^ (self.busqueda_prim(bosque, dato[1][1]) is not None)):
                bosque.append(dato)
                pos_vertice = self.buscar_vertice(dato[1][1])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                adyac = 0
                while(adyac < nuevo_vertice['aristas'].tamanio()):
                    arista = nuevo_vertice['aristas'].obtener_elemento(adyac)
                    # print(arista)
                    aristas.arribo([nuevo_vertice['info'], arista['destino']], arista['peso'])
                    adyac += 1
            # print(bosque)
            # print(aristas.elementos)
            # a = input()
        return bosque



    def relaciones(self,relacion,buscado): #devuelve una relacion especifica
        origen = self.inicio.buscar_vertice(buscado)
        if (origen != -1):
            dios=self.inicio.obtener_elemento(origen)
            for i in range (dios['aristas'].tamanio()):
                aux= dios['aristas'].obtener_elemento(i)
                if (relacion in aux ['data']['relacion']):
                    print(aux['destino'])
        else:
            print('dios no encontrado')           


    def barrido_madre(self, ver_origen):    #usado para el ej 6 punto H
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(ver_origen < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                cola.arribo(vertice)
                while(not cola.cola_vacia()):
                    nodo = cola.atencion()
                    print(nodo['info'], nodo['data'])
                    for i in range (nodo['aristas'].tamanio()):
                        aristas=nodo['aristas'].obtener_elemento(i)
                        if (len(aristas['data']['relacion'])==2):
                            if (aristas['data']['relacion'][1]== 'madre'):
                                print(aristas['destino'])
                    aristas=0
                    while(aristas < nodo['aristas'].tamanio()):
                        adyacente = nodo['aristas'].obtener_elemento(aristas)
                        pos_vertice = self.buscar_vertice(adyacente['destino'])
                        nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                        if(not nuevo_vertice['visitado']):
                            nuevo_vertice['visitado'] = True
                            cola.arribo(nuevo_vertice)
                        aristas += 1
            ver_origen += 1        


    def ancestro(self,vertice_nombre):
        origen = self.buscar_vertice(vertice_nombre)
        if(origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
                dios_aux = dios['aristas'].obtener_elemento(i)['data']
                if(len(dios_aux['relacion']) > 1):
                    if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                        print(nombre_dios, dios_aux['relacion'])
                        self.ancestro(nombre_dios)


    def nietos(self,vertice_nombre):
        origen = self.buscar_vertice(vertice_nombre)
        if(origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
                dios_aux = dios['aristas'].obtener_elemento(i)['data']
                if(len(dios_aux['relacion']) > 1):
                    if(dios_aux['relacion'][1] == 'hijo'):
                        #print(nombre_dios, dios_aux['relacion'])
                        origen = self.buscar_vertice(nombre_dios)
                        if(origen != -1):
                            dios = self.inicio.obtener_elemento(origen)
                            for i in range(dios['aristas'].tamanio()):
                                nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
                                dios_aux = dios['aristas'].obtener_elemento(i)['data']
                                if(len(dios_aux['relacion']) > 1):
                                    if(dios_aux['relacion'][1] == 'hijo'):
                                        print(nombre_dios)
                                                 