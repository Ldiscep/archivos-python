#además, una funcion puede retornar multiples valores, añadiendo una coma al final del ultimo, estos pueden ser de distinto tipo. 
numero1= int(input("Primer número:"))
numero2= int(input("Segundo número:"))

def funcion(num1, num2):
    return num1 + num2, 'pesos'


#(los valores los retorna en forma de tupla, vamos a desempaquetarlo, vamos a asignarle a cada uno de los valores que retorne la función, una variable.

sumado, moneda= funcion(numero1, numero2) #le asignamos "sumado" a la suma de num1 y num2 en la linea 6, y a "moneda" el str 'pesos', para que de esta forma no salga una tupla
print("el total de los productos es de", sumado, moneda)


