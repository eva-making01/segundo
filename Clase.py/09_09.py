"""
valor=int(input("Ingresar figura:"))
if(valor==1):
    print("Es un cuadrado")
elif(valor==2):
    print("Es un rectamgulo")
elif(valor==3):
    print("Es un triangulo")
else:
    print("Figura dewconocida")

area=0
base=0
altura=0
valor=int(input("Ingresar figura"))
if(valor==1):
    base=float(input("Ingresar base:"))
    area=base*base
    print(area)
elif(valor==1):
    valor=int(input("Ingresar figura"))
if(valor==2):
    base=float(input("Ingresar base:"))
    lado=float(input("Ingresar lado"))
    area=base*lado
    print(area)
elif(valor==2):
    valor=int(input("Ingresar figura"))
if(valor==3):
    base=float(input("Ingresar base:"))
    altura=float(input("Ingresar altura"))
    area=(base*altura)/2
    print(area)
else:
    print("Figura desconocida")

password=(input("Ingresar contraseña"))
password_adnmin=12345
rol=input("Ingresar rol:")
intento=(input("Ingresar intento"))
if(password_adnmin==password and rol=="administrador"):
    print("Tienes todos los privilegios")
elif(password_adnmin==password):
    print("Cuenta basica")
else:
    print("No tiene acceso")


lista1=[1,2,3]
lista2=[4,5,6]
matriz=[lista1, lista2]
print(matriz)
matriz[0][2]=8
print(matriz)

datos1=input("Ingresar elemento1:")
datos2=input("Ingresar elemento2:")
datos3=input("Ingresar elemento3:")
datos4=input("Ingresar elemento4:")
lista1=[datos1, datos2]
lista2=[datos3, datos4]
matriz=[lista1, lista2]
print(matriz)

contador=1
while(contador<=5):
    print(contador)
    contador+=1

contador=1
while(contador<=10):
    if(contador%2==0):
        print("el numero:",contador,"es par")
    contador=contador+1

password="7"
while(bandera==False):
    intento=(input("Ingresar"))
    if(intento==password):
        bandera=True
        print("Correcto")
    elif(intento!=password):
        print("Incorrecto")
"""
salir=1
bandera=False
contador=0
while bandera==False:
    animal=input("ingresar animal:")
    if(animal==salir):
        print("Fin de la lista")
        bandera=True
    contador+=1
print(contador)

