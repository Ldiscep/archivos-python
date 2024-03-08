#los atributos de una clase se dividen en atributos de clase y atributos de instancia
#los atributos de clase son atributos que le pertenecen a una clase, para utilizarlos hay que si o si utilizar la clase
#los atributos de instancia son atributos que le pertenecen a un objeto, y para utilizarlos hay que trabajar obligatoriamente con el objeto

#para crear atributos de clase hay que crear variables dentro de la clase:

class User:
    nombre= 'Luciano'
    mail= ''  #estos atributos le pertenecen a la clase

#para usar los atributos de clase se hace de la siguiente manera:

print(User.nombre) #nombredelaclase.atributo

#vamos a modificar el atributo nombre de la clase User

User.nombre='Luciano Alfonso'
User.mail= 'lucianodiscepolo@gmail.com'

print(User.nombre)
print(User.mail)