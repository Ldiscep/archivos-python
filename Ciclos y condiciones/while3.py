#con while tambien podemos usar else
numero = 123123123

contador=0

while numero >= 1:
    contador= contador+1
    numero=numero/10
else: #se ejecuta cuando la condicion de while no se cumple
    print("Fin del Ciclo")


print(contador)