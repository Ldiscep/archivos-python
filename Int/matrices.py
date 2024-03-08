#usando listas se pueden almacenar diferentes tipos de datos, incluidas otra listas

#vamos a crear una matriz de 2x2, para ello vamos a crear una lista que contenga dos listas mas
columna_a=[10, 20]
columna_b=[30, 40]
matriz=[columna_a, columna_b] 
# ^ esta es una lista, funciona como una matriz bidimensional, esto significa que tiene dos columnas, que poseen dos filas
print(matriz)
#para obtener el número, hay que poner su número de índice en la Y (vertical)  y en la posición X (horizontal)
#ejemplo:
print(matriz[0][1]) # esto consigue el número 20
print(matriz[1][0]) # esto consigue el número 30
print(matriz[1][1]) # esto consigue el número 40

#a continuación, matrices mas complejas: (todo esto no sale en el curso, me lo acabo de inventar)
columna_1=["A", "B", "C"]
columna_2=["D", "E", "F"]
columna_3=["G", "H", "I"]
columna_4=["J", "K", "L"]
columna_5=["M", "N", "Ñ"]
columna_6=["O", "P", "Q"]
columna_7=["R", "S", "T"]
columna_8=["U", "V", "W"]
columna_9=["X", "Y", "Z"]
matriz_abecedario=[columna_1, columna_2, columna_3, columna_4, columna_5, columna_6, columna_7, columna_8, columna_9]
#ahora va un vago ejemplo de escribir mi nombre en una matriz, usando las coordenadas
print(matriz_abecedario[3][2]) 
print(matriz_abecedario[7][0])
print(matriz_abecedario[0][2])
print(matriz_abecedario[2][2])
print(matriz_abecedario[0][0])
print(matriz_abecedario[4][1])
print(matriz_abecedario[5][0])
# uix a marzo