a, b, c, d= 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)
#arriba se crean variables que almacenan un npumero cada una, esto se puede hacer de mejor manera con una tupla
numeros=(1, 2, 3, 4, 5)
uno, dos, tres, cuatro, cinco=numeros
#arriba, python asigna las variables automáticamente, el primer numero a la primera variable, el segundo a la segunda, etc.
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
#esto se llama desempaquetar tuplas

"""
en caso de tener mas elementos dentro de la tupla que variables para asignar, obtendremos un error,
 en ese caso se usa el *para indicarle a python que el resto de valores sin especificar se guardan en una variable, ejemplo abajo
"""
letras= ("a", "b", "c", "d", "e", "f", "g") 
primera, segunda, tercera, cuarta, *resto_de_letras = letras
print(primera)
print(segunda)
print(tercera)
print(cuarta)
print(resto_de_letras)

#para dejar valores sin incluir en una variable, se usa "*_" para indicarle a python que se usan los demás elementos hasta el *, ejemplo abajo
nombres=("luciano", "juan", "adrian", "jorge", "miguel")
nombre1, nombre2, nombre3, *_=nombres
print(nombre1)
print(nombre2)
print(nombre3)
#si no se usa eñ *_, python da un error

#para obtener elementos luego de omitir algunos se escribe así:

colores=("rojo", "verde", "azul", "gris", "negro", "rosa", "naranja", "amarillo")
color1, color2, color3, *_, color4, color5=colores

print(color1)
print(color2)
print(color3)
print(color4)
print(color5)
#arriba, se seleccionan los primeros tres colores, luego se skipean todos los demás hasta los últimos dos,  que son el número de variables que asignamos después del *_

#ejercicio:
#seleccionar elementos para descomprimir, uno si y uno no, uno si y uno no
ejercicio=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero1, _, numero2, _, numero3, _, numero4, _, numero5, _=ejercicio
print(numero1)
print(numero2)
print(numero3)
print(numero4)
print(numero5)
