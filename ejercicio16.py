""" Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente 
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la 
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con 
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión. """

from cola import Cola

class Documentos (object):
    def __init__ (self,ID, nombre): 
        self.ID = ID
        self.nombre = nombre 


cola_doc = Cola()
cola_aux = Cola()

documentos = Documentos('1','raul') #puntoA
cola_doc.arribo(documentos)
documentos = Documentos('1','dario bel')
cola_doc.arribo(documentos)
documentos = Documentos('1','jorge romero')
cola_doc.arribo(documentos)

x = cola_doc.en_frente() 
print (x.ID,x.nombre)#puntoB

documentos = Documentos('2','julio') #puntoC
cola_doc.arribo(documentos)
documentos = Documentos('2','ruben')
cola_doc.arribo(documentos)

documentos = Documentos('3','karla') #puntoD

cantidad_elementos = 0 
while(cantidad_elementos < cola_doc.tamanio()):
    dato = cola_doc.mover_al_final()
    cola_aux.arribo(dato)    
    cantidad_elementos += 1

for i in range(2): #puntoE
    x = cola_aux.atencion()
    print(x.ID,x.nombre)

documentos = Documentos('1','sebas') #puntoF
cola_doc.arribo(documentos)
documentos = Documentos('1','eric')  
cola_doc.arribo(documentos)
documentos = Documentos('3','flor') 
cola_doc.arribo(documentos) 

cantidad_elementos = 0 #puntoG
while(cantidad_elementos < cola_doc.tamanio()):
    dato = cola_doc.mover_al_final()
    print(dato.ID, dato.nombre)    
    cantidad_elementos += 1