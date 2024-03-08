#los diccionarios sirven para almacenar cualquier tipo de datos, hasta otros diccionarios
# no se rigen por índices, sino por llaves
#son mutables, como las listas
#todos los elementos en un diccionario pueden ser modificados


#como se define un diccionario?

diccionario={}

#alternativamente, se puede usar diccionario= dict()



#para añadir elementos:
elementos={}
elementos[ "nombre" ] = "Luciano"

#entre los corchetes van las llaves que queramos añadir, son objetos inmutables
print(elementos)

#en este caso, el elemento es {"nombre":"Luciano"}
#                                  A        A
#                                  |        |-- siendo "Luciano" el valor
#                                  |
#                                  |-- siendo "nombre" la llave


#para conocer la longitud de un diccionario se usa "len", como en las listas y tuplas
#ejemplo:

print(len(elementos))

#vamos a agregar una llave de tipo tupla
elementos[(1, 2, 3, 4, 5)]= "la llave es una tupla, este es el valor de esa llave"

print(elementos)

#para actualizar el valor de una llave simplemente se reescribe, por ejemplo, ahora voy a cambiar el valor de la llave "nombre"

elementos["nombre"]="Luciano Alfonso"

#si en un diccionario se repiten llaves, como muestro a continuación, se guarda el último valor definido para la llave, NO SE PERMITEN LAS LLAVES DUPLICADAS

diccionario2={"a": 1, "b":2, "c":3, "a":4}
print(diccionario2)
#el diccionario solo contiene tres elementos:
print(len(diccionario2))
print(elementos)
