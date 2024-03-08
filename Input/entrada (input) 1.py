#la funcion input sirve para obtener valores que el usuario haya ingresado a traves del teclado
nombre=input("Ingresa tu nombre completo: ")
"""
input pausa el codigo hasta que el usuario presiona enter, por eso no se termina el programa cuando ejecutamos
input va a regresar todo lo que el usuario escribio hasta presionar enter
"""
print(nombre)
#arriba, le estamos pidiendo a la consola que imprima lo que escribio el usuario
"""
La función input retorna resultados de tipo str, en las próximas líneas se va a solicitar la edad (expresada en numeros)
e igualmente cuando usemos la función type va a dar resultado str
"""
edad=input("Ingresa tu edad: ")

print(nombre + ", " + edad + " años")
print(type(edad))
"""
en la línea 16, nos va a marcar que el tipo de valor de la edad es str, lo que no está bien por que almacena un numero
lo solucionamos en las siguientes lineas con la funcion "int", que sirve para guardar los datos como int
SEGUIR EN ARCHIVO "entrada (input) 2.py"
"""

