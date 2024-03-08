#vamos a hacer una funcion que llame a las dos anteriores, para ver el promedio y si está o no aprobado

promedio= lambda *args : sum(args) / len(args) #

aprobado= lambda calificacion : calificacion >= 7

def resultado (func_promedio, func_aprobado, *args):
    promedio= func_promedio (*args) #se usa * por segunda vez para separar los elementos y que no esten en una tupla

    if func_aprobado(promedio):
        print(f'Materia aprobada con: {promedio}')
    else:
        print('Materia no aprobada')


mensaje=resultado(promedio, aprobado, 8,7,5,2,10,10,10)

"""
Todo esto es muy complicado de leer para mi, asi que lo voy a explicar para mi yo del futuro:

Primero, definimos las funciones lambda 'promedio' y 'aprobado'

'promedio' se encarga de sacar el promedio que hay entre las notas, estas notas se guardan en *args, y se proveen en la linea 16
'aprobado' chequea si el promedio es mayor o igual a 7.

la función 'resultado' mezcla todo, es un quilombo. sus parámetros son, (func_promedio, func_aprobado, y *args)
estos parametros van a ser reemplazados en la linea 16 con (promedio, aprobado y los numeros) respectivamente

la linea 8 hace que la variable 'promedio', que no es la misma que la funcion de la linea 3, sea igual al resultado de func_promedio (reemplazada por la variable 'promedio' de la linea 3) llamada con los args de la linea 16
la linea 10 y 11 hacen que si el resultado de la linea 8 es mayor o igual a 7 (esto se define en la funcion de la linea 5) se imprima en pantalla el texto de la linea 11, else, el texto de la linea 13

finalmente, en linea 16 se llama a la funcion resultado con los parametros que sirven para hacer funcionar todo, siendo estos las funciones lambda de la linea 3 y 5, reemplazando los argumentos (func_promedio y func_aprobado)
y despues los numeros, reemplazando los args
"""