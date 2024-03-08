fecha_valida_inicio=False

while not fecha_valida_inicio:
    
    inicio= input("Fecha de inicio de operaciones (dd/mm/aaaa): \n")

    if len(inicio) != 10:
         print("La fecha debe estar en formato dd/mm/aaaa")
         continue
    
    fecha_dividida= inicio.split("/")
    if len(fecha_dividida) != 3:
        print("La fecha debe estar en formato dd/mm/aaaa")
        continue

    dia_inicio=fecha_dividida[0]
    mes_inicio=fecha_dividida[1]
    año_inicio=fecha_dividida[2]

    if not dia_inicio.isdecimal() or not mes_inicio.isdecimal() or not año_inicio.isdecimal():
        print("El día, mes y año deben estar en formato numérico")
        continue

    dia_inicio=int(dia_inicio)
    mes_inicio=int(mes_inicio)
    año_inicio=int(año_inicio)

    if dia_inicio < 1 or dia_inicio > 31:
        print("El día ingresado no és válido.")
        continue
    if mes_inicio < 1 or mes_inicio > 12:
        print("El mes ingresado no és válido.")
        continue
    
    fecha_valida_inicio= True


fecha_valida_fin= False

while not fecha_valida_fin:
    
    fin= input("Fecha de final de operaciones (dd/mm/aaaa): \n")

    if len(fin) != 10:
         print("La fecha debe estar en formato dd/mm/aaaa")
         continue
    
    fecha_dividida_fin= fin.split("/")
    if len(fecha_dividida) != 3:
        print("La fecha debe estar en formato dd/mm/aaaa")
        continue

    dia_fin=fecha_dividida_fin[0]
    mes_fin=fecha_dividida_fin[1]
    año_fin=fecha_dividida_fin[2]

    if not dia_fin.isdecimal() or not mes_fin.isdecimal() or not año_fin.isdecimal():
        print("El día, mes y año deben estar en formato numérico")
        continue

    dia_fin=int(dia_fin)
    mes_fin=int(mes_fin)
    año_fin=int(año_fin)

    if dia_fin < 1 or dia_fin > 31:
        print("El día ingresado no és válido.")
        continue
    if mes_fin < 1 or mes_fin > 12:
        print("El mes ingresado no és válido.")
        continue
    
    if año_fin < año_inicio:
        print("Hubo un problema al validar los años.")
        continue
    
    fecha_valida_fin= True


dias_totales= dia_fin - dia_inicio
meses_totales= mes_fin - mes_inicio
años_totales= año_fin - año_inicio

diasameses= dias_totales / 30 
tiempo_total= (meses_totales / 12) + (diasameses / 12) + años_totales 
print(tiempo_total, "años trabajados")

mrnh= input("Ingrese el mejor sueldo: \n")

while not mrnh.isdecimal():
    mrnh=input("Ingrese un número, por favor: \n")
    continue
mrnh=float(mrnh)

antiguedad=int(tiempo_total)
total_antiguedad= mrnh * antiguedad

preaviso_ok= False
while not preaviso_ok:
    if tiempo_total < 5: 
        preaviso=input("¿Se notificó al empleado con un mes de anticipación? \n 1) SI \n 2) NO \n")
    else: 
        preaviso=input("¿Se notificó al empleado con dos meses de anticipación? \n 1) SI \n 2) NO \n")
    

    if not preaviso.isdecimal():
        print("Ingrese una opción válida (1/2)")
        continue

    preaviso = int(preaviso)

    if preaviso != 1 and preaviso != 2: 
        print("Ingrese una opción válida.")
        continue

    preaviso_ok= True

if tiempo_total < 5 and preaviso == 2:
    total_preaviso= mrnh
elif tiempo_total > 5 and preaviso == 2:
    total_preaviso = mrnh * 2
else:
    total_preaviso= 0

multaart80_ok = False

while not multaart80_ok:
    multa= input("¿Se le entregó la documentación al empleado? \n 1) SI \n  NO \n")

    if not multa.isdecimal():
        print("Ingrese un número válido" )

