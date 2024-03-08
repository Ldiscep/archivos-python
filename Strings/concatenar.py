#los strings no pueden modificarse una vez definidos(inmutables), lo que se puede hacer, es generar nuevos strings a traves de los ya existentes
nombre="Luciano Alfonso"
apellido="Discepolo"
nombre_completo= nombre + " " + apellido
#el signo + se usa para concatenar variables, se pueden concatenar todas las que necesitemos
#si en cambio se usan comas, se genera una tupla
print(nombre_completo)
print(type(nombre_completo))

#otra manera de escribirlo, es la siguiente:

nombre2= "Juan"
apellido2= "Gomez"
nombre_completo_2= "Señor %s %s %s" %(nombre2, apellido2, "Gonzales") 
print(nombre_completo_2)# los %s van a ser reemplazados por los elementos establecidos fuera de las comillas, en su respectivo orden
print(type(nombre_completo_2))