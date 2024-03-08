#para poder solucionar el problema de que no retorne el resultadom hay que guardar la cuncion a decorar de la linea 7 en una variable, y retornar esa variable

def decorador (funcion_a_decorar):
    
    def funcion_decorada(*args, **kwargs): #si aca no ponemos args y kwargs, nos va a dar un error, ya que le estamos dando dos valores en la linea 13, pero no estaria teniendo donde almacenarlos
        print('el resultado es: ')
        var_suma=funcion_a_decorar(*args, **kwargs) #funcion_a_decorar=suma
        return var_suma
    return funcion_decorada


@decorador
def suma (num1, num2):
    return num1 + num2

#si ahora llamaramos a la funcion de la siguiente manera: suma(10, 20), el resultado sería "el resultado es:" sin ningun resultado de suma, esto es por que en ningun momento se imprime lo que retorna la suma
#hay que llamarla de la siguiente manera

resultado=suma(10,20)
print(resultado)

"""
Megacomentario explicador:

primero, se define la funcion decorador, que es una funcion que sirve para expandir la funcionalidad de la funcion suma de la linea 13.
dentro de la funcion decorador (a, a partir de ahora) se definen dos acciones, la funcion decorada (c, a partir de ahora) y el return del valor de la funcion c, en la linea 9

la funcion decorada tiene como argumento args y kwargs para almacenar cualquier cantidad de elementos de varios tipos (en tuplas o diccionarios, segun corresponda. en este caso usamos tuplas)

Me faltó aclarar que la funcion a decorar es el argumento de la funcion a, por lo que es lo mismo que suma, para eso sirve el arroba de la linea 12, para indicar que suma va a ser funcion_a_decorar. Osea el argumento de la funcion a

Como los valores dados en la linea 19 son numeros singulares, se guardan en forma de args (tupla) 

Desde linea 6 hasta 9, son lineas dentro de la funcion decorada (c)

la linea 7 es la funcion b (suma o funcion a decorar) puesta en marcha con los args o kwargs asignados en linea 19



"""