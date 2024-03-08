#si quisieramos modificar el valor d euna variable global dentro de un bloque, ya sea una función u otro, se usa "global"

nombre="luciano"

def funcion():
    global nombre #con "global le indicamos a python que vamos a usar la variable global con ese nombre"
    
    nombre="alfonso" #la variable ahora pasa a llamarse "alfonso" (en todo el código), pero el id de la variable es el mismo
    apellido="discepolo"
    
    print(id(nombre))
    print(nombre)
    print(apellido)

funcion()

print(id(nombre))