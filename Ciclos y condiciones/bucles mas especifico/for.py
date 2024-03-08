#el bucle for es una instruccion que permite ejecutar un bloque de codigo par cada elemento de un objeto iterable
#un ejemplo:
#for elemento in lista:
#la traduccion seria algo como: para {tal elemento} encontrado en {tal lista}: ejecutar el siguiente código

colores=["rojo", "verde", "azul", "amarillo", "violeta"]

for x in colores: #la variable x no es necesario que este definida antes de esta linea, se crea en esta variable
    print("hola    !") #las lineas dentro de un bucle for se van a ejecutar tantas veces como elementos haya en la lista u objeto iterable, en este caso colores, que tiene 5 elementos
    print(x) #x es una variable cuyo valor va cambiando en cada una de las ejecuciones(iteraciones) del bloque, va a ir recibiendo cada uno de los elementos del objeto iterable, en su respectivo orden

#cuando termina el ciclo, x se queda con el ultimo valor iterable, violeta en este caso
print(x)


