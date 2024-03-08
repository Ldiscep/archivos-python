#un generador es una funcion que retorna objetos que son faciles de iterar sin que la funcion finalice
#vamos a hacer un generador que itere los numeros pares del 0 al 100

def pares():
    for numero_par in range(0,100,2): #el primer argumento es el inicio, el segundo el final y el tercero los saltos, en este caso de dos en dos
        print(numero_par)

pares()

#en este caso esto no es un generador ya que la funcion finaliza