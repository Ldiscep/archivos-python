#función lambda o anónima es aquella que se ejecuta en una sola linea de código, tampoco posee un nombre, sirve para analizar tareas muy pequeñas
'''
vamos a pasar esta función a lambda:
def conversion (grados): 
    return 'son {} grados fahrenheit'.format (grados * 1.8 + 32) 
    

print(conversion(123))

'''
#fórmula: lambda <parametros> : <cuerpo>

conversion= lambda grados: grados * 1.8 + 32

#la función lambda siempre retorna la linea de codigo ejecutada, por lo que no es necesario usar return
#despues de la palabra "lambda" se ponen los parámetros separados por comas, y despues de los dos puntos se pone la linea de código a ejecutar por la función

print(conversion(10))
