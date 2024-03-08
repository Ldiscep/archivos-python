#while

edad=int(input("Ingresa tu edad: "))

while edad <= 0:
    print("La edad debe ser mayor a 0")
    edad=int(input("Vuelve a ingresar tu edad: "))

print(f"Te faltan {65  - edad} años para ña jubilación.")