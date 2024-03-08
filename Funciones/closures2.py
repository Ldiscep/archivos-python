#vamos a modificar el valor de una variable local en un subbloque o bloque anidado
#para tener la misma variable, con el mismo id, se usa 'nonlocal'
e='variable global' 

def principal ():
    a= 'a'
    b= 'b'

    

    def anidada():
        c = 'c'
        nonlocal b #le indica a python que no nos estamos refiriendo a una variable local, sino a una con un scope superior
        b='valor cambiado'

        print(b)
        print(id(b)) #aca se imprime la variable de linea 14

    anidada()
    print(b)
    print(id(b))#aca se imprime la variable de la linea7, la misma.
principal()