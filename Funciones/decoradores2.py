"""vamos a extender la funcionalidad de esta funcion:

def saludo():
    print('Hola')



a= funcion principal (decorador)
b=input (funcion a decorar)
c=output (funcion ya decorada)
"""


def funcion_a (funcion_b):
    
    def funcion_c():
        pass #le indica a python que por ahora no vamos a hacer nada aca
    
    return funcion_c #la funcion a va a retornar la funcion decorada (c)


@funcion_a #en la parte de arriba de la funcion se pone el nombre del decorador que queramos utilizar, de esta forma, funcion_a va a recibir como argumento la funcion saludo
def saludo(): #en este caso la funcion saludo sería la funcion b (a decorar)
    print('hola')

saludo() #si ejecutamos en este momento no pasa nada, por que no estramos ejecutando la funcion decorada, sino que la funcion que se nos retorna (c), que en este caso no hace nada. continuar en decoradores3