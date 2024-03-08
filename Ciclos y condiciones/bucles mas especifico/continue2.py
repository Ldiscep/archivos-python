#el siguiente código tiene un error, que es que si una vez dentro del segundo bloque while, ingreso un numero no decimal, me va a dar un error.
#Esto se da por que dentro de ese bucle no tengo una validación isdecimal.


edad=input("Ingresa tu edad: ")


while not edad.isdecimal():
    print("Edad Inválida")
    edad=input("Vuelve a ingresar tu edad:")


edadint= int(edad)
    

while edadint <= 0 or edadint > 65:
    print("Edad Inválida")
    edadint=input("Vuelve a ingresar tu edad:")

print(f"Para la jubilación faltan {65 - edadint} años.")

"""
una forma de solucionarlo es poniendo el primer bucle while, duplicado adentro del segundo, de modo que quedaría así:

while edadint <= 0 or edadint > 65:
    print("Edad Inválida")
    edadint=input("Vuelve a ingresar tu edad:")
    
    while not edad.isdecimal():
    print("Edad Inválida")
    edad=input("Vuelve a ingresar tu edad:")


Esto es una forma de resolverlo, pero en el proximo archivo vamos a ver como resolverlo de manera mas elegante con un continue.
"""