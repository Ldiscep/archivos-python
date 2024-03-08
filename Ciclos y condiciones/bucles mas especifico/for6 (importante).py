#vamos a validar la lista con respecto al código de for5.py


from statistics import mean
#en este caso lavariable notas_str va a tener varios numeros(correctos) y una letra(incorrecto), es por eso que hay que hacer la validación antes de la linea que convierte todo eso a una lista de enteros

notas_str= input("Ingresa la lista de notas:")

#el metodo isdecimal solo se puede aplicar sobre cadenas
lista_notas=notas_str.split()

for nota in lista_notas: #vamos a aplicar un isdecimal a cada uno de los elementos de la lista creada en linea 10
    if not nota.isdecimal(): #si "nota" no es un numero en forma de str: /// si la variable no es un número decimal:
        print(f"El dato '{nota}' no es un número entero")
        exit()

notasint= list(map(int, lista_notas))

for nota in notasint:
    if nota < 1 or nota >10:
        print(f"La nota '{nota}' no está entre 1 y 10")
        exit()


print(f"El promedio es: {mean(notasint)}")