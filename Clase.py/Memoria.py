class Carro:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

c1 = Carro("blanco", "Ferrari")
c2 = Carro("azul", "Nissan")

print(c1.color, c1.marca)
print(c2.color, c2.marca)
