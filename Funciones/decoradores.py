"""
un decorador es una funcion que toma como input una funcion y su output es otra función :)?????
con estos se puede hacer el codigo mas legible y facil de testear, reduciendo lineas de codigo

se trabajan con por lo menos tres funciones:

a= funcion principal (decorador)
b=input (funcion a decorar)
c=output (funcion ya decorada)

a(b) -> c
"""

def funcion_a (funcion_b):
    def funcion_c():
        pass
    
    return funcion_c

#vamos a extender la funcionalidad de la siguiente función en decoradores 2:

def saludo():
    print('hola')
