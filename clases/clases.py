#para crear clases se usa la palabra reservada 'class'. Esta permite representar a un usuario
#se escribe con la nomenclatura <CamelCase>, esto significa que todas las palabras tienen su primera letra en mayuscula, en caso de ser dos o mas palabras estas se unenc como en el ejemplo anterior
class Usuario:
    pass #le indicamos a python que por ahora el bloque no hace nada, no se lo puede dejar vacio por que sino nos da un error


#una vez definida la clase podemos instanciar cualquier cantidad d eobjetos que queramos
Luciano = Usuario() #dentro de los parentesis van los argumentos para inicializar los atributos de objeto, en este caso no ponemos nada.

print(Luciano) #el objeto es de tipo usuario