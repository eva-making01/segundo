#Nivel 1
def imprimir_nombre():
    print("Ruben")
def imprimir_asterisco():
    print("********")
def imprimir_motivacion():
    print("El exito no es un destino es un viaje")
imprimir_asterisco()
imprimir_nombre()
imprimir_motivacion()
#Nivel 2
def nombre(nombre):
    print("Saludos", nombre)
def suma(sum1, sum2):
    respuesta = sum1 + sum2
    return respuesta

sum1 = float(input("Ingrese el primer número: "))
sum2 = float(input("Ingrese el segundo número: "))

resultado = suma(sum1, sum2)
print("La suma es:", resultado)

def check_edad(valor_edad):
    if valor_edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

edad_usuario = float(input("Escriba su edad: "))
check_edad(edad_usuario)
#Nivel 3
def multiplicar(por1, por2):
    respuesta = por1 * por2
    return respuesta

por1 = float(input("Ingrese el primer número: "))
por2 = float(input("Ingrese el segundo número: "))

resultado = multiplicar(por1, por2)
print("La multiplicacion es:", resultado)

def multiplicar(por1, por2):
    respuesta = por1 * por2
    return respuesta

por1 = float(input("Ingrese el primer número: "))
por2 = float(input("Ingrese el segundo número: "))

resultado = multiplicar(por1, por2)
print("La multiplicacion es:", resultado)

def letras(texto):
    return len(texto)
texto1=input("Ingrese el texto")
cantidad=letras(texto1)
print("Cantidad de letras igual a", cantidad)


