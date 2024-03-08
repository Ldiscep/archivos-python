#hay casos en los que las funciones deban retornar valores, ya sea para almacenarlos, o otras cosas. se usa la palabra reservada "return"
def suma(num1, num2):
    resultado= num1 + num2
    return resultado

numero1= int(input("Ingresa el primer número: "))
numero2= int(input("Ingresa el segundo número: "))


#para almacenar el valor que retorne la funcion se lo guarda en una variable

resultado= suma(numero1,numero2)
print(resultado)

"""
Tambien se puede hacer la misma funcion con menos lineas de código, poniendo directamente return num1 + num2:


def suma(num1, num2):
    return num1 + num2
"""



