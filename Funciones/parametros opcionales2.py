#como pi es un valor constante, lo vamos a definir en los primeros parámetros de la función utilizando el = sin espacios

def area(radio, pi=3.14): #IMPORTANTE: los parametros con valores por default, como pi en este caso, siempre se ponen de derecha a izquierda
    return pi * (radio**2) 

resultado=area(10) #por lo tanto, aca no hace falta poner dos parámetros, solo uno (radio), ya que pi se encuentra definido
# SI se puede agregar otro parámetro y que en esta call reemplaze el que se encuentra predefinido en linea 3

print(resultado)

#parametros obligatorios son los que se usan si o si al llamar una funcion
#parametros opcionales son a los que se les define el valor al redactar la función, aunque este despues pueda ser reemplazado por obligatorios