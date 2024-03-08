carrito=input("Ingresa los productos para el carrito: ")

lista=list(carrito.split())

if "Auriculares" not in lista:
    lista.append("Auriculares")
    print("¡Se agregaron unos auriculares de regalo!")
else:
    pass

print(f"Cantidad de productos en el carrito: {len(lista)}")
print(*lista, sep="\n")
