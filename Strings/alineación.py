#los strings se pueden alinear/justificar  utilizando métodos
mensaje="hola mundo"

print(mensaje)

"""
Los tres métodos que existen son:

ljust--> justifica a la izquierda
rjust--> justifica a la derecha
center--> justifica al centro

"""
#ejemplos:

mensaje=mensaje.ljust(20)#<-- el parámetro es un número entero que muestra la cantidad de espacios que se va a mover
print(mensaje, ".")

mensaje2=("hola mundo")

mensaje2=mensaje2.rjust(20)
print(mensaje2)

#visto así no tiene mucho sentido, pero hay que pensar que ljust lo mueve () espacios hacia la derecha, mientras que rjust lo mueve () espacios hacia la izquierda

#el método center añade la mitad de los espacios puestos en el parámetro a la derecha y la otra mitad a la izquierda, ejemplo abajo:
 
mensaje3="hola mundo"
mensaje3=mensaje3.center(50)
print(mensaje3)
#añadió 25 espacios a la izquierda y 25 a la derecha


