#Calculadora
def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b!=0:
        return a / b
    else:
        return("Error no se puede dividir entre 0")
print("1.Suma")#+
print("2.Resta")#-
print("3.Multiplicacion")#*
print("4.Divison")#/
while True:
    Dato = input("Seleccione operacion")
    if Dato in ('1','2','3','4'):
        Num = float(input("Ingresar el numero"))
        Num2 = float(input("Ingrese el otro numero"))
        if Dato =='1':
            print(Num, "+", Num2, "=", sumar(Num, Num2))
        elif Dato =='2':
            print(Num, "-", Num2, "=", restar(Num, Num2))
        elif Dato =='3':
            print(Num, "*", Num2, "=", multiplicacion(Num, Num2))
        elif Dato =='4':
            print(Num, "/", Num2, "=", division(Num, Num2))
        siguiente_calculo=input("Quieres hacer otra operacion si/no:")
        if siguiente_calculo. lower()!= 'si':
            print("Fin")
            break
