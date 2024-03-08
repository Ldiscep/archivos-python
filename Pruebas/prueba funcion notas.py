notas=input("Ingresa tus notas: ")
notas=list(notas)

notas_verificadas=[]

for nota in notas:
    if not nota.isdecimal():
        print(f"La nota '{nota}' ingresada no és válida")
    else:
        notas_verificadas.append(nota) 

        

notas_verificadas=list(map(float, notas_verificadas))


def promediar(notas):
    promedio= sum(notas) / len(notas)
    return promedio

resultado=promediar(notas_verificadas)

if resultado >= 7:
    print(f"Nota final: {resultado} \nAprobado")
else: print(f"Nota final: {resultado} \nDesaprobado")