lista_archivos = []
txt = 0
exe = 0
normales = 0
nombre = input("Introduce el archivo o escribe 'fin' para terminar: ")
while nombre.lower() != "fin":
    lista_archivos.append(nombre)
    
    if nombre.endswith(".txt"):
        txt += 1
    elif nombre.endswith(".exe"):
        exe += 1
    else:
        normales += 1

    nombre = input("Introduce otro archivo o 'fin' para terminar: ")
print("\nResumen:")
print(f"Archivo ejecutable sin riesgo: {txt}")
print(f"Archivo ejecutable, revisar con cuidado: {exe}")
print(f"Archivo normal: {normales}")
