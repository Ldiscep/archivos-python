diccionario={"a":1, "b":2, "c":3, "d": 4}


#en momentos vamos a necesitar conocer que llaves, valores o elementos tenemos en un diccionario con los siguientes métodos:

"""
keys
values
items
"""

llaves=diccionario.keys()
print(llaves)


#el objeto emitido por la variable "llaves se puede convertir en una tupla"


#método1
tuplallaves=tuple(diccionario.keys())
print(tuplallaves)

#método2:
llaves=tuple(llaves)
print(llaves)

#          |---- los valores los almacenamos en una tupla
#          v
valores=tuple(diccionario.values())
print(valores)

elementos=tuple(diccionario.items()) #elementos son la llave y su valor
print(elementos)

