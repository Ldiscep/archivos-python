edad_str = input("Edad: ")

if not edad_str.isdecimal():  #isdecimal sirve para saber si un str es un numero entero, un numero que se pueda convertir en tipo de dato int. Lo escrito en esta línea significa que si lo puesto en el input no es un valor convertible a int, imprimir lo de la línea 4
    print("solo se permiten números")   #isdecimal retorna un Bool
    exit()

edad_int= int(edad_str)
años_restantes= 65 - edad_int

print(años_restantes, "años para la jubilacion")

