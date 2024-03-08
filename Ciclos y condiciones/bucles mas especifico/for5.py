#vamos a usar un bucle for para validar una lista que le pedimos al usuario
from statistics import mean

notas= input("Ingresa la lista de notas: ")
notas=list(map(int, notas.split()))

#lo que pasa hasta aca es que si el usuario ingresa un caracter que no sea un número, da un error.
#la validación tiene que ir antes de la línea de código que da el error, en este caso "notas=list(map(int, notas.split()))" en la línea 5

#continúa en for6.py
