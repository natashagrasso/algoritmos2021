""" Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuerto que tiene una pista, contemplando las siguientes actividades:
a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de 
origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).
b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de 
salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.
c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.
d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas después de realizar una atención.
e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –dado que son 
aviones que están sobrevolando en la zona de espera–, salvo que sea el horario de salida del 
primer avión de la cola de despegue, en ese caso se deberá atender dicho despegue.[99]
f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterrizaje –adaptados a segundo para los fines prácticos del ejercicio–:
I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde 
cuando se lo atiende para despegar (en esta caso el horario de salida será mayor que el 
último de la cola). """

from cola import Cola

class Aeropuerto (object):
    def __init__ (self, nombre_empresa, hora_salida, hora_llegada, aeropuerto_origen, aeropuerto_destino, tipo): 
        self.nombre_empresa = nombre_empresa
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.aeropuerto_origen = aeropuerto_origen
        self.aeropuerto_destino = aeropuerto_destino
        self.tipo = tipo

cola_despegue = Cola()
cola_aterrizaje= Cola()
cola_aux = Cola()

aeropuerto = Aeropuerto('LPPietroboni','12:45', '17:30','costa del Sol','aerolineas argentinas','pasajeros')
cola_despegue.arribo(aeropuerto)
aeropuerto = Aeropuerto('SARANDI','16:20', '02:40','internacional Guaraní','Avianca','pasajeros')
cola_despegue.arribo(aeropuerto)
aeropuerto = Aeropuerto('Aserradero Papi SRL','12:00','15:00','Los Llanos', 'Alas del Sur','cargas')
cola_aterrizaje.arribo(aeropuerto)
aeropuerto = Aeropuerto('NOELMA S.A.','04:40', '13:20', 'Flybondi','Jorge Newbery', 'cargas' )
cola_aterrizaje.arribo(aeropuerto)