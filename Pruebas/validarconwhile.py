nombres_productos = ["Teclado", "Mouse", "Auriculares", "Impresora"]
precios_productos = [20, 10, 30, 100]

# Solicitar el nombre de un producto e imprimir su precio.

producto=input("Ingresa el nombre de un producto: ")

while not producto.isalpha():
    print("El producto ingresado no es válido")
    producto=input("Ingrese un nuevo producto: ")

while producto not in nombres_productos:
    print("Producto no existente.")
    producto=input("Ingrese un nuevo producto: ")

indice= 0

for prod in nombres_productos:
    if prod == producto:
        break

    indice= indice + 1

print(f"El precio es: {precios_productos[indice]}")