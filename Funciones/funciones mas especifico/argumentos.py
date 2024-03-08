from os import system

curso_python=[1,2,3,9,10,6,10,9,8,7]
curso_java=[4,9,7,9,4,8,5,8]

def aprobadas(curso, nombrecurso):
    print(f"Promedio Curso {nombrecurso}:")
    print(sum(curso)/len(curso))
    
    input("Press enter...")
    system("cls")
    print(f"Notas aprobadas {nombrecurso}:")
    for nota in curso:
        if nota >= 7:
            print(nota)
        else:
            pass
    
while True:
    print("¿Que curso querés consultar?")
    print("1. Python")
    print("2. Java")
    eleccion=input()

    system("cls")

    if eleccion.isdecimal():
        eleccion=int(eleccion)
    else:
        pass

    if eleccion == "Python" or eleccion == "python" or eleccion == 1:
        aprobadas(curso_python, "Python")
        input("Enter para volver al menú principal")
        continue
    elif eleccion == "Java" or eleccion == "java" or eleccion == 2:
        aprobadas(curso_java, "Java")
        input("Enter para volver al menú principal")
        continue
    else:
        system("cls")
        print("Elección no válida.")
        input("Enter para volver al menú principal")
        continue