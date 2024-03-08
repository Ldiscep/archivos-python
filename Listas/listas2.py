#                  -4        -3        -2        -1
#                   0         1         2         3
lista_nombres=["luciano", "martin", "nicolas", "Juan"]

primer_nombre=lista_nombres[0]
print(primer_nombre)
"""
con las dos lineas de arriba 
le asignamos un valor de la lista a la variable, 
eligiendo su número de índice
"""
segundo_nombre=lista_nombres[1]
print(segundo_nombre)

"""
a continuación, 
se ve como se puede imprimir el tercer nombre del índice,
sin asignarle una variable
"""
print(lista_nombres[2])

"""
Para leer la lista de derecha a izquierda se pueden usar 
números negativos, por ejemplo el -1 
para leer el que normalmente sería el último valor de la lista
Ver líneas 1 y 2
"""
ultimo_nombre=lista_nombres[-1]
print(ultimo_nombre)
"""
Para reemplazar o actualizar 
un elemento dentro de la lista,
hay que hacerlo con los índices
ejemplo abajo
"""
lista_nombres[3] = "Manuel"
    #aca, se usa el número de indice del elemento para indicar cual se quiere cambiar
print(lista_nombres[3])
