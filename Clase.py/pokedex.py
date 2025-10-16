Pokedex = []
def agregar_pokemon(nombre, tipo, PS):
    pokemon = {
        "nombre": nombre,
        "tipo": tipo,
        "PS": PS,
    }
    Pokedex.append(pokemon)
    print(f"Pokémon {nombre} agregado a la Pokédex.")
def mostrar_pokedex():
    for pokemon in Pokedex:
        print(f"Nombre: {pokemon['nombre']}, Tipo: {pokemon['tipo']}, PS: {pokemon['PS']}")
def eliminar_pokemon(nombre):
    global Pokedex
    Pokedex = [p for p in Pokedex if p["nombre"] != nombre]
    print(f"Pokémon {nombre} eliminado de la Pokédex.")
while True:
    print("\nMenú de la Pokédex")
    print("1. Agregar Pokémon")
    print("2. Mostrar Pokédex")
    print("3. Eliminar Pokémon")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
            nombre = input("Ingrese el nombre del Pokémon: ")
            tipo = input("Ingrese el tipo del Pokémon: ")
            PS = int(input("Ingrese los puntos de salud (PS) del Pokémon: "))
            agregar_pokemon(nombre, tipo, PS)
    elif opcion == "2":
            mostrar_pokedex()
    elif opcion == "3":
            nombre = input("Ingrese el nombre del Pokémon a eliminar: ")
            eliminar_pokemon(nombre)
    elif opcion == "4":
            print("Saliendo de la Pokédex.")
            break
    else:
        print("Opción no válida. Intente de nuevo.")