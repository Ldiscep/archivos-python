#para combinar valores de una tupla y una lista, se utiliza la función zip, ejemplo abajo
lista=[1,2,3,4,5]

tupla=(10,20,30,40,50)

mezcla=zip(lista, tupla) #-->  por si sola esta función genera un tipo de dato zip con un número raro
mezcla=tuple(mezcla)#--> ahora, convertimos ese dato en una tupla
print(mezcla)
#esta tupla almacena subtuplas, las cuales están conformadas por los elementos de las anteriores
#si quisiera hacer tuplas de tres o mas valores, solo hace falta añadir una lista o una tupla

#de a cientos
lista2=[100,200,300,400,500]
mezcla=zip(lista, tupla, lista2)
mezcla=tuple(mezcla)
print(mezcla)

#de a miles
tupla2=(1000,2000,3000,4000,5000)
mezcla=zip(lista, tupla, lista2, tupla2)
mezcla=tuple(mezcla)
print(mezcla)

#se puede hacer una lista de tuplas, en vez de la función tuple se usa la función list
mezcla=list(mezcla)
print(mezcla)
#acá obtenemos una lista de tuplas, igualmente es mas recomendable usar tuplas con subtuplas, como arriba

#si tuviera una lista/tupla con mas elementos que las demás, estos elementos de más no serían tomados en cuenta para formar la tupla, ejemplo abajo
numeros=(1,2,3,4,5,6,7,8,9,10)
numeros2=(10,20,30,40,50)
mezcladenum=zip(numeros, numeros2)
mezcladenum=tuple(mezcladenum)
print(mezcladenum)
#vemos como se genera hasta la subtupla (5, 50)