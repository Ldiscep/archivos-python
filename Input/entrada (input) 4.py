nombre=input("Ingresa tu nombre: ")

edad=input(nombre + ", ingresa tu edad: ")
edad= int(edad)
#en vez de hacer lo mostrado en la línea 4, se podría hacer edad=int(input("ingresa tu edad"))
altura=input(nombre + ", ingresa tu altura: ")
altura= float(altura)
#en vez de hacer lo mostrado en la línea 7, se podría hacer altura=float(input("ingresa tu altura"))
autorizacion=input("¿autorizas el programa? (si/no) ")
autorizacion= autorizacion== "sis"
#arriba, al usar el comparados == (igual que), "si", la variable se vuelve "True"
print(autorizacion)
#a partir de aca, no es contenido que salga en el curso hasta ahora, son cosas que yo probe

if autorizacion==True:
    print(nombre, edad, "años, ", altura,  " metros")
else:
     print(nombre, ", autoriza para continuar")
