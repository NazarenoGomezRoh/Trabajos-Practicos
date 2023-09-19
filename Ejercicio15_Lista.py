# Lista de entrenadores Pokémon, donde cada entrenador es una lista con su información
# [nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, lista_de_pokémons]
entrenadores_pokemon = [
    ["Ash Ketchum", 10, 2, 50, [["Pikachu", 50, "Eléctrico", None],
                                ["Charizard", 70, "Fuego", "Volador"]]],
    ["Misty", 5, 15, 25, [["Starmie", 60, "Agua", "Psíquico"],
                          ["Gyarados", 30, "Agua", "Volador"]]],
    ["Brock", 7, 18, 28, [["Onix", 40, "Roca", "Tierra"],
                          ["Geodude", 20, "Roca", "Tierra"]]],
    ["Gary Oak", 15, 8, 48, [["Blastoise", 75, "Agua", None],
                             ["Arcanine", 80, "Fuego", None]]],
    ["Erika", 4, 4, 6, [["Terrakion", 90, "Roca", "Lucha"],
                        ["Pikachu", 55, "Eléctrico", None]]]
]

# a.


def cantidad_de_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return len(entrenador_pokemon[4])
    return 0

# b.


def entrenadores_mas_de_tres_torneos():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[1] > 3:
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores

# c.


def pokemon_mas_poderoso():
    entrenador_mas_torneos = max(entrenadores_pokemon, key=lambda x: x[1])
    pokemons_entrenador_mas_torneos = entrenador_mas_torneos[4]
    pokemon_mas_nivel = max(
        pokemons_entrenador_mas_torneos, key=lambda x: x[1])
    return pokemon_mas_nivel[0]

# d.


def datos_entrenador(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return entrenador_pokemon

# e.


def entrenadores_porcentaje_batallas_ganadas():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        porcentaje_ganadas = (
            entrenador_pokemon[3] / (entrenador_pokemon[3] + entrenador_pokemon[2])) * 100
        if porcentaje_ganadas > 79:
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores

# f.


def entrenadores_pokemon_tipo_fuego_planta_o_agua_volador():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        pokemons_entrenador = entrenador_pokemon[4]
        tipos = [pokemon[2] for pokemon in pokemons_entrenador]
        subtipos = [pokemon[3]
                    for pokemon in pokemons_entrenador if pokemon[3] is not None]
        if ("Fuego" in tipos and "Planta" in tipos) or (("Agua" in tipos) and ("Volador" in subtipos)):
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores

# g.


def promedio_nivel_entrenador(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            pokemons_entrenador = entrenador_pokemon[4]
            niveles = [pokemon[1] for pokemon in pokemons_entrenador]
            if niveles:
                return sum(niveles) / len(niveles)
    return 0

# h.


def entrenadores_con_pokemon(pokemon_buscado):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if pokemon[0] == pokemon_buscado:
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores

# i.


def entrenadores_con_pokemons_repetidos():
    entrenadores = []
    nombres_pokemon = set()
    for entrenador_pokemon in entrenadores_pokemon:
        pokemons_entrenador = entrenador_pokemon[4]
        for pokemon in pokemons_entrenador:
            nombre_pokemon = pokemon[0]
            if nombre_pokemon in nombres_pokemon:
                entrenadores.append(entrenador_pokemon[0])
                break
            nombres_pokemon.add(nombre_pokemon)
    return entrenadores

# j.


def entrenadores_con_pokemons_especificos(pokemons_especificos):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon_entrenador in entrenador_pokemon[4]:
            if pokemon_entrenador[0] in pokemons_especificos:
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores

# k.


def entrenador_tiene_pokemon(entrenador, pokemon):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            pokemons_entrenador = entrenador_pokemon[4]
            for pokemon_entrenador in pokemons_entrenador:
                if pokemon_entrenador[0] == pokemon:
                    return True, entrenador_pokemon
    return False, None


# funciones
print("a. Cantidad de Pokémons de Ash Ketchum:",
      cantidad_de_pokemons("Ash Ketchum"))
print("b. Entrenadores con más de tres torneos ganados:",
      entrenadores_mas_de_tres_torneos())
print("c. Pokémon más poderoso del entrenador con más torneos ganados:",
      pokemon_mas_poderoso())
print("d. Datos de entrenador Ash Ketchum y sus Pokémons:",
      datos_entrenador("Ash Ketchum"))
print("e. Entrenadores con porcentaje de batallas ganadas mayor al 79%:",
      entrenadores_porcentaje_batallas_ganadas())
print("f. Entrenadores con Pokémon de tipo fuego y planta o agua/volador:",
      entrenadores_pokemon_tipo_fuego_planta_o_agua_volador())
print("g. Promedio de nivel de Pokémons de Ash Ketchum:",
      promedio_nivel_entrenador("Ash Ketchum"))
print("h. Entrenadores con Pikachu:", entrenadores_con_pokemon("Pikachu"))
print("i. Entrenadores con Pokémon repetidos:",
      entrenadores_con_pokemons_repetidos())
print("j. Entrenadores con Tyrantrum, Terrakion o Wingull:",
      entrenadores_con_pokemons_especificos(["Tyrantrum", "Terrakion", "Wingull"]))
tiene_pokemon, datos = entrenador_tiene_pokemon("Ash Ketchum", "Pikachu")
if tiene_pokemon:
    print(f"k. Ash Ketchum tiene a Pikachu: {datos}")
else:
    print("k. Ash Ketchum no tiene a Pikachu")
