modalidad=float(input("Elija su modalidad:\n -Suma: 1 \n -Resta: 2 \n -Multiplicación: 3 \n -División: 4\n"))

def suma():
    num1= float(input("Ingrese el primer número: "))
    num2= float(input("Ingrese el segundo número: "))
    resultado= num1 + num2 
    devolución= "el resultado es {}".format(resultado)
    print(devolución)

def resta():
    num1= float(input("Ingrese el primer número: "))
    num2= float(input("Ingrese el segundo número: "))
    resultado= num1 - num2 
    devolución= "el resultado es {}".format(resultado)
    print(devolución)

def multiplicacion():
    num1= float(input("Ingrese el primer número: "))
    num2= float(input("Ingrese el segundo número: "))
    resultado= num1 * num2 
    devolución= "el resultado es {}".format(resultado)
    print(devolución)

def division():
    num1= float(input("Ingrese el primer número: "))
    num2= float(input("Ingrese el segundo número: "))
    resultado= num1 / num2 
    devolución= "el resultado es {}".format(resultado)
    print(devolución)

if modalidad == 1:
    suma()
elif modalidad == 2:
    resta()
elif modalidad == 3:
    multiplicacion()
elif modalidad == 4:
    division()
else:
    print("Ingrese un número correcto")