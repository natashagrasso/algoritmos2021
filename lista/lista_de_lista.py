from lista import Lista 
lista_personas = Lista()

datos = [
    {'nombre':'juan','edad': 34, 'provincia' : 'chaco', 'dni': 32, 'autos': Lista()}, #creamos un campo que se llama autos, que es una lista
    {'nombre':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20, 'autos': Lista()},
    {'nombre':'maria','edad': 18, 'provincia' : 'entre rios', 'dni': 28, 'autos': Lista()},
    {'nombre':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45, 'autos': Lista()},
    {'nombre':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38, 'autos': Lista()},

]

for persona in datos:
    lista_personas.insertar(persona,'nombre')

autos1 = {'modelo': 2020, 'marca': 'fiat','patente': 'abc123'}
autos2 = {'modelo': 2020, 'marca': 'ford','patente': 'abc456'}

#le cargamos un auto a carlos
pos = lista_personas.busqueda('carlos', 'nombre', '38', 'dni')
if (pos != -1):
    lista_personas.obtener_elemento(pos)['autos'].insertar(autos1, 'marca')
    lista_personas.obtener_elemento(pos)['autos'].insertar(autos2, 'marca') #otra forma de mostrar los autos de carlos, es poniendo en vez de insertar, barrido()

#para modificar un auto: lo primero es identificar la person, una vez que ya se cual es el elemento principal al que tengo que ir ..
pos_auto = lista_personas.obtener_elemento(pos)['autos'].busqueda('fiat', 'marca')#sobre esta lista hago la busqueda del auto que quiero modificar
if (pos_auto != -1): 
    lista_personas.obtener_elemento(pos)['autos'].obtener_elemento(pos_auto)['modelo'] = 2010



lista_personas.barrido_lista_autos() #barrido con la lista