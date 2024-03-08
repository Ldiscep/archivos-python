def funcion_a (funcion_b):
    
    def funcion_c():
        print('Este es el resultado de la función C')
    
    return funcion_c #la funcion a va a retornar la funcion decorada (c)


@funcion_a #en la parte de arriba de la funcion se pone el nombre del decorador que queramos utilizar, de esta forma, funcion_a va a recibir como argumento la funcion saludo
def saludo(): #en este caso la funcion saludo sería la funcion b (a decorar)
    print('hola')

saludo() #lo que hicimos aca fue cambiar o expandir la funcionalidad de la funcion saludo (B) por la de la funcion_c (C), que es la nueva funcion, que generalmente va a cumplir mejores funciones


#lo que vamos a hacer a continuacion va a ser llamar a la funcion a decorar (B) dentro de la decorada (C)

"""
A partir de ahora:

A=1
B=2
C=3
"""
def funcion_1(funcion_2):

    def funcion_3():
        funcion_2() #aca llamamos a la funcion en vez de imprimirla por que sino nos da cualquier cosa
        print('Hola, estamos expandiendo la funcionalidad de la funcion2 ')
    return funcion_3 #hacemos que la funcion1 retorne la funcion 3, osea la 2 pero modificada


@funcion_1
def nombre():
    print('Mi nombre es luciano')

nombre()

#voy a hacer un ejemplo que se entienda mas en el proximo archivo
