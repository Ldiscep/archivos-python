
from os import listdir

largo= len(listdir())
print(f"Archivos y carpetas en el directorio actual: {largo}")

archivos= listdir()
print(*archivos, sep="\n") #el asterisco en archivos significa que queremos que la instruccion sep se aplique a esta lista

