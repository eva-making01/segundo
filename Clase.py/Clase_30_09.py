matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matriz[0])
print(matriz[1])
print(matriz[2])
for fila in matriz:
    print(fila)
print(matriz)

matriz.append([10,11,12])
print("Matriz nueva")
matriz[0].insert(1,99)
print("Matriz nueva")

matriz.pop()
print(matriz)
matriz[1].pop()
print(matriz)
matriz[0].remove(2)
print(matriz)

calificaciones =[
    [100,80,90],
    [80,70,90],
    [100,85,90],
]
alumno=1
for fila in calificaciones:
    promedio=sum(fila)/len(fila)
    print("Alumno", alumno, "con promedio:", promedio)
    alumno+=1