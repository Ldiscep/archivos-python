#que las funciones sean ciudadanos de primer orden significa que pueden ser asignadas a variables, pueden ser utilizadas como argumentos o hasta pueden retornar otras funciones
#vamos a definir una funcion que sirva para pasar grados centígrados a grados fahren

def conversion (grados): 
    return 'son {} grados fahrenheit'.format (grados * 1.8 + 32) 
    

print(conversion(123))

#vamos a guardar la función en una variable

mi_funcion= conversion #no va parentesis por que sino python va a pensar que la estamos llamando
print(type(mi_funcion))

#ahora se puede llamar la funcion a traves de la variable

print(mi_funcion(202)) #el 202 es el argumento que iria entre los parentesis de la función original
