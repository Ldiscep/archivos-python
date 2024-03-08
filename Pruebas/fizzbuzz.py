#este es un ejercicio que se trata de imprimir una serie de números, excepto cuando estos son múltiplos de 3/5.
#para esto se usa el operador "%", que sirve para devolver el resto de una division
#se usa de la siguiente manera: x % 2 . Si el resultado de la division entre estos numeros es exacto se retorna un 0, de lo contrario se retorna un 1. asi podemos ver si el numero es par o impar por ejemplo


for n in range (0,101):
    if n % 3 == 0 and n % 5 == 0: #si n es múltiplo de tres y cinco:
        print("FizzBuzz")
    elif n % 5 == 0: #si n es múltiplo de cinco:
        print("Buzz")
    elif n % 3 == 0: #si n es múltiplo de tres:
        print("Fizz")
    else:
        print(n)
        


