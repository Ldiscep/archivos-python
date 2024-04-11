#en un vector de numpy van todos datos del mismo tipo (int/float)
import numpy  as np
array1=np.array([1,2,3,4,5,6,7,8,9,10])
array2 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
print(f"array1: {array1}")

#preguntar a santi por un 
#AttributeError: partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import)

#operaciones elementales entre arrays:
v1=np.array([1,2,3,4,5])
v2=np.array([6,7,8,9,10])
v3=v1+v2
v4=v1*v2
v5= v1 @ v2 #producto interno
#otras que no alcancé a copiar


#slicing        
v= np.array([1,0,3,5,9,4,9,1,0])
print(v[0:4]) # [1 0 3 5]
print(v[1:4]) # [0 3 5]
print(v[3:-1]) # [5 9 4 0 9 1]
print(v[3:]) # [5 9 4 0 9 1 0]