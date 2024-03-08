#se puede meter una función adentro de otra función
#vamos a hacer una función que simule un deposito y un extracto bancarios

def operacion(cantidad, balance, tipo='deposito'):


    def deposito(cantidad, balance):
        return balance + cantidad


    def retiro (cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
            
        else:
            return None

    
    if tipo == 'deposito':
        return deposito(cantidad, balance) #los parametros de esta call a la función depósito hacen referencia a los de la línea 4
    elif tipo == 'retiro': 
        return retiro(cantidad, balance) #los parametros de esta call a la función retiro hacen referencia a los de la línea 4
      

    
resultado=operacion(1000, 10000, "retiro")
print('dinero restante:',resultado)