#el tipeo dinamico permite cambiar el tipo de valor de una variable a lo largo del código
valor=("Luciano")
valor=(1)
valor=(2.13)
valor=(True)
print(valor)
#Si ejecutas el codigo de esta manera, unicamente se muestra el último valor asignado (True)
# En cambio, si se ejecuta como está abajo, escribe una vez cada vez que cambio el valor
valor=("Luciano")
print(valor)

valor=(1)
print(valor)

valor=(2.13)
print(valor)

valor=(True)
print(valor)
#lo mejor es usar una variable (o más) para cada tipo de valor
