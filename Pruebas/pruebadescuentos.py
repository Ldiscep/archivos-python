# Al elemento en el índice 0 del la lista precio_productos
# se le debe aplicar el descuento indicado en el índice 0
# de la lista descuentos_productos; al elemento en el
# índice 1 de precio_productos, el descuento indicado
# en el índice 1 de descuentos_productos; y así
# sucesivamente.

precios_productos = [150, 100, 500, 200]
# Estos descuentos están expresados en porcentajes.
descuentos_productos = [5, 30, 15, 10]

# De cada precio de la lista precios_productos, imprimir
# su precio tras aplicar el descuento, cada uno en una
# nueva línea.
descuento1= (precios_productos[0]*descuentos_productos[0]) / 100
descuento2= (precios_productos[1]*descuentos_productos[1]) / 100
descuento3= (precios_productos[2]*descuentos_productos[2]) / 100
descuento4= (precios_productos[3]*descuentos_productos[3]) / 100

total1=precios_productos[0]
total2=precios_productos[1]
total3=precios_productos[2]
total4=precios_productos[3]


final1= total1 - descuento1
final2= total2 - descuento2
final3= total3 - descuento3
final4= total4 - descuento4

print(final1)
print(final2)
print(final3)
print(final4)