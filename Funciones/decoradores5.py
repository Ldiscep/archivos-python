#vamos a hacer que la funcion a decorar reciba argumentos/parametros y retorne un valor
#para eso hay que adaptar el decorador, usando args y kwargs


"""
decorador=a
a decorar=b
decorada=c
"""

def decorador (funcion_a_decorar):
    
    def funcion_decorada(*args, **kwargs): #si aca no ponemos args y kwargs, nos va a dar un error, ya que le estamos dando dos valores en la linea 23, pero no estaria teniendo donde almacenarlos
        print('el resultado es: ')
        funcion_a_decorar(*args,**kwargs) #funcion_a_decorar=suma
    return funcion_decorada


@decorador
def suma (num1, num2):
    return num1 + num2

#si ahora llamaramos a la funcion de la siguiente manera: suma(10, 20), el resultado sería "el resultado es:" sin ningun resultado de suma, esto es por que en ningun momento se imprime lo que retorna la suma
#hay que llamarla de la siguiente manera

resultado=suma(10,20)
print(resultado) #ahora el resultado es "el resultado es: None" lo vamos a solucionar en el proximo documento
