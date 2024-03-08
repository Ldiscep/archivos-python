#elif se usa para evaluar multiples condiciones y poder ejecutar diferentes bloques.
# las condiciones se evalúan de manera descendente
calificación = int(input("Ingresa tu nota: "))

if calificación == 10:
    print("Aprobaste con nota perfecta")
elif calificación < 10 and calificación >= 7: #tambien puede escribirse: calificación == 9 or calificacion == 8 or calificacion == 7:
    print("Aprobaste")
elif calificación > 10:
    print("Ingresar la nota correctamente")
else:
    print("Desaprobaste")

