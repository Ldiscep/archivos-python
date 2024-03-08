lista=[1, 4, 2, 7, 345, 453, 332, 543, 234, 23]

print(4 in lista)# confirmamos que el elemento "4" esté en la lista

indice=lista.index(4) # definimos la variable "índice" como el número de índice del elemento "4" en la lista
print(indice)

#si en una lista existiese un elemento, varias veces, la función index va a retornar el número de índice de la primera vez que aparece el elemento en la lista
#ejemplo:
lista2=[2, 4, 7, 4, 2, 4, 78, 123, 1243]
indice2=lista2.index(2)
print(indice2)