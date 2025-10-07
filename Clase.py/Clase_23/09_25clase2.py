def ingresar_palabras():
    palabras = []
    while True:
        palabra = input("Escribe una palabra (o 'fin' para terminar): ")
        palabras.append(palabra)
        if palabra == 'fin':
            print("Fin del ingreso de palabras.\n")
            break
    return palabras

def imprimir_palabras(palabras):
    if not palabras:
        print("No se ingresaron palabras.")
    else:
        print("Palabras ingresadas:")
        for i, palabra in enumerate(palabras, start=1):
            print(f"{i}. {palabra}")

lista = ingresar_palabras()
imprimir_palabras(lista)

