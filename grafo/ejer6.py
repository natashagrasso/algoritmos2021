""" 6. Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio
20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
representa, no más de 20 palabras;
b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
pareja, la etiquetas de dichas aristas son estos nombre de relación.
c. dado el nombre de un dios mostrar los hijos de este;
d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación entre ambos;
f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
camino más corto el que tenga menor número de aristas;
g. realizar un barrido en profundidad y amplitud de dicho grafo;
h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
i. mostrar todos los ancestros de un determinado dios;
j. mostrar todos los nietos de Cronos;
k. mostrar todos los hijos de Tea; """


from GrafoTDA import Grafo

dioses = Grafo(dirigido=False)


dioses.insertar_vertice('Ouranos', data ='acercamiento a la mitologia griega') #Escribir descripcion, donde la descripcion esta en el campo otros
dioses.insertar_vertice("Gaia", data ="diosa del misterio") 
dioses.insertar_vertice("Themis", data ="diosa del misterio") 
dioses.insertar_vertice("Minemosyne", data ="diosa del misterio")  
dioses.insertar_vertice("Hera", data ="diosa del misterio")
dioses.insertar_vertice("Hyperion", data ="diosa del misterio") 
dioses.insertar_vertice("Theia", data ="diosa del misterio") 
dioses.insertar_vertice("Krios", data ="diosa del misterio")
dioses.insertar_vertice("Kronos", data ="diosa del misterio")
dioses.insertar_vertice("Rhea", data ="diosa del misterio")
dioses.insertar_vertice("Kdios", data ="diosa del misterio")
dioses.insertar_vertice("Phoibe", data ="diosa del misterio")
dioses.insertar_vertice("Iapetos", data ="diosa del misterio")
dioses.insertar_vertice("Okeanos", data ="diosa del misterio")
dioses.insertar_vertice("Tethys", data ="diosa del misterio")
dioses.insertar_vertice("Helios", data ="diosa del misterio")
dioses.insertar_vertice("Eos", data ="diosa del misterio")
dioses.insertar_vertice("Selene", data ="diosa del misterio")
dioses.insertar_vertice("Prometheus", data ="diosa del misterio")
dioses.insertar_vertice("Epimetheus", data ="diosa del misterio")
dioses.insertar_vertice("Atlas", data ="diosa del misterio")
dioses.insertar_vertice("Plevone", data ="diosa del misterio")
dioses.insertar_vertice("Hades", data ="diosa del misterio")
dioses.insertar_vertice("Demeter", data ="diosa del misterio")
dioses.insertar_vertice("Poseidon", data ="diosa del misterio")
dioses.insertar_vertice("Hestia", data ="diosa del misterio")
dioses.insertar_vertice("Zeus", data ="diosa del misterio")
dioses.insertar_vertice("Leto", data ="diosa del misterio")
dioses.insertar_vertice("Semelle", data ="diosa del misterio")
dioses.insertar_vertice("Maia", data ="diosa del misterio")
dioses.insertar_vertice("Persephone", data ="diosa del misterio")
dioses.insertar_vertice("Aphrodite", data ="diosa del misterio")
dioses.insertar_vertice("Ares", data ="diosa del misterio")
dioses.insertar_vertice("Athena", data ="diosa del misterio")
dioses.insertar_vertice("Apollo", data ="diosa del misterio")
dioses.insertar_vertice("Artemis", data ="diosa del misterio")
dioses.insertar_vertice("Dyonisos", data ="diosa del misterio")
dioses.insertar_vertice("Hermes", data ="diosa del misterio")
dioses.insertar_vertice("Hephaistos", data ="diosa del misterio")
dioses.insertar_vertice("Penelopeia", data ="diosa del misterio")
dioses.insertar_vertice("Phobos", data ="diosa del misterio")
dioses.insertar_vertice("Deimos", data ="diosa del misterio")
dioses.insertar_vertice("Eros", data ="diosa del misterio")
dioses.insertar_vertice("Himeros", data ="diosa del misterio")
dioses.insertar_vertice("Hermaphrodite", data ="diosa del misterio")
dioses.insertar_vertice("Pan", data ="diosa del misterio")


#Pareja
dioses.insertar_arista(1,"Ouranos","Gaia", data ={'relacion': ['pareja']})  #le pasamos 1 por el peso

#padre/hijo
dioses.insertar_arista(1,"Ouranos","Themis", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Ouranos","Minemosyne", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Hyperion", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Theia", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Krios", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Kronos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Rhea", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Kdios", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Phoibe", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Iapetos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Okeanos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Tethys", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ouranos","Themis", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino

#madre/hijo
dioses.insertar_arista(1,"Gaia","Minemosyne", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Hyperion", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Theia", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Krios", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Kronos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Rhea", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Kdios", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Phoibe", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Iapetos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Okeanos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Tethys", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Gaia","Themis", data ={'relacion': ['madre', 'hijo']}) #peso, origen, destino

#hermanos
dioses.insertar_arista(1,"Themis","Minemosyne", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Hyperion", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Themis","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Hyperion", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Minemosyne","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Theia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hyperion","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Krios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Theia","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Kronos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Krios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Rhea", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kronos","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Kdios", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Rhea","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Phoibe", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Kdios","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Iapetos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phoibe","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Iapetos","Okeanos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Iapetos","Tethys", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Okeanos","Tethys", data ={'relacion': ['hermanos']})


#Pareja
dioses.insertar_arista(1,"Hyperion","Theia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hyperion","Helios", data ={'relacion': ['padre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Hyperion","Eos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Hyperion","Selene", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Theia","Helios", data ={'relacion': ['madre', 'hijo']}) #peso, origen, destino
dioses.insertar_arista(1,"Theia","Eos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Theia","Selene", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Helios","Eos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Helios","Selene", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Eos","Selene", data ={'relacion': ['hermanos']})

#pareja
dioses.insertar_arista(1,"Kronos","Rhea", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Kronos","Hades", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Demeter", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Poseidon", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Hestia", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Hera", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Kronos","Zeus", data ={'relacion': ['padre', 'hijo']}) 
#madre/hijo
dioses.insertar_arista(1,"Rhea","Hades", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Demeter", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Poseidon", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Hestia", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Hera", data ={'relacion': ['madre', 'hijo']}) 
dioses.insertar_arista(1,"Rhea","Zeus", data ={'relacion': ['madre', 'hijo']}) 
#hermanos
dioses.insertar_arista(1,"Hades","Demeter", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Poseidon", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hades","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Poseidon", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Demeter","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Hestia", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Poseidon","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hestia","Hera", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hestia","Zeus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Hera","Zeus", data ={'relacion': ['hermanos']})


#pareja
dioses.insertar_arista(1,"Kdios","Phoibe", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Kdios","Leto", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Phoibe","Leto", data ={'relacion': ['madre', 'hijo']}) 

#padre/hijo
dioses.insertar_arista(1,"Iapetos","Prometheus", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Iapetos","Epimetheus", data ={'relacion': ['padre', 'hijo']}) 
dioses.insertar_arista(1,"Iapetos","Atlas", data ={'relacion': ['padre', 'hijo']}) 
#hermanos
dioses.insertar_arista(1,"Prometheus","Epimetheus", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Prometheus","Atlas", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Epimetheus","Atlas", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Okeanos","Tethys", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Okeanos","Plevone", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Tethys","Plevone", data ={'relacion': ['madre', 'hijo']}) 

#Pareja
dioses.insertar_arista(1,"Atlas","Plevone", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Atlas","Maia", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Plevone","Maia", data ={'relacion': ['madre', 'hijo']}) 

#Pareja
dioses.insertar_arista(1,"Zeus","Hera", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Ares", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Zeus","Hephaistos", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Hera","Ares", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Hera","Hephaistos", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Ares","Hephaistos", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Zeus","Demeter", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Persephone", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Demeter","Persephone", data ={'relacion': ['madre', 'hijo']})

#madre/hijo
dioses.insertar_arista(1,"Leto","Apollo", data ={'relacion': ['madre', 'hijo']})#madre/hijo
dioses.insertar_arista(1,"Leto","Artemis", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Apollo","Artemis", data ={'relacion': ['hermanos']})


#Pareja
dioses.insertar_arista(1,"Zeus","Maia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Zeus","Hermes", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Maia","Hermes", data ={'relacion': ['madre', 'hijo']})

#madre/hijo
dioses.insertar_arista(1,"Semelle","Dyonisos", data ={'relacion': ['madre', 'hijo']})

#Pareja
dioses.insertar_arista(1,"Ares","Aphrodite", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Ares","Phobos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Deimos", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Eros", data ={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1,"Ares","Himeros", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Aphrodite","Phobos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Deimos", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Eros", data ={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1,"Aphrodite","Himeros", data ={'relacion': ['madre', 'hijo']})
#hermanos
dioses.insertar_arista(1,"Phobos","Deimos", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phobos","Eros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Phobos","Himeros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Deimos","Eros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Deimos","Himeros", data ={'relacion': ['hermanos']})
dioses.insertar_arista(1,"Eros","Himeros", data ={'relacion': ['hermanos']})

#Pareja
dioses.insertar_arista(1,"Hermes","Penelopeia", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hermes","Pan", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Penelopeia","Pan", data ={'relacion': ['madre', 'hijo']})

#Pareja
dioses.insertar_arista(1,"Hermes","Aphrodite", data ={'relacion': ['pareja']})
#padre/hijo
dioses.insertar_arista(1,"Hermes","Hermaphrodite", data ={'relacion': ['padre', 'hijo']})
#madre/hijo
dioses.insertar_arista(1,"Aphrodite","Hermaphrodite", data ={'relacion': ['madre', 'hijo']})

""" origen = dioses.buscar_vertice('Cronos')
dioses.barrido_amplitud(origen)
print() """

# origen = dioses.buscar_vertice('Persefone')
# print('apmlitud')
# dioses.barrido_amplitud(0)
# print('fin')

""" for i in range(dioses.inicio.tamanio()):
    dios=dioses.inicio.obtener_elemento(i)
    print('aristas', dios['info'])
    for j in range (dios['aristas'].tamanio()):
        print(dios['aristas'].obtener_elementos(j))

    print() """

#PUNTO.C
# print('HIJOS:')
# origen = dioses.buscar_vertice('Kronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'hijo'):
#             print(arista)
# print()

#PUNTO.D
# print('PADRES:')
# origen = dioses.buscar_vertice('Kronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'padre'):
#             print(arista)

# print('HERMANOS:')
# origen = dioses.buscar_vertice('Kronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['data']['relacion'][0] == 'hermanos'):
#         print(arista)    

#PUNTO.E
# print()
# origen = dioses.buscar_vertice('Kronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['destino']=='Zeus'):
#         print('hay relacion y es : ')
#         print(arista) 




#tmb se puede determinar si es relacion directa con la funcion es_adyacente
#print(dioses.es_adyacente('Zeus', 'Urano')) #este devuelve VoF

#en cambio:
#dioses.adyacentes('Zeus')   #muestra la lista completa


# #para mostrar toda la info si hay relacion
# def directo(ver_origen, ver_destino):
#     print('tiene relacion directa:')
#     pos = dioses.buscar_arista(ver_origen, ver_destino)
#     print(pos)
#     if(pos != 1):
#         pos_aux = dioses.buscar_vertice('Zeus')
#         print(dioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))




#PUNTO.F
# vertice_origen = dioses.buscar_vertice('Themis')
# vertice_destino = dioses.buscar_vertice('Krios')

# camino = dioses.dijkstra(vertice_origen, vertice_destino)

# destino = 'Krios'
# costo = None
# while(not camino.pila_vacia()):
#     dato = camino.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]
# print('el costo total del camino es:', costo)

#PUNTO.G
# print ('barrido en profundidad')
# dioses.barrido_profundidad

# print ('barrido en amplitud')
# dioses.barrido_amplitud

#PUNTO-I
# dioses.ancestro('Persephone')                   

#PUNTO.H
""" print('barrido madre: ', dioses.tamanio())
dioses.marcar_no_visitado()
dioses.barrido_madre(0) """

dioses.nietos('Ouranos')