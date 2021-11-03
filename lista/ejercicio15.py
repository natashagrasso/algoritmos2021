# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;[115]
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos;

from lista import Lista

class Entrenadores (object):
    def __init__ (self, nombre,torneos_ganados, batallas_perdidas, batallas_ganadas, especie, torneos_ganados, episodios_queaparecio ): 
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.especie = especie
        self.torneos_ganados = torneos_ganados
        self.episodios_queaparecio = episodios_queaparecio
        

lista_personajes_sw = Lista()
lista_aux = Lista()
lista_aux2 = Lista()


personajes_sw = [
    {'nombre':'Leia','altura':'0,60', 'edad':'19','genero':'F', 'especie': 'humana', 'planeta_natal': 'Alderaan', 'episodios_queaparecio':'V'},
    {'nombre':'Darth Vader','altura':'2,16', 'edad':'854','genero':'M', 'especie': 'Droide', 'planeta_natal': ' forestal,', 'episodios_queaparecio':'IV'},
    {'nombre':'Han solo','altura':'2,03', 'edad':'900','genero':'M', 'especie': 'humana', 'planeta_natal': 'Alderaan', 'episodios_queaparecio':'VII'},
    {'nombre':'Chewbacca','altura':'0,40', 'edad':'200 ','genero':'F', 'especie': 'Droide', 'planeta_natal': ' forestal,', 'episodios_queaparecio':'VI'},
    {'nombre':'Phasma','altura':'4,01', 'edad':'890 ','genero':'F', 'especie': 'humana', 'planeta_natal': 'pantanoso', 'episodios_queaparecio':'IV'},
]