#las funciones al ser ciudaddanos de primer orden pueden retornar otras funciones

def saludo():

    def mensaje():

        print('Hola, buenos días')

    return mensaje

respuesta=saludo() #esto no va a imprimir el texto de la linea siete, sino que nos va a mostrar que mensaje es parte de saludo
print(respuesta)
print(type(respuesta)) #type function

respuesta() #esto imprime el texto de la linea 7, y se llama asi ya que guardamos la funcion saludo en esta variable
