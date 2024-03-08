#vamos a definir una función para limpiar la consola 
import os
nombre=input("Ingresa tu nombre: ")
def limpiar():
    os.system("cls") #system sirve para correr cualquier comando en la consola, cls es una funcion de consola que sirve para limpiarla
                     #el problema con esto es que el comando cls solo sirve en windows, con ayuda del módulo os, vamos a poder chequear que sistema operativo se está usando

nombre_sistema=os.name #sirve para saber que sistema operativo estamos usando

def limpiar_completo():
    if nombre_sistema == "nt": #nt es el nombre de una versión de windows antigua, por alguna razón se sigue usando esa
        os.system("cls")
    else: 
        os.system("clear") # es como el cls de linux o mac

limpiar_completo()



print(f"Hola {nombre}")



edad= input("Ingresa tu edad: ")


def validacion_edad():
    
    global edad #indicamos que vamos a usar la variable edad de fuera de la función, es distinto a nonlocal, ya que con nonlocal nos referimos a la variable de una funcion padre

    while not edad.isdecimal():
        print("La edad ingresada no es válida")
        edad=input("Ingrese una edad válida: ")
    
    edad=int(edad)
    

validacion_edad()

limpiar_completo()
while edad < 1:
    print("La edad ingresada no es válida")
    edad=input("Ingrese una edad válida: ")
    validacion_edad()
if edad > 65:
    print(f"Usted ya se encuentra en edad de jubilación hace {edad - 65} años.")
else:
    print(f"{nombre}, para jubilarte te faltan {65 - edad} años")
limpiar_completo()
    
