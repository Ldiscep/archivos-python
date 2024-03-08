lista=["luciano", "manuel", "juan", "pedro", "Martin"]
#           0         1       2         3        4
sublista=lista[0:3]
"""
En la variable "sublista", se muestra como se crea una 
sublista a partir de la lista creada en la primera línea.
se incluyen desde el elemento 0, hasta el 2 
(el tres no se incluye, si no sería [0:4]), 
el indice final no se toma en cuenta
"""
print(sublista)


#en el caso siguiente se muestra que pasa cuando se crea una sublista con más índices de los que hay
sublista2=lista[0:1000]
print(sublista2)


#para obtener todos los elementos a partir de un índice, se escribe así
sublista3=lista[1:]
print(sublista3)
#se imprimen todos los elementos desde el índice 1

#para crear una sublista de elementos con saltos entre ellos se escribe así:
lista_saltos=["a", "b", "c", "d", "e", "f", "g"]
sublista_saltos=lista_saltos[0:7:2]
# 0 en este caso es el start, 7 el end y 2 saltos de cuantos items se realizan
print(sublista_saltos)


#resumen:
"""
[start:end]
[start:]--> obtenemos los elementos desde start hasta el final
[:end]--> obtenemos los elementos de la lista desde el principio hasta end
[start:end:skip]

"""