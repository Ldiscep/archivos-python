#el operador logico "or" asigna a la variable el primer valor verdadero con el que se encuentre
#ejemplo:
variable= "Luciano" or "Luciana"
#todos los strings que no estén vacions, python los considera verdaderos, por eso "luciano" es verdadero

print(variable)

nombre= "" or "Pepa" # los valores vacios son falsos, por eso marca "pepa"
print(nombre)

#otro ejemplo:
var2= "" or [] or 0 or True
print(var2)