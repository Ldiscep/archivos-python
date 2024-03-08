notas=input("Ingresa la lista de notas (separadas por espacios): ")

notas= list(map(float,notas.split()))

notas.sort()

print("Notas ordenadas de menor a mayor:")
print(*notas, sep="\n")


notas.sort(reverse=True)
print("Notas ordenadas de mayor a menor:")
print(*notas, sep="\n")