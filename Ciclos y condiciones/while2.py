#proximo caso, sin saber la cantidad de iteraciones
#vamos a imprimir la cantidad de digitos que tiene un numero entero


numero= 123435156313241651531263
digitos=0

while numero >= 1:
    digitos=digitos + 1 
    #otra opcion para anotar lo de la linea 9 es:digitos +=1 (abreviatura)

    numero = numero /10 #se divide por 10 por que cada vez que un numero se divide por 10, se le resta un digito. Hasta llegar a un numero menor que 1
    
resultado= "El número tiene {} dígitos".format(digitos)
print(resultado)


