fecha_valida=False

while not fecha_valida:
    fecha=input("Ingresa una fecha en formato dd/mm/aaaa: ")
    
    if len(fecha) != 10:
        print("La fecha debe tener 10 caracteres.")
        continue

    fecha_lista=fecha.split("/")

    if len(fecha_lista) != 3:
        print("La fecha debe tener el formato dd/mm/aaaa.")
        continue

    dia_str= fecha_lista[0]
    mes_str= fecha_lista[1]
    año_str= fecha_lista[2]

    if not dia_str.isdecimal() or not mes_str.isdecimal() or not año_str.isdecimal():
        print("El día, mes y año deben ser números.")
        continue

    dia=int(dia_str)
    mes=int(mes_str)
    año=int(año_str)

    if dia < 1 or dia > 31:
        print("El día debe estar entre 1 y 31.")
        continue
    if mes < 1 or mes > 12:
        print("El mes debe estar entre 1 y 12.")
        continue
    if año < 1900 or año > 2100:
        print("El año debe estar entre 1900 y 2100.")
    
    fecha_valida=True

print("¡La fecha ingresada es correcta!")

        
#dentro del while en vez de usar otros whiles usamos if para que el continue vaya al while principal, y no se mantenga dentro del while en el que está. por que continue sirve para ir al principio del BUCLE en el que está ubicado