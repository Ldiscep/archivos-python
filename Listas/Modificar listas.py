lista_nombres=["luciano", "manuel", "juan", "martin", "pepe"]

#para añadir elementos al final:
lista_nombres.append("diego")

#para conocer la longitud:
print(len(lista_nombres))


#prueba de combinar ambas cosas:
lista=["a", "b", "c", "d"]
print(lista)
print(len(lista))

lista.append("e")
print(lista)
print(len(lista))

"""
se pueden añadir cualquier tipo de dato, 
pero se intenta almacenar en una lista tipos
de dato iguales
"""
#para añadir elementos a la lista con un número de índice se usa "insert"
lista_nombres.insert(1, "Pedro")#  <-- elemento a añadir
#                    ^numero de indice en el que se añade el elemento
#acá se añade el elemento "pedro" a la lista de nombres, se añade en el número de índice 1
lista_nombres.insert(0, "Matias")
"""
si yo fuera a imprimir la lista ahora, "pedro" se mostraría en el índice 2, 
por que estaba en el índice 1
y al agregar "matías", se hacen para la derecha
"""
print(lista_nombres)
print(len(lista_nombres))

#para agregar elementos de una lista a otra se usa la función "extend"
#la segunda lista no se elimina ni modifica
lista1=[1, 2, 3, 4, 5]
print(lista1)
print(len(lista1))
lista2=[6, 7, 8, 9, 10]

lista1.extend(lista2)
print(lista1)
print(len(lista1))

#para eliminar elementos de la lista se usa la función "remove"

lista_nombres.remove("luciano")

print(lista_nombres)
print(len(lista_nombres))
#para eliminar elementos de la lista usando su número de índice se usa la palabra reservada "del"

del lista_nombres[3]#<-- en este caso sería "juan"
#                 ^ hace referencia al número de índice del elemento a borrar
print(lista_nombres)
print(len(lista_nombres))
#para eliminar todos los elementos almacenados de una lista se usa la función "clear"

lista_nombres.clear()
print(lista_nombres)
print(len(lista_nombres))