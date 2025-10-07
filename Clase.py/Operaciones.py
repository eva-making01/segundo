#Clase 4 de semtiembre 

#Recibir tres animales
#Formar una lista
#Imprimir la lista
#Modificar la ultima posicion 
animal1=input("Ingresar animal1: ")
animal2=input("Ingresar animal2: ")
animal3=input("Ingresar animal3: ")
lista=[animal1, animal2, animal3]
print("tu lista es:", lista)
lista[2]="tortuga"
print("tu lista es:", lista)
animal_nuevo="Gato"
lista.append(animal_nuevo)
print(lista)
lista.pop()
print(lista)
#Ejercicio
#Ingresar 2 colores 
#Asignar a una lista
#Imprimir la lista
#Insertar al final un nuevo color
#Imprimir la lista