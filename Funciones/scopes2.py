#para poder identificar una variable local de una global, vamos a usar su numero único de id

animal='Perro' 

def imprimir_animal():

    animal='Ballena' 
    print(animal) 
    print(id(animal))


imprimir_animal()

print(animal)
print(id(animal))

