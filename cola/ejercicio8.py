""" Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando 
solo una cola como estructura auxiliar """

from cola import Cola

cola_datos = Cola()
cola_aux = Cola()

numeros = [0, 3, 1, 7, 2, 10]

for i in numeros:
    if (cola_datos.cola_vacia()):  ## Si la cola está vacía, inserta el primer elemento
        cola_datos.arribo(i)
    elif (i > cola_datos.en_frente()): ## Si el nuevo elemento es mayor al primer elemento de la cola empieza a retirar elementos
        while(not cola_datos.cola_vacia() and i > cola_datos.en_frente()):  ##Retira elementos hasta que la cola se vacía o encuentra un elemento mayor al que se quiere insertar 
            cola_aux.arribo(cola_datos.atencion()) ## Va cargando los elementos retirados en una auxiliar para no perderlos

        #Cuando la cola se vacía o encuentra un elemento mayor, inserta el nuevo elemento en la auxiliar
        cola_aux.arribo(i) 

        ## Si la cola original todavía tenia elementos, los pasa a la auxiliar, insertarlos despues del nuevo elemento, ya que son mayores
        while (not cola_datos.cola_vacia()):
            cola_aux.arribo(cola_datos.atencion())

        ## Vuelve a pasar todos los elementos a la cola original, con el nuevo elemento ya cargado
        while (not cola_aux.cola_vacia()):
            cola_datos.arribo(cola_aux.atencion())


cantidad_elementos = 0 
while(cantidad_elementos < cola_datos.tamanio()):
    datos = cola_datos.mover_al_final()
    print(datos)    
    cantidad_elementos += 1