# Solicitar usuario y clave y volver a preguntar si son incorrectos.
usuario_valido = "admin"
clave_valida = "clave123"

user=input("Ingresa el nombre de usuario: ")
password=input("Ingresa la clave:")

while user != usuario_valido and password != clave_valida:
    print("El usuario o la clave son incorrectos.")
    user=input("Ingresa el nombre de usuario: ")
    password=input("Ingresa la clave: ")
    
print("¡Bienvenido!")