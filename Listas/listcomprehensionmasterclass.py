lista= [num for num in range(1,11)]

#creo una funcion que recorre la lista al reves
def alreves(lista):
    return lista[::-1]

print(alreves(lista), "\n")

#creo una funcion que crea una matriz con la lista original
def matriz(lista):
    matriz=[lista for i in range(10)] #el rango es segun la cantidad de filas que queramos
    return matriz

for a in matriz(lista):
    print(a)
print("\n")
#creo una funcion que eleva al cuadrado los elementos de la lista

def cuadrado(lista):
    return [i**2 for i in lista]

print(cuadrado(lista))