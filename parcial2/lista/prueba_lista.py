from random import randint 
from lista import Lista

lista_personas = Lista()
lista_num = Lista()

datos = [
        {'nombre: juan ','edad: 43', 'provincia: entre rios', 'dni: 43348688'},
        {'nombre: luis ','edad: 32', 'provincia:misiones',  'dni: 45666978'},
        {'nombre: rita ','edad:28', 'provincia: entre rios', 'dni: 21359832'},
        {'nombre: pablo ','edad:40', 'provincia: formosa',  'dni: 11068397'},
]

for persona in datos:
    lista_personas.insertar(persona,'nombre')
lista_personas.barrido()    

print(lista_personas('juan', 'nombre'))

for i in range(0,10):
    lista_num.insertar(randint(0,100)) 

lista_personas.barrido()

lista_num.barrido()

