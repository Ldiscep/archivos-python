#para crear una sublista sin aumentar el espacio n memoria se hace de la siguiente manera:

productos= ["Parlantes", "Monitor", "Mouse", "Teclado", "USB", "Disco ssd", "Placa de video", "placa de sonido"]

for indice in [3,4,5,6]: #definimos la variable indice que va a ir teniendo como valores 3, 4, 5 y 6
    print(productos[indice]) #imprimimos el elemento de la lista productos con el indice que tenga la variable de arriba en esa iteración