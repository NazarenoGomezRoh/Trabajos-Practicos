from grafo import Grafo
from lista import Lista as ListaArista
from cola import Cola
from pila import Pila
from heap_min import Heap

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')

"""15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica);
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido."""
 
mi_grafo_n = Grafo(dirigido=False)
mi_grafo_a = Grafo(dirigido=False)

class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
        self.relaciones = {} 

    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.tipo}'
    


mi_grafo_a.insert_vertice(Maravilla('Muralla China', 'China', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Petra', 'Jordania', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Cristo redentor', 'Brasil', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Chichen Itza', 'Mexico', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Machu Picchu', 'Peru', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Coliseo Romano', 'Italia', 'arquitectonica'), criterio= 'nombre')
mi_grafo_a.insert_vertice(Maravilla('Muralla de Adriano', 'UK', 'arquitectonica'), criterio= 'nombre')

mi_grafo_a.insert_arist('Muralla China', 'Petra', 50, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Muralla China', 'Cristo redentor', 77, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Muralla China', 'Chichen Itza', 90, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Muralla China', 'Machu Picchu', 50, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Muralla China', 'Coliseo Romano', 70, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Muralla China', 'Muralla de Adriano', 58, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Petra', 'Cristo redentor', 69, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Petra', 'Chichen Itza', 88, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Petra', 'Machu Picchu', 56, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Petra', 'Coliseo Romano', 57, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Petra', 'Muralla de Adriano', 82, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Cristo redentor', 'Chichen Itza', 46, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Cristo redentor', 'Machu Picchu', 112, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Cristo redentor', 'Coliseo Romano', 73, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Cristo redentor', 'Muralla de Adriano', 67, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Chichen Itza', 'Machu Picchu', 99, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Chichen Itza', 'Coliseo Romano', 102, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Chichen Itza', 'Muralla de Adriano', 107, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Machu Picchu', 'Coliseo Romano', 27, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Machu Picchu', 'Muralla de Adriano', 100, criterio_vertice='nombre')
mi_grafo_a.insert_arist('Coliseo Romano', 'Muralla de Adriano', 64, criterio_vertice='nombre')

mi_grafo_n.insert_vertice(Maravilla('Bahía de Ha-Long', 'Vietnam', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Cataratas del Iguazú', 'Argentina y Brasil', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Montaña de la Mesa', 'Sudáfrica', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Parque Nacional de Komodo', 'Indonesia', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Selva Negra', 'Alemania', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Amazonia', 'Brasil', 'natural'), criterio='nombre')
mi_grafo_n.insert_vertice(Maravilla('Río Subterráneo de Puerto Princesa', 'Filipinas', 'natural'), criterio='nombre')

mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Cataratas del Iguazú', 150, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Montaña de la Mesa', 300, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Parque Nacional de Komodo', 250, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Selva Negra', 400, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Amazonia', 500, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Bahía de Ha-Long', 'Río Subterráneo de Puerto Princesa', 350, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Cataratas del Iguazú', 'Montaña de la Mesa', 200, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Cataratas del Iguazú', 'Parque Nacional de Komodo', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Cataratas del Iguazú', 'Selva Negra', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Cataratas del Iguazú', 'Amazonia', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Cataratas del Iguazú', 'Río Subterráneo de Puerto Princesa', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Montaña de la Mesa', 'Parque Nacional de Komodo', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Montaña de la Mesa', 'Selva Negra', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Montaña de la Mesa', 'Amazonia', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Montaña de la Mesa', 'Río Subterráneo de Puerto Princesa', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Parque Nacional de Komodo', 'Selva Negra', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Parque Nacional de Komodo', 'Amazonia', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Parque Nacional de Komodo', 'Río Subterráneo de Puerto Princesa', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Selva Negra', 'Amazonia', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Selva Negra', 'Río Subterráneo de Puerto Princesa', 450, criterio_vertice='nombre')
mi_grafo_n.insert_arist('Amazonia', 'Río Subterráneo de Puerto Princesa', 450, criterio_vertice='nombre')



#c.
bosque = mi_grafo_a.kruskal()
for arbol in bosque:
    print('---------------------------------arbol expansion minima arquitectonicas---------------------------------')
    for nodo in arbol.split(';'):
        print(nodo)
    
bosque = mi_grafo_n.kruskal()
for arbol in bosque:
    print('---------------------------------arbol expansion minima naturales---------------------------------')
    for nodo in arbol.split(';'):
        print(nodo)

#----------------------------------------A CONSULTAR------------------------------------------------------

#d determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;