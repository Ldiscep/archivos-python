notas=input("Ingresa la lista de notas: ")
notas_float=list(map(float, notas.split()))

aprobadas=[]
desaprobadas=[]

for nota in notas_float:
    if nota >= 7 and nota <= 10:
        aprobadas.append(nota)
    elif nota < 7 and nota >= 1:
        desaprobadas.append(nota)
    else:
        print("Ingresa una nota válida (1-10)")
    
print("Notas aprobadas:")
for aprobada in aprobadas:
    print(aprobada)

print("Notas desaprobadas:")
for desaprobada in desaprobadas:
    print(desaprobada)

#soy fan de este codigo que hice. 
#el objetivo es anotar en una lista las notas aprobadas y en otra las desaprobadas