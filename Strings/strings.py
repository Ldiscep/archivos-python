#para crear una lista desde este solo string, se usa el método "split"

nombres= "luciano daniel santiago juan manuel tomas"

listado_nombres=nombres.split()
print(listado_nombres)
#con esto se ha generado una lista con los nombres del str, utilizando espacios, cada espacio denota un nuevo elemento en la lista
#si quisieramos dividir el str según otro caracter, este se pone en los parámetros de la función split, ejemplo abajo
colores=("rojo-verde-azul-amarillo-blanco-gris-naranja")
lista_colores=colores.split("-")#<-- acá le muestro que quiero dividir el str con guiones, se usan las comillas por que este parámetro solo acepta str
print(lista_colores)
#otro ejemplo, pero en este caso, solo queremos dividir el str dos veces, para esto se inserta un segundo valor en los parámetros, un int
numeros="1//2//3//4//5//6//7"
lista_numeros=numeros.split("//", 2)
print(lista_numeros)#<-- aca vemos que se generan tres elementos, es como si agarrara una espada y cortara dos veces el str, quedan tres pedazos
#igual, regularmente no se usa el segundo argumento


#el método "join" sirve para crear un/os string/s a partir de una lista, es lo opuesto a split, literalmente

lista_nombres= ["luciano", "daniel", "santiago", "juan", "manuel", "tomas"]
string_nombres=" ".join(lista_nombres)
            #   las comillas definen que se va a usar entre los nombres, ahora tienen un espacio, la fórmula es parecida a la de split, pero al revés
print(string_nombres)
print(type(string_nombres))



