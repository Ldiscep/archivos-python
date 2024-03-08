notas = [9, 5, 3, 7.5, 2, 8.6, 6, 4.5, 1]

aprobadas=0
desaprobadas=0
for nota in notas:
    if nota >= 4:
        aprobadas= aprobadas + 1
    elif nota < 4:
        desaprobadas= desaprobadas + 1
    elif nota < 1 or nota > 10:
        print("Ingresa una nota válida (1-10)")
        exit()

print(f"Cantidad de notas aprobadas: {aprobadas}")
print(f"Cantidad de notas desaprobadas: {desaprobadas}")