#para pasar diferentes valores cuando llamamos a una función, se puede usar **, la diferencia con * es que estaremos trabajando con diccionarios en vez de tuplas 
#los parámetros con ** se llaman kwargs

#vamos a hacer una funcion que almacene las notas de dos alumnos
def usuarios (**kwargs): #el doble asterisco lo convierte en diccionario
    print(kwargs)
    print(type(kwargs))

usuarios(Luciano=[10, 7, 8, 5], Manuel=[7, 8, 9, 9]) #las llaves serían "luciano" y "manuel" y las llaves serían las listas con las notas que se les asignaron

#para resumir: * = tupla(args)
#              **= diccionario(kwargs)

#vamos a definir una función con args y kwargs:

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion('a','b','c',1,2,3, Llave1=True, Llave2="no tan True")