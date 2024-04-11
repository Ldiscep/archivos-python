#en un vector de numpy van todos datos del mismo tipo (int/float)
import numpy  as np
array1=np.array([1,2,3,4,5,6,7,8,9,10])
array2 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
print(f"array1: {array1}")

#preguntar a santi por un 
#AttributeError: partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import)

"""
uint8: int de 8 bits, puede representar numeros [0, 255].
caso de overflow: 250 + 10 = 4 (cero cuenta)
int8: int de 8 bits, puede representar numeros [-128, 127]

uint16: int de 16 bits, puede representar numeros [0, 65535]
int16: int de 16 bits, puede representar numeros [-32768, 32767]

uint32: int de 32 bits, puede representar numeros [0, 4294967295]
int32: int de 32 bits, puede representar numeros [-2147483648, 2147483647]

y asi...
"""