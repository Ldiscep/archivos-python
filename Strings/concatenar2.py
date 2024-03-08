#vamos a hacer uso del método "format"
nombre="Luciano"
seg_nombre="Alfonso"
apellido="Discepolo"

nombre_completo= "Mister {} {} {}, {}.".format(nombre, seg_nombre, apellido, "first of his name")
print(nombre_completo)
#esto funciona como el porcentaje, solo que directamente se usa el método format
#los {} son reemplazados por los valores en su respectivo orden
#se puede nombrar los {}, solo hay que poner su nombre dentro de los {}, ejemplo abajo

nombrecompleto2= "Mister {nombre} {segundo_nombre} {apellido}, {primero_de_su_nombre}.".format(
    nombre=nombre,
    segundo_nombre=seg_nombre,
    apellido=apellido,
    primero_de_su_nombre="first of his name"

)
print(nombrecompleto2)
#todo esto de arriba es un recontra re mil quilombo, mejor hacerlo como lo hice en las líneas 2 a 7, lo único bueno que trae es que las variables no se van a asignar seún el orden, sino por el nombre
