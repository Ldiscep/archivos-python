salario=float(input("Ingresa el salario: "))


if salario > 1000:
    print("Salario alto.")
elif salario in range(500, 1000):
    print("Salario medio.")
elif salario < 500:
    print("Salario bajo.")

 