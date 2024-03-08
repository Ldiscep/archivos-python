meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

mes=input("Ingresa el número de mes: ")

if not mes.isdecimal():
    print("Solo se permiten números.")
    exit()


mes_int=int(mes)

if mes_int < 1 or mes_int > 12:
    print("El mes debe estar entre 1 y 12.")
    exit()
seleccionado= meses[mes_int - 1]
print(seleccionado)