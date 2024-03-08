#continue sirve para regresar a la cabecera del bucle (for/while)

#en el caso de un bucle for actúa de la siguiente manera:

numeros_primos= [1,2,3,5,7,11,13,17,23]


for n in numeros_primos:        #en este caso no queremos imprimir el 11 y su cuadrado
    
    if n == 11:
        continue
        #volver a la caabecera del bucle y seguir con el próximo elemento.  Sigue con el proximo elemento para evitar la repeticion
    
    cuadrado= n**2
    print(f"El cuadrado de {n} es {cuadrado}")