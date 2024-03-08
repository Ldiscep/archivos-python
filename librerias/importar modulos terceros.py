"""
Hay una página con modulos de terceros listados para instalar: pypi.org

ejemplo:
vamos a instalar el módulo pyperclip: 

hay que ejecutar este comando en la consola:
py -m pip install pyperclip

"""

import pyperclip


pyperclip.copy("Hola desde pyperclip") #con este comando copiamos al portapapeles ese texto

texto= pyperclip.paste() #se pega lo que esta copiado en el portapapeles

print(texto)