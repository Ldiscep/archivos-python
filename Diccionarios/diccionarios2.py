diccionario={"a":1, "b":2, "c":3, "d":4}
#para obtener el valor de la llave "d", se define una variable
valor=diccionario["d"]
print(valor)
#para saber si un elemento se encuentra o no en un diccionario se usa "in"
print("a" in diccionario)
print("A" in diccionario)

#get se usa para obtener el valor de una llave de forma segura

valor2=diccionario.get("d")
print(valor2)

#la diferencia entre este método y el de la línea 3 es que cuando se utiliza una llave que no está en el diccionario, en vez de dar un error se otorga "none"
#además este metodo puede recibir un segundo argumento, que se retorna si el primer argumento no existe, ejemplo abajo (es como un mensaje que se muestra si el valor no existe)
valor3=diccionario.get("h", "Esta llave no se encuentra en el diccionario") #el segundo argumento puede ser CUALQUIER tipo de dato (variabl, tupla, etc.)
print(valor3)

#existe la contraparte del método get se llama "setdefault"
#lo que hace es lo mismo que get, pero si la llave no existe, se la añade con un valor especificado en el segundo argumento

valor4=diccionario.setdefault("e", 5)
print(valor4)
print(diccionario)