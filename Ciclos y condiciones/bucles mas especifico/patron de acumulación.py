#los patrones de código son porciones de código son porciones de codigo que permiten solucionar problemas. uno de esos patrones es el acumulador 
#ejemplo:
precios= [300, 20, 123, 2020]

total= 0
#en este caso el problema es que no siempre vamos a saber la cantidad de productos que hay, y por lo tanto a veces no conviene estar sumando todo individualmente (precios[0] + precios[1]) hay que hacer un patron para sumar todos los elementos sin importar cuantos sean

for precio in precios:
    print (f"+{precio}")
    total= total + precio #este total guarda el valor de la iteracion anterior para la nueva iteracion

print(f"El total es: {total}")
#se le llama patron a esto ya que en cada una de las iteraciones vamos acumulando un dato