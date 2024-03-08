#se utiliza la palabra if para condicionar bloques de codigo

resultado = 30
cuenta = resultado > 10

verdadero = "{} es mayor que 10".format(resultado)
falso = "{} es menor que 10".format(resultado)

if cuenta : #esto es lo mismo que poner "if cuenta is true"
    print (verdadero)
else:
    print(falso)


#tambien se pueden usar operadores lógicos como "and" "or"
#continua en Condiciones 2

