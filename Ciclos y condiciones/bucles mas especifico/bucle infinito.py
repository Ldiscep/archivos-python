gastos=[]

while True: #esto es un verdadero, no es ninguna comparación. el bucle se va a ejecutar infinitamente
    
    print("1. Registrar un nuevo gasto.")
    print("2. Ver los gastos registrados.")
    print("3. Salir")
    eleccion=input("Ingresar la opcion correspondiente: ")

    if not eleccion.isdecimal():
        input("la opción ingresada no es válida.")
        continue
    else: 
        eleccion= int(eleccion)

    if eleccion == 1: 
        nuevogasto=input("Ingresar el gasto a registrar: $")
        
        if not nuevogasto.isdecimal():
            input("El gasto ingresado no és válido")
            continue
        else: nuevogasto=int(nuevogasto)
        
        gastos.append(nuevogasto)
        print("Gasto Registrado exitosamente.")
        input("Menú Principal")

    elif eleccion == 2: 
        print(f"Hay un total de {len(gastos)} gastos registrados")
        for gasto in gastos:
            print(f"${gasto}")
            print(f"El total de los gastos es de: ${sum(gastos)}")
            
            input("Menú Principal")
    

    elif eleccion == 3: 
        print("Finalizando programa...")
        break #usamos break en vez de exit por que queremos finalizar el bucle, no el programa

    else:
        input("la opción ingresada no es válida.")