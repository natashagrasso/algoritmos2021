"""  Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, 
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic """

from lista import Lista

class Superheroe (object):
    def __init__ (self, nombre,anio_aparicion, casa, biografia): 
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia= biografia
        

lista_personajes = Lista()
lista_A = Lista()
lista_B = Lista()
lista_S = Lista()
lista_aparicion_antesde1963 = Lista()

superheroes = [
    {'nombre':'Linterna Verde','anio_aparicion':1940, 'casa':'DC','biografia':'Linterna Verde es el alias de varios superhéroes  de la ficción del Universo DC, los cuales se caracterizan por un anillo de poder y la capacidad de crear manifestaciones de luz sólida con dichos anillos'},
    {'nombre':'Wolverine','anio_aparicion':1963, 'casa':'Marvel','biografia':'Wolverine, cuyo nombre de nacimiento es James Howlett ​ es un superheroe ficticio que aparece en los comics estadounidenses publicado por Marvel Comics, principalmente en asociación con los X-Men'},
    {'nombre':'Dr. Strange','anio_aparicion':1963, 'casa':'DC','biografia':'El doctor Stephen Vincent Strange es un superhéroe con armadura y cirujano ficticio que aparece en cómics estadounidenses publicados por Marvel Comics. Creado por el artista Steve Ditko y el escritor Stan Lee, ​ el personaje apareció por primera vez en Strange Tales #110'},
    {'nombre':'Capitana Marvel','anio_aparicion':2009, 'casa':'Marvel','biografia':'Una guerrera extraterrestre de la civilización Kree se encuentra atrapada en medio de una batalla. Con la ayuda de Nick Fury trata de descubrir los secretos de su pasado mientras aprovecha sus poderes para terminar la guerra.'},
    {'nombre':'Mujer Maravilla','anio_aparicion':1941, 'casa':'DC','biografia':'La Mujer Maravilla Es una princesa guerrera de las Amazonas, pueblo ficticio basado en el de las amazonas de la mitología griega. Diana ocasionalmente usa armamento adicional en una batalla formal, como por ejemplo el uso de una armadura ceremonial de oro con alas doradas, un yelmo o casco dorado adornado con la cabeza de un águila y una placa pectora'},
    {'nombre':'Flash','anio_aparicion':2014, 'casa':'DC','biografia':'Nueve meses después de que el laboratorio S.T.A.R. explotara, Barry despierta del coma y descubre que tiene el poder de la súper velocidad. Con la ayuda de su nuevo equipo, Barry, denominado ahora `Flash, luchará contra el crimen en Ciudad Central'},
    {'nombre':'Star-Lord','anio_aparicion':1980, 'casa':'Marvel','biografia':'Star-Lord es un personaje ficticio con traje que aparece en los cómics estadounidenses publicados por Marvel Comics. El personaje, creado por Steve Englehart y Steve Gan, apareció por primera vez en Marvel'},
    {'nombre':'Bene.','anio_aparicion':1880, 'casa':'Marvel','biografia':'un capo'},

]

cont_aparicion = []
cont_B = ''
cont_DC = 0
cont_Marvel = 0


for superheroe in superheroes:
    lista_personajes.insertar(superheroe,'nombre')

posCapitanaMarvel = lista_personajes.busqueda('Capitana Marvel', 'nombre') #puntoF
CapitanaMarvel = lista_personajes.obtener_elemento(posCapitanaMarvel)
print('la casa de la capitana marvel es: ', CapitanaMarvel['casa']) 

posCapitanaMarvel = lista_personajes.busqueda('Mujer Maravilla', 'nombre') #puntoF
CapitanaMarvel = lista_personajes.obtener_elemento(posCapitanaMarvel)
print('la casa de la Mujer Maravilla es: ', CapitanaMarvel['casa'])

lista_personajes.eliminar('Linterna Verde','nombre') #puntoA

posWolverine = lista_personajes.busqueda('Wolverine', 'nombre') #puntoB
aparicion_Wolverine = lista_personajes.obtener_elemento(posWolverine)
print('el anio de aparicion de Wolverine es: ',aparicion_Wolverine['anio_aparicion']) 

posDrstrange = lista_personajes.busqueda('Dr. Strange','nombre') #puntoC
if(posDrstrange != -1 ): 
    lista_personajes.obtener_elemento(posDrstrange)['casa'] = 'MARVEL'

posflash = lista_personajes.busqueda('Flash', 'nombre') #puntoG
info_flash = lista_personajes.obtener_elemento(posflash)
print('--la info de flash es--', 'casa:',info_flash['casa'],'anio de aparicion:', info_flash['anio_aparicion'])

posflash = lista_personajes.busqueda('Star-Lord', 'nombre') #puntoG
info_StarLord = lista_personajes.obtener_elemento(posflash)
print('--la info de Star-Lord es--', 'casa:',info_StarLord['casa'],'anio de aparicion:', info_flash['anio_aparicion'])

#lista_personajes.barrido_superheroe()

for i in range(lista_personajes.tamanio()):
    if (i < lista_personajes.tamanio()):
        personaje = lista_personajes.obtener_elemento(i)  

    if ('armadura' in personaje['biografia']): #puntoD
        print(personaje['nombre'], 'utiliza armadura')
    
    if ('traje' in personaje['biografia']): #puntoD
        print(personaje['nombre'], 'utiliza un traje')


    if (personaje['anio_aparicion'] <1963): #puntoE
        lista_aparicion_antesde1963.insertar(personaje['nombre'])#personaje[casa]
        lista_aparicion_antesde1963.insertar(personaje['casa'])

    if (personaje['nombre'][0] =='M'):#puntoH
        lista_A.insertar(personaje['nombre'])
    if (personaje['nombre'][0] =='B'):
        lista_B.insertar(personaje['nombre'])
    if (personaje['nombre'][0] =='S'):
        lista_S.insertar(personaje['nombre'])
    
    if (personaje['casa']== 'DC'):#puntoI
        cont_DC +=1  

    if (personaje['casa']== 'Marvel'):#puntoI
        cont_Marvel +=1   

print('los personajes que comienzan con M, S y B son ') 
lista_A.barrido()
lista_B.barrido()
lista_S.barrido()

print('la cantidad de super heroes que hay en la casa DC son: ', cont_DC)
print('la cantidad de super heroes que hay en la casa Marvel son: ', cont_Marvel) 
print(' casa y personajes con aparicion antes del 1963:') 
lista_aparicion_antesde1963.barrido() 




