#vamos a usar 'Docstring' para documentar funciones:
#un docstring es un comentario que se coloca en la primera linea de codigo de la función, sirve para describirla
#se le puede agregar un 'to-do list'
def suma(num1, num2):
    """
    La función suma los dos valores provistos

    Argumentos: 
    num1 (int)
    num2 (int)

    se retorna la suma de los parámetros
    TODO: 
    *
    """
    return num1 + num2



"""
Objetos documentables:
-módulos
-clases
-métodos
-funciones

"""
#para ver la documentacion de una función se usa el método __doc__ (dos guiones de cada lado)
print(suma.__doc__)

#tambien se puede usar la función 'help', obteniendo el mismo resultado
print(help(suma))