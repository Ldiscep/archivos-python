#vamos a hacer una funcion lambda sin parametros
noparametros= lambda :  True


#vamos a hacer una con parámetros opcionales
opcional= lambda p1=100, p2=200, p3= 300 : p1+p2+p3


#vamos a hacer una con args y kwargs

args= lambda *args, **kwargs : len(args) + len(kwargs)

