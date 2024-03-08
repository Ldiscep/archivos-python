nota=float(input("Ingresa la nota: "))

if nota > 10 or nota < 1:
    print("Solo numeros del 1 al 10")
    exit() #el exit en este caso se utiliza para hacer que finalize el programa una vez ejecutada esa linea.
elif nota >= 7: 
    print("Aprobado")
elif nota < 7: 
    print("Desaprobado")