from random import randint


clave= randint(0,9999)
numero= randint(0, 9999)

while numero != clave:
    numero= randint(0, 9999)
    print(numero)
else:
    print(f"la clave era: {clave}")
