#para crear un generador vamos a usar la palabra 'yield'

def pares():
    for numero_par in range(0,1000,2): #el primer argumento es el inicio, el segundo el final y el tercero los saltos, en este caso de dos en dos
        yield numero_par
        print('se ha reanudado la ejecucion de la funcion')
for par in pares(): #aca retornamos cada valor iterado de la funcion pares sin tener que finalizar la funcion
    print(par)

#la palabra yield se usa para detener la ejecucion para retornar un objeto hasta que este se haya retornado
#en este caso, hemos creado un 'lazy iterator' esto significa que nos da los numeros cuando se los pedimos
#el generador no se reanuda hasta que se lo llama en la linea 7, una vez por cada elemento

#se reanuda la ejecucion con cada iteracion de la funcion pares

#la diferencia entre yield y return es que yield retorna y pausa y return retorna y finaliza 