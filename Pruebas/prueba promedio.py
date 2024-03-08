from statistics import mean

curso1=input("Ingresa las notas del curso de Python: ")
curso2=input("Ingresa las notas del curso de Java: ")

curso1= list(map(float, curso1.split()))
curso2= list(map(float, curso2.split()))

curso1.sort()
curso2.sort()

notamasalta1= curso1[-1]
notamasbaja1= curso1[0]

notamasalta2= curso2[-1]
notamasbaja2= curso2[-0]

promedio1= mean(curso1)
promedio2= mean(curso2)


print("Estadísticas del curso de Python:")
print(f"Nota máxima: {notamasalta1}")
print(f"Nota mínima: {notamasbaja1}")
print(f"Promedio de notas: {promedio1}")

print("Estadísticas del curso de Java:")
print(f"Nota máxima: {notamasalta2}")
print(f"Nota mínima: {notamasbaja2}")
print(f"Promedio de notas: {promedio2}")

if notamasalta1 > notamasalta2:
    mejormaxima= "Python"
elif notamasalta1 < notamasalta2:
    mejormaxima= "Java"

print(f"Curso con mejor nota máxima: {mejormaxima}") 

if notamasbaja1 > notamasbaja2:
    mejorminima= "Python"
elif notamasbaja1 < notamasbaja2:
    mejorminima= "Java"

print(f"Curso con mejor nota mínima: {mejorminima}") 

if promedio1 > promedio2:
    mejorpromedio= "Python"
elif promedio1 < promedio2:
    mejorpromedio= "Java"

print(f"Curso con mejor promedio: {mejorpromedio}") 
