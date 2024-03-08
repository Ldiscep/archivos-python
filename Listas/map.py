#map() sirve para aplicar una instruccion a cada elemento de una lista, tupla, etc. como vamos a hacer ahora con el int



notas_str= input("Ingresa la lista de notas: ")
notas=list(map(int,notas_str.split())) #no hacemos que la lista se convierta en int, si no que cada elemento de esta se convierta en un int

if 10 in notas:
    print("¡Hay al menos una nota excelente!")
else:
    print("No hay ninguna nota excelente.")

print(notas)