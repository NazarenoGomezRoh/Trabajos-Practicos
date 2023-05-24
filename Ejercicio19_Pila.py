class Pelicula:
    def __init__(self, titulo, estudio, anio):
        self.titulo = titulo
        self.estudio = estudio
        self.anio = anio


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0


def mostrar_peliculas_2014(pila):
    print("Películas estrenadas en 2014:")
    for pelicula in pila.items:
        if pelicula.anio == "2014":
            print(pelicula.titulo)
    print()


def contar_peliculas_2018(pila):
    contador = 0
    for pelicula in pila.items:
        if pelicula.anio == "2018":
            contador += 1
    return contador


def mostrar_peliculas_marvel_2016(pila):
    print("Películas de Marvel Studios estrenadas en 2016:")
    for pelicula in pila.items:
        if pelicula.anio == "2016" and pelicula.estudio == "Marvel Studios":
            print(pelicula.titulo)
    print()


# Crear pila de películas
pila_peliculas = Pila()
pila_peliculas.apilar(Pelicula("Iron Man I", "Marvel Studios", "2014"))
pila_peliculas.apilar(
    Pelicula("Spider-Man: Homecoming", "Marvel Studios", "2017"))
pila_peliculas.apilar(Pelicula("Wonder Woman", "DC Films", "2017"))
pila_peliculas.apilar(
    Pelicula("Guardians of the Galaxy", "Marvel Studios", "2014"))
pila_peliculas.apilar(Pelicula("Deadpool", "20th Century Fox", "2016"))
pila_peliculas.apilar(Pelicula("Black Panther", "Marvel Studios", "2018"))
pila_peliculas.apilar(
    Pelicula("Doctor Strange", "Marvel Studios", "2016"))  # Nueva película

# Mostrar películas estrenadas en 2014
mostrar_peliculas_2014(pila_peliculas)

# Contar películas estrenadas en 2018
contador_2018 = contar_peliculas_2018(pila_peliculas)
print("Cantidad de películas estrenadas en 2018:", contador_2018)
print()

# Mostrar películas de Marvel Studios estrenadas en 2016
mostrar_peliculas_marvel_2016(pila_peliculas)
