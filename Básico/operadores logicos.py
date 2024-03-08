#Los operadores lógicos permiten comparar valores booleanos, son los siguientes:

#and
"""
permite comparar valores booleanos
todas las operaciones deben ser verdaderas para que arroje un valor verdadero
si una de ellas es falsa , el valor será falso
"""
resultado_final= True and True #se pueden comparar la cantidad de valores que queramos (True and True and True, etc.)
resultado_final2= True and False #este resultado va a arrojar un resultado falso
print(resultado_final)
print(resultado_final2)
"""
tambien pueden compararse valores numéricos, ejemplo abajo
"""
resultado_final3= True and 10>20 #va a arrojar falso, por que 10 no es mayor a 20
print(resultado_final3)

#or
"""
por lo menos una de las comparaciones debe ser verdadera
para que el resultado final sea verdadero
"""
resultado_final4= True or False
resultado_final5= False or False
resultado_final6= False or 30<300
"""
usando parentesis se pueden combinar los operadores lógicos
ejemplo abajo
"""
resultado_combinado= True and ( False or 40 < 20)
                    #True and False 
                    #(python resuelve primero el paréntesis)
                    #Como hay un valor false, el resultado será False
print(resultado_final4)
print(resultado_final5)
print(resultado_final6)
print(resultado_combinado)

#not
"""
permite negar un valor booleano
convierte True a False y viceversa
"""
resultado_final7= not True 
resultado_final8= not False
print(resultado_final7)
print(resultado_final8)