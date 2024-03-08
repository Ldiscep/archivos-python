#vamos a hacer un lazy iterator que nos de cada uno de sus objetos cuando lo vamos necesitando
#usaremos la funcion 'next'

def pares():
    for numero_par in range(0,10,2):
        yield numero_par

        print('ejecución reanudada')

generador = pares()
print(next(generador))
    #de esta manera obtenemos los elementos on demand, con cada llamado nos da una iteración, y con 'next' nos da la próxima
    #esto es por si no los necesitamos todos de una sola vez

"""
si nos excedemos llamados al generador y se queda sin numeros par dar (linea 5, max 10 por ejemplo) vamos a obtener el error stopiteration, esto se puede manejar con:
'try' y 'except'
ejemplo abajo:
"""

                                             #transcripción:
while True:                                 #mientras no hayan errores
    try:                                    #intentar
        siguiente_numero= next(generador)   #llamar a la siguiente iteración del generador
        print(siguiente_numero)
    except StopIteration:                   #si se encuentra con el error 'StopIteration'
        print('El generador finalizó')      # imprimir en pantalla: 'El generador Finalizó'
        break                               #terminar el ciclo