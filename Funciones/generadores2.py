#para poder retornar valores se usa return

def pares():
    for numero_par in range(0,100,2): #el primer argumento es el inicio, el segundo el final y el tercero los saltos, en este caso de dos en dos
        return numero_par

print(pares())

#en este caso solo se visualiza 0, ya que al usar return se finaliza inmediatamente la funcion, en este caso, finaliza despues de la primera iteración
#todas las lineas de codigo despues de return no se ejecutan por que la funcion finaliza




