#si queremos cuantas veces un str existe dentro de otro str, podemos usar la función "count"
nombre_completo= "Luciano Alfonso Discepolo"

contador=nombre_completo.count("o") #la función count nos va a mostrar cuantas veces sale un elemento en el string, puede ser una letra, una palabra, etc
print(contador)
#para ver si un elemento se encuentra o no dentro de un str, se usa la palabra reservada "in", ejemplo abajo
colores= "Rojo, Verde, Azul, Amarillo, Naranja, Rojo, Negro, Blanco"

print("Verde" in colores) #en este caso retorna "True"
print("VERDE" in colores) #en este caso retorna false
#distingue mayusculas y minusculas
#para pasar todo a mayúsculas y minúsculas se usa "upper" o "lower", ejemplo abajo

print("VERDE" in colores.upper()) #en este caso retorna "True"
#en este caso, estamos chequeando si "verde", existe en colores en mayúsculas

print("rojo" in colores) #en este caso retorna false por que no tiene la primer letra mayúscula

print("rojo" in colores.lower())# True


#de igual manera, se puede negar la presencia de un elemento en una variable, str, lista, etc, con el operador "not" y la palabra "in"
#ejemplo:

print("rojo" not in colores) #true, por que la palabra rojo sin mayúscula no se encuentra en colores

print("rojo" not in colores.lower()) #false, por que rojo si se encuentra en minuscula con la funcion lower

print("Rojo" not in colores) #false, por que Rojo con la primera en mayuscula, si se encuentra en colores

#para saber si un elemento se encuentra al inicio del string se usa la función "startswith", ejemplo abajo

print(colores.startswith("Rojo")) #el argumento recibe el elemento que queremos saber

print(colores.startswith("Azul"))

#mismo concepto para "endswith"

print(colores.endswith("Blanco"))
print(colores.endswith("Negro"))

