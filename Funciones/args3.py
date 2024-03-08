#el uso del asterisco no nos limita a no usar otros parámetros

def combinacion(p1, p2, *args, p4): #tambien podemos añadir un parámetro opcional, para que a este se le asigne un valor tenemos que poner su nombre en los argumentos dados en linea9
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(1,2,3,4,5,6,7,8,p4=9)
#guardamos los primeros dos valores en las primeras dos variables y todos los demas al args