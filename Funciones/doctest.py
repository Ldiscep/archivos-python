
#se puede testear el funcionamiento de las funciones con __doc__

def suma(num1, num2):
    """
    La función suma los dos valores provistos

    Argumentos: 
    num1 (int)
    num2 (int)

    se retorna la suma de los parámetros


    >>> suma(10, 20)
    30

    >>> suma(100, 1000)
    1100
    """
    return num1 + num2

#explicación: en la linea 15 y 16 simulamos estar en consola, en la linea 15 se simula la ejecución de la función en consola, esto para chquear que funcione como debe
#              en la línea 16, se da el resultado esperado

#se pueden hacer todas las pruebas que queramos
# se ejecuta la prueba poniendo en consola: python -m doctest doctest.py
#                                                               ^nombre del archivo
#si la consola no retorna nada es que no hay error, sino te da error