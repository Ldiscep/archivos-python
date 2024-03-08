#vamos a ver como se comportan las variables dentro y fuera de las funciones

animal='Perro' #variable global: función, condición, ciclo

def imprimir_animal():

    animal='Ballena' #variable local
    print(animal) #si elimino esta variable, se usará la variable global con ese nombre

imprimir_animal()

print(animal)

#animal de la linea 3 y animal de la línea 7 son variables distintas, una es global y la otra está dentro de la función (local)
#para poder distinguir las variables que tienen un mismo nombre entre sí, se puede sacar su id, ver en scopes2.py