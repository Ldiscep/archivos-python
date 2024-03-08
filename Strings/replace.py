#replace sirve para reemplazar o eliminar todos los elementos de un tipo de un str.

texto="hola mundo"
a=texto.replace("o","")
print(a)

#tambien funciona con números:
flotante= "8.213" #hay que escribirlo en una str para poder combinarlo con el isdecimal
entero= flotante.replace(".", "")
print(entero)