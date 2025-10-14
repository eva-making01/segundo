Alumnos = []
print("Lista vacía:", Alumnos)

def insertar_alumno(nombre, edad, carrera):
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    Alumnos.append(alumno)
nombre = input("Ingrese el nombre del alumno: ")
edad = int(input("Ingrese la edad del alumno: "))
carrera = input("Ingrese la carrera del alumno: ")
insertar_alumno(nombre, edad, carrera)

nombre2 = input("Ingrese el nombre del alumno: ")
edad2 = int(input("Ingrese la edad del alumno: "))
carrera2 = input("Ingrese la carrera del alumno: ")
insertar_alumno(nombre2, edad2, carrera2)

nombre3 = input("Ingrese el nombre del alumno: ")
edad3 = int(input("Ingrese la edad del alumno: "))
carrera3 = input("Ingrese la carrera del alumno: ")
insertar_alumno(nombre3, edad3, carrera3)

print("Alumno", Alumnos)
