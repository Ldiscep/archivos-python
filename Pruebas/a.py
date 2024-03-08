def pares():
    for numero_par in range(0,1000,2): #el primer argumento es el inicio, el segundo el final y el tercero los saltos, en este caso de dos en dos
        yield numero_par
        print('se ha reanudado la ejecucion de la funcion')

for par in pares():
    print(par)
