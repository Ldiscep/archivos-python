#un closure es una funcion que puede generar de forma dinamica a otra función. la funcion generada puede acceder a las variables locales aún cuando la principal haya finalizado


def saludo(usuario): #esta funcion es un closure
    mensaje= f'hola {usuario}' #variable local

    def mostrar_mensaje(): #anidada
        print(mensaje)

    return mostrar_mensaje

usuario ='Luciano'
final=saludo(usuario) 
usuario='Juan' #en este caso, se sigue imprimiendo luciano por que la variable se define con usuario siendo igual a luciano
final()
#en este caso, en vez de destruirse la variable 'mensaje' al finalizar la funcion principal, se utiliza en la función anidada para imprimirse  