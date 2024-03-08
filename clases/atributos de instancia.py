#los atributos de instancia son atributos que le pertenecen a un objeto, y para utilizarlos hay que trabajar obligatoriamente con el objeto

class User:
    #atributos de clase
    usuario= 'Nombre por defecto' 
    mail= ''

user1= User() #creamos un objeto de tipo usuario de la clase User
print(user1.usuario)

#aca lo que hacemos es:
#definir los atributos de la clase al principio, y en base a esa clase, se crea un usuario que personaliza los atributos de la clase pero solo para ese usuario

#en python