#ordenar listas: se usa la función "sort" o algún algoritmo de orden
lista=[1, 4, 2, 7, 345, 453, 332, 543, 234, 23]
lista.sort()#ordena la lista por defecto de forma ascendente, menor a mayor
print(lista)

#para ordenarla al revés se camba el parámetro a continuación
lista.sort(reverse=True)
print(lista)

#en caso de querer conocer un número menor o mayor en la lista:
lista.sort()
print(lista[0])#<-- para imprimir el menor número, cuando la lista ya fué ordenada por la línea 11
print(lista[-1])#<-- para imprimir el mayor número
#si no, se puede usar la función "min"-"max"; a continuación un ejemplo
#print(min(lista))
#print(max(lista))

#si queremos conocer si un elemento se encuentra o no en una lista, se usa la palabra "in"
#suelta un valor True o False, dependiendo si el número está en la lista

print (10 in lista) #10 no se encuentra en la lista
print (23 in lista) #23, si

#para saber si un valor no está dentro d euna lista se usa el operador lógico "not"
print (11 not in lista)
print (23 not in lista)