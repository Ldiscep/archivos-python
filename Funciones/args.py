#vamos a crear una funcion que pueda recibir cualquier cantidad de argumentos
#va a servir para sacar el promedio de una cantidad x de numeros enteros


def promedio(listado): 
    return sum(listado) / len(listado) #sum sirve para obtener la suma de todos los elementos (int y float) que hay en un listado, tupla, etc
                         #len sirve para obtener la cantidad de elementos que se encuentran en un listado, tupla, etc

resultado= promedio([0, 25, 50, 100]) #cabe aclarar que "promedio" es el nombre de la función arriba, mientras que el listado entre paréntesis son los argumentos
#entonces, resultado sería la variable que almacena el resultado de la funcion "promedio" puesta a funcionar con los parámetros/argumentos especificados entre los paréntesis
#el argumento va en forma de lista por que la funcion promedio, solo toma un valor (listado) el cual reemplazamos por la lista 
print("el promedio entre estos números es de:", resultado)
