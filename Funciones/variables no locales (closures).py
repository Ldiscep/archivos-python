#vamos a repasar como funcionan las variables dentro y fuera de las funciones

e='variable global' #esta puede ser utilizada dentro o fuera de los bloques

def principal():
    a= 'a'
    b= 'b'


    def anidada():
        c='c'
        d='d'
        print(a)
        print(b)

    anidada() #la funcion anidada se corre dentro de la principal
    print(c)

principal() #corremos la funcion principal
#En este caso nos va a dar un error al llegar a 'c' ya que no se encuentra definida globalmante, y el print esta localmente en la funcion anidada.
#La variable c no puede ser usada fuera de la funcion

#las variables a y b tienen un scope de un nivel superior a c, aunque actuen como variables locales en el codigo general, actuan como globales para los niveles inferiores a la misma funcion
#es por esto que se ejecutan

