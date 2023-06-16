class Personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

# Creamos la cola con los personajes de Marvel
cola_marvel = [
    Personaje("Tony Stark", "Iron Man", "M"),
    Personaje("Steve Rogers", "Capitán América", "M"),
    Personaje("Natasha Romanoff", "Black Widow", "F"),
    Personaje("Carol Danvers", "Capitana Marvel", "F"),
    Personaje("Scott Lang", "Ant-Man", "M")
]

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_personaje_capitana_marvel = ""
for personaje in cola_marvel:
    if personaje.nombre_superheroe == "Capitana Marvel":
        nombre_personaje_capitana_marvel = personaje.nombre_personaje
        break
print("a. El nombre del personaje de la Capitana Marvel es:", nombre_personaje_capitana_marvel)

# b. Mostrar los nombres de los superhéroes femeninos
superheroes_femeninos = [personaje.nombre_superheroe for personaje in cola_marvel if personaje.genero == "F"]
print("b. Los nombres de los superhéroes femeninos son:", superheroes_femeninos)

# c. Mostrar los nombres de los personajes masculinos
personajes_masculinos = [personaje.nombre_personaje for personaje in cola_marvel if personaje.genero == "M"]
print("c. Los nombres de los personajes masculinos son:", personajes_masculinos)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
nombre_superheroe_scott_lang = ""
for personaje in cola_marvel:
    if personaje.nombre_personaje == "Scott Lang":
        nombre_superheroe_scott_lang = personaje.nombre_superheroe
        break
print("d. El nombre del superhéroe de Scott Lang es:", nombre_superheroe_scott_lang)

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
personajes_con_S = [personaje for personaje in cola_marvel if personaje.nombre_personaje.startswith("S") or personaje.nombre_superheroe.startswith("S")]
print("e. Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for personaje in personajes_con_S:
    print("   - Nombre del personaje:", personaje.nombre_personaje)
    print("     Nombre del superhéroe:", personaje.nombre_superheroe)
    print("     Género:", personaje.genero)

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
encontrado = False
nombre_superheroe_carol_danvers = ""
for personaje in cola_marvel:
    if personaje.nombre_personaje == "Carol Danvers":
        encontrado = True
        nombre_superheroe_carol_danvers = personaje.nombre_superheroe
        break
if encontrado:
    print("f. Carol Danvers se encuentra en la cola. Su nombre de superhéroe es:", nombre_superheroe_carol_danvers)
else:
    print("f. Carol Danvers no se encuentra en la cola.")
