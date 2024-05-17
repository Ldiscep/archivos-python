# Calcula el peso de la caja a partir de una lista con los pesos de cada objeto
def pesar_caja_simple(lista_objetos):
    peso_total = sum(lista_objetos)
    return peso_total

# Calcula el peso de la caja a partir de una lista con los pesos de cada objeto, asumiendo que alguno de los objetos podría ser una cja
def pesar_caja(lista_objetos):
    peso_total = 0
    for e in lista_objetos:
        if type(e) == list:
            peso_total += pesar_caja(e)
        else:
            peso_total += e
    return peso_total

print(pesar_caja_simple([800, 430, 220]))
print(pesar_caja([[430, [8700, 430]], 430, 220]))

