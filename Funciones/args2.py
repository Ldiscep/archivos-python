#para que la funcion tome una cantidad indeterminada o infinita de argumentos, se pone un asterisco al principio de los parámetros:
def promedio(*args): #el asterisco sirve para hacer que python genere una tupla con los parámetros y esa tupla se la asigne al parametro con asterisco
                        #por convención, los parámetros con asterisco deben nombrarse ARGS
    return sum(args) / len(args)

resultado=promedio(1, 10, 5, 20)
print(resultado)
