import json

def crear():
    with open("pokedex.json", mode="r") as pokemon:
        leerjson = json.load(pokemon)
    region = input("ingrese el nombre de la region con el que desea interactuar")
    nombre = input("Ingrese el nombre del Pokémon que quieres ingresar: ")

    for recorrido in leerjson:
        if recorrido["kanto"] == region:
            if recorrido ["nombre"] == nombre:
                print("ese pokemon ya existe")

    id = int(input("Ingrese su número en la Pokédex: "))
    tipo = input("Ingrese el tipo del Pokémon: ")
    new_pokemon = {
        "id": id,
        "nombre": nombre,
        "tipo": tipo
    }

    leerjson["nombre"].append(new_pokemon)
    with open("pokedex.json", mode="w") as pokemon:
        json.dump(leerjson, pokemon, indent=4)
    
    print("Pokémon ingresado correctamente")

crear()
