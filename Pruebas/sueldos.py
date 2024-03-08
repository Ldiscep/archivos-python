bruto= int(input("Ingresa el sueldo bruto del empleado: "))

hsextras= int(input("Ingresa las horas extras: "))

antiguedad= int(input("Ingresa la antigüedad (en años): "))

if bruto <= 0:
    exit()

adicional_extras= (bruto * 1) / 100
totalextras= adicional_extras * hsextras


adicional_antiguedad= (bruto * 3) / 100
totalantiguedad= adicional_antiguedad * antiguedad

total_sin_aportes= bruto + totalextras + totalantiguedad

jubilacion= (total_sin_aportes * 11) / 100

total_con_aportes= total_sin_aportes - jubilacion

if total_sin_aportes > 100000:
    impuestos= (total_sin_aportes * 20) / 100
else: 
    impuestos= 0

total_con_impuestos = total_sin_aportes - impuestos

print(f"Sueldo bruto: $ {bruto}")

print(f"Adicional por horas extras: $ {totalextras}")

print(f"Adicional por antigüedad: $ {totalantiguedad}")

print(f"Deducción por jubilación: $ {jubilacion}")

print(f"Deducción por impuestos: $ {impuestos}")

print("---------------------------------------")

print(f"Total a cobrar: $ {total_con_aportes - impuestos}")



#esta es hasta ahora, mi mejor creación. 0 chatgpt, 0 internet. Solo mía. ~26/7/2023 00:23 AM
