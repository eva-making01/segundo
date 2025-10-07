
def crear_matriz():
    Calificaciones=[
        [1,2,3],
        [4,4,7],
        [3,3,9],
    ]
    return Calificaciones
def imprimir_calificaciones(Calificaciones):
    for fila in Calificaciones:
        print(fila)
def promedio(Calificaciones):
    for fila in Calificaciones:
        promedio=sum(fila)/len(fila)
        print("Calificaciones", Calificaciones, "promedio=", promedio)

j=crear_matriz()
imprimir_calificaciones(j)
promedio(j)


