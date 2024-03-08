#las tuplas permiten almacenar todo tipo de datos, hasta otras tuplas
#la diferencia entre listas y tuplas es que las tuplas son inmutables, esto significa que una vez definida, no se pueden modificar los elementos almacenados
tupla=("hola", 10, 2.23, True, [1, 2, 3], (4, 5, 6))
#esta tupla contiene un string, un entero, un flotante, Un booleano, una lista y otra tupla
print(tupla)
print(type(tupla))
#la tupla sirve principalmente para consultar valores, ya que no se puede añadir ni quitar elementos
#la principal ventaja en cuanto a las listas es que las tuplas son mucho más rápidas en cuanto a obtener elementos
nombres=("pepe", "jorge", "daniel", "manuel", "luciano")
#           0       1         2         3         4
primer_nombre=nombres[0]
print(primer_nombre)
ultimo_nombre=nombres[-1]
print(ultimo_nombre)
#para crear una subtupla:
sub_tupla=nombres[0:3] #el indice final no se incluye al generar la subtupla
print(sub_tupla)
