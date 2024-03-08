from webbrowser import open

urls=[
    "https://python.org",
    "https://docs.python.org",
    "https://recursospython.com"
]
for direccion in urls:
    open(direccion)


#lo que hago aca es promero crear una lista de direcciones, despues de eso hago un bucle for para que se encarge de abrirlas todas mediante la variable direccion