edad=input("Ingresa tu edad: ")


while not edad.isdecimal():
    print("Edad Inválida")
    edad=input("Vuelve a ingresar tu edad:")


edadint= int(edad)
    

while edadint <= 0 or edadint > 65:
    print("Edad Inválida")
    edadint=input("Vuelve a ingresar tu edad:")

print(f"Para la jubilación faltan {65 - edadint} años.")