lista= []
nombre= "Luciano"
variable= lista or nombre

print(variable)

#esto es lo mismo que hacer lo siguiente:

"""
if lista: #es lo mismo que poner "if lista is True"
    variable=lista
else:
    variable=nombre

print(variable)
"""