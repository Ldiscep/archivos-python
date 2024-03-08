from random import randint
contra=(input("Ingresa una contraseña (4 dígitos): \n"))

contra=str(contra)
numdecaracteres=[]
resp=randint(1,10)
while not contra.isdecimal():
  contra=input("La contraseña tiene que ser numérica y tener cuatro dígitos. \nIngresar Nuevamente: ")

for digito in contra:
         numdecaracteres.append(digito)

def verif(contra):
    global numdecaracteres
    numdecaracteres.clear()
    contra=str(contra)
    for digito in contra:
         numdecaracteres.append(digito)
    global resp
    resp=randint(1,10)


        

while not len(numdecaracteres) == 4:
    if resp == 1: 
        contra=int(input("¡Che, metéle 4 dígitos nomás!\n"))
        verif(contra)
        continue
    elif resp==2:
        contra=int(input("No te hagas el vivo, poné 4 números.!\n"))
        verif(contra)
        continue
    elif resp==3:
        contra= int(input("¡4 dígitos, ni uno más ni uno menos, boludo!\n"))
        verif(contra)
        continue
    elif resp==4:
        contra= int(input("¿Cuántos dígitos? ¡4, papá!\n"))
        verif(contra)
        continue
    elif resp==5:
        contra= int(input("Ni 3, ni 5, acá se usan 4, loco.\n"))
        verif(contra)
        continue
    elif resp==6:
        contra= int(input("¡4, como los 4 fantásticos, che!\n"))
        verif(contra)
        continue
    elif resp==7:
        contra=int(input("No te enrosques, son 4 dígitos.\n"))
        verif(contra)
        continue
    elif resp==8:
        contra=int(input("¡El secreto es 4 dígitos, amigo!\n"))
        verif(contra)
        continue
    elif resp==9:
        contra= int(input("¡Poné 4 y listo, hermano!\n"))
        verif(contra)
        continue
    elif resp==10:
        contra=int(input("¡Che, metéle 4 dígitos nomás!\n"))
        verif(contra)
        continue

# # Esto podría haber sido una función pero la verdad es que soy un virgo
contra=int(contra)
excepciones=[]
numero=randint(0, 10000)


def generacion (inicio, fin):

    global contra
    global numero

    while numero != contra:
        excepciones.append(numero)
        if numero in excepciones:
            numero = randint(inicio,fin)
            print(numero)
    return numero
        

funcion= generacion(0,10000) 
while funcion != contra:
    print(funcion)
else:
    print(f"Tu contraseña era: {funcion}")





