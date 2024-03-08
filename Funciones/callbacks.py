#callbacks son las funciones que son utilizadas como argumento para otra funcion
#vamos a hacer una funcion lambda que nos permita obtener el promedio de un listado

promedio= lambda *args : sum(args) / len(args) #usamos args por que vamos a ponerle muchos elementos, asi se convierte en una tupla de valores

aprobado= lambda calificacion : calificacion >= 7 #aca la calificacion va a retornar true si calificacion es igual o mayor que 7, el argumento calificacion va a ser reemplazado con los valores de la linea 9

print(promedio(5,8,10,8))
print(aprobado(promedio(5,8,10,8))) #aca lo que hago es pasar la funcion calificacion con la funcion promedio con los argumentos (5,8,10,8)


