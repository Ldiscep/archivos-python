#en la mayoría de los casos las funciones necesitan valores de entrada para su correcto funcionamiento, se definen variables llamadas parámetros entre los paréntesis de una función

def suma(num1, num2): #acá marcamos que vamos a necesitar dos variables distintas para la función
    
    resultado = num1 + num2
    print(resultado)

#lo que vamos a hacer va a ser que los valores que usa la función para funcionar estén fuera de la función, esto sirve por si después queremos usarlos en alguna otra cosa, o para usar valores que procedan de otros lugares

num1= int(input("Ingresa el primer número: "))
#num2= int(input("Ingresa el segundo número: "))
ag= 123123123123
suma(num1,ag) #acá marcamos cuales son las variables que vamos a usar, no tienen que compartir nombre con las que pusimos en el primer argumento, arriba solo se indica el numero de variables
#en este caso sustitui num2 por "ag" en la función