#vamos a crear una funcion que nos permita calcular el area de un circulo

def area(radio, pi): #para calcularla, hacen falta dos numeros; el radio y pi
    return pi * (radio**2) #para potenciar un numero se escribe **

resultado=area(10, 3.14)
print(resultado)
#en este caso, los argumentos son obligatorios, ya que con estos se hace la formula de la función