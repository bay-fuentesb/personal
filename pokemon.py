import json

def crear():
    try:
        # Abrir y cargar el contenido del archivo JSON
        with open("pokedex.json", mode="r") as file:
            leerjson = json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, inicializar un diccionario con una lista vacía
        leerjson = {"kanto": []}
    
    nombre = input("Ingrese el nombre del Pokémon que quieres ingresar: ")
    
    # Verificar si el Pokémon ya existe
    for recorrido in leerjson["kanto"]:
        if recorrido["nombre"] == nombre:
            print("Ese Pokémon ya existe")
            return

    # Solicitar información del nuevo Pokémon
    id = int(input("Ingrese su número en la Pokédex: "))
    tipo = input("Ingrese el tipo del Pokémon: ")
    new_pokemon = {
        "id": id,
        "nombre": nombre,
        "tipo": tipo
    }
    
    # Agregar el nuevo Pokémon a la lista
    leerjson["kanto"].append(new_pokemon)
    
    # Guardar la lista actualizada de vuelta en el archivo JSON
    with open("pokedex.json", mode="w") as file:
        json.dump(leerjson, file, indent=4)
    
    print("Pokémon ingresado correctamente")

crear()
