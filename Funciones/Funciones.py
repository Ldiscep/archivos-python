#para definir una función se utiliza la palabra reservada "def" seguida dcel nombre de una función
#vamos a crear una función que sume numeros

def suma(): #por ahora no vamos a definir parámetros
    num1=int(input("Ingresa el primer número entero: "))
    num2=int(input("Ingresa el segundo número entero: ")) #convertimos el str de input a int
    resultado= num1 + num2 
    respuesta= "El resultado es {}".format (resultado)
    print(respuesta)

suma()
#la funcion se puede llamar todas las veces que queramos