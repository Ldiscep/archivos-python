#vamos a hacer  un input  que sirva  para ejecutar un codigo la cantidad de veces que quiera un usuario, con la funcion range
veces=int(input("Cuantas notas desea ingresar: "))
notas=[]

for  x in range(veces): #aca creamos un range desde el 0 hasta el valor de la variable veces
    nota=(input("Ingresa la nota: "))
    
    notas.append(nota)
    for l in notas:
        if not l.isdecimal():
            print(f"La nota '{l}' no es válida")
            exit()
from statistics import mean


notas=list(map(float,notas))

print(f"Promedio: {mean(notas)}")
    