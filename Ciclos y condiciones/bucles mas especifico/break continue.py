numeros_primos= [1,2,3,5,7,11,13,17,23]

#break= termina el bucle prematuramente
#continue

#en este ejemplo de break quiero imprimir pero solamente hasta el 11

for n in numeros_primos:

    if n == 13:
        break

    print(n)

#break hace que termine el bucle y continue el programa en la proxima linea fuera de este, por lo que la 13 no se ejecuta tampoco
print("Fin")



#el break tambien se puede usar para saber el numero de índice de un elemento junto a un bucle for, por ejemplo:
#tambien se puede usar la funcion index pero bue

productos= ["Mouse", "Teclado", "Mousepad", "Auriculares", "Monitor", "Gabinete"]
indice= 0

for producto in productos:
    if producto == "Monitor":
        print(f"El índice de {producto} es: {indice}")
        break
        
    indice= indice + 1
    #