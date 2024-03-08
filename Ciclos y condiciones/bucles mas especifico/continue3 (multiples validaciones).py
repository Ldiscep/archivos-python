edad_valida= False

while not edad_valida:
    edad_str=input("Ingresa tu edad: ")
    if not edad_str.isdecimal():
        print("La edad ingresada debe ser un número.")
        continue 
        #este continue va para que el interprete vuelva al inicio del bucle y vuelva a preguntar con el input de linea 4, si el input no estuviera, intentaria convertir la edad a int y tiraria un error
    edad= int(edad_str)

    if edad <= 0:
        print("La edad debe ser mayor a cero")
        continue  #este continue va para que el interprete vuelva al inicio del bucle y vuelva a preguntar con el input de linea 4
    edad_valida=True #cambiar el true es necesario por que siempre que un bloque while llega a la última línea vuelve a chequear la condicion de ingreso de la primera. Si no lo cambiaramos, seguiría ingresando

#bueno en este caso el codigo funciona de la siguiente manera: primero se determina que edad_valida es falso. Esto es para que el interprete entre al while. 
#primero pregunta la edad, en vez de hacerlo afuera del while. Si la edad no es decimal se imprime el mensaje de la linea 6 y se vuelve al principio del while, donde vuelve a preguntar la edad con el mismo input.
#si el bucle pasa de ahi, significa que la edad es un numero (decimal), por lo que en linea 9 se lo convierte a int
#despues, verifica si la edad es mayor que 0, de lo contrario imprime el mensaje y te manda devuelta al principio del bucle, donde te vuelve a preguntar la edad. si la edad es mayor que 0, edad_valida pasa a ser true.

print(f"Para la jubilación te faltan {65 - edad} años")
