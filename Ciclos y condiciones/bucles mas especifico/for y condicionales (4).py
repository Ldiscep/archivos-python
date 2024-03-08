numeros_primos= [1, 2, 3, 5, 7, 11, 13, 17, 23]

for n in numeros_primos:
    #en este caso vamos a querer omitir el 11
    if n != 11:
        cuadrado= n**2    
        print(f"El cuadrado de {n} es {cuadrado}")
    else: 
        print("Se omitió el 11.")