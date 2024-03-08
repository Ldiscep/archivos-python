#una libreria es un conjunto de herramientas que vienen con el lenguaje que traen instrucciones que podemos utilizar en nuestro programa
#importar una instruccion significa señalarle a python que en algun momento del archivo  vamos a usar la libreria

#se usan las palabras From e import
#from {nombre del módulo} import {instrucción}

from statistics import mean

#mean sirve para sacar el promedio de una lista

lista=[1, 4, 10, 23]
promedio=mean(lista)
print(promedio)

#docs.python.org para ver todos los módulos, dentro de la documentación