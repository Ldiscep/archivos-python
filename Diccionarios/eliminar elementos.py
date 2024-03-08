diccionario={"a":1, "b":2, "c":3, "d":4}
print(diccionario)
print(len(diccionario))

# primera forma de eliminar un elemento usando su llave:

del diccionario["a"]
print(diccionario)
print(len(diccionario))



#segunda forma de eliminar un elemento es con el método "pop"

valor=diccionario.pop("b")
print(valor)
#retorna el valor del elemento que se extrajo


print(diccionario) #ahora el diccionariono tiene la llave "a", extraida en la linea 7 ni la llave "b", extraída en la línea 15
print(len(diccionario))
#si quisieramos elminiar todos los elementos del diccionario se usa el elemento "clear"

diccionario.clear()
print(diccionario)
print(len(diccionario))