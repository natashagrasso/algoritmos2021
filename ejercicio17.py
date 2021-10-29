"""  Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador, 
de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:
a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la función time.sleep (segundos) – hasta que se vacíe la cola.
b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como 
máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el 
tiempo restante para terminar su ejecución–.
c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el 
quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
d. no se aplican criterios de prioridad en los procesos. """