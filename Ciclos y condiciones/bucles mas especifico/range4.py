#si usamos la instruccion range con un solo numero en los paréntesis, python genera un rango de numeros desde el cero hasta ese número (no incluído)

#print(list(range(10)))
veces=int(input("Cuantas veces saluda?: "))
for n in range(veces):
    print("Hola")
