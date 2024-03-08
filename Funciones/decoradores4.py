def cocina (ingrediente_inicial):

    def ingredientes_añadidos ():

        ingrediente_inicial()
        print('lechuga')
        print('carne')
        print('tomate')
        print('ketchup')
        ingrediente_inicial()
    
    return ingredientes_añadidos


@cocina
def plato (): #ingrediente inicial, no hace falta compartir nombre con la variable parametro de la linea 1
    print('pan')

plato()