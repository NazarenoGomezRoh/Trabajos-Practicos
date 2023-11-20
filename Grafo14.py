"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""
from grafo import Grafo 
from lista import Lista as ListaArista
from cola import Cola
from pila import Pila
from heap_min import Heap


mi_grafo = Grafo(dirigido=False)

mi_grafo.insert_vertice('comedor')
mi_grafo.insert_vertice('cochera')
mi_grafo.insert_vertice('sala')
mi_grafo.insert_vertice('quincho')
mi_grafo.insert_vertice('baño1')
mi_grafo.insert_vertice('baño2')
mi_grafo.insert_vertice('habitacion1')
mi_grafo.insert_vertice('habitacion2')
mi_grafo.insert_vertice('terraza')
mi_grafo.insert_vertice('patio')
mi_grafo.insert_vertice('cocina')




mi_grafo.insert_arist('comedor', 'cochera', 10)  # Distancia entre comedor y cochera: 10 metros
mi_grafo.insert_arist('comedor', 'cocina', 5)  
mi_grafo.insert_arist('comedor', 'sala', 3)  

mi_grafo.insert_arist('cochera', 'cocina', 12)   
mi_grafo.insert_arist('cochera', 'habitacion1', 15) 
mi_grafo.insert_arist('cochera', 'baño1', 3)   

mi_grafo.insert_arist('quincho', 'cocina', 16)   
mi_grafo.insert_arist('quincho', 'patio', 2)   
mi_grafo.insert_arist('quincho', 'habitacion2', 20)   

mi_grafo.insert_arist('habitacion2', 'sala', 8)   
mi_grafo.insert_arist('habitacion2', 'baño2', 9)   
mi_grafo.insert_arist('habitacion2', 'terraza', 7)  
 
mi_grafo.insert_arist('habitacion1', 'cocina', 13)
mi_grafo.insert_arist('habitacion1', 'baño1', 6)
mi_grafo.insert_arist('habitacion1', 'patio', 14) 
mi_grafo.insert_arist('habitacion1', 'cochera', 18) 
mi_grafo.insert_arist('habitacion1', 'cocina', 24) 
  
mi_grafo.insert_arist('cocina', 'cocina', 17)   
mi_grafo.insert_arist('cocina', 'baño2', 16)    
mi_grafo.insert_arist('cocina', 'quincho', 12)    

mi_grafo.insert_arist('patio', 'habitacion2', 11)    
mi_grafo.insert_arist('patio', 'baño1', 19)    
mi_grafo.insert_arist('patio', 'terraza', 4)    
mi_grafo.insert_arist('patio', 'comedor', 21)    
mi_grafo.insert_arist('patio', 'baño2', 8)    

mi_grafo.insert_arist('baño1', 'baño2', 11)   
mi_grafo.insert_arist('baño1', 'cocina', 10)   
mi_grafo.insert_arist('baño1', 'comedor', 3)   

mi_grafo.insert_arist('baño2', 'patio', 6)   
mi_grafo.insert_arist('baño2', 'terraza', 8)   
mi_grafo.insert_arist('baño2', 'quincho', 10)   

mi_grafo.insert_arist('terraza', 'habitacion1', 2)  
mi_grafo.insert_arist('terraza', 'patio', 6)  
mi_grafo.insert_arist('terraza', 'cochera', 17)   

mi_grafo.insert_arist('sala', 'cocina', 21)  
mi_grafo.insert_arist('sala', 'cochera', 13)
mi_grafo.insert_arist('sala', 'habitacion1', 4)

mi_grafo.barrido()
print()

#c. imprimir el arbol de expansion minima dado por el metodo de kruskal
bosque = mi_grafo.kruskal()
for arbol in bosque:
    print("---------------------------------------------------------------------------------")
    print('c.arbol de expansion minima:')
    for nodo in arbol.split(';'):
        print(nodo)
#c. definimos funcion para la cantidad total de metros de cable necesaria (sumando las aristas del arbol de expansion minima)
def cantidad_cables():
    total_cables=0
    bosque=mi_grafo.kruskal()
    for arbol in bosque:
        print ('')
        for nodo in arbol.split(';'):
            partes=nodo.split('-')
            peso=int(partes[-1])
            total_cables+=peso
    print(f'la longitud total de los cables necesarioes es de: {total_cables} metros')

cantidad_cables()

ori = 'habitacion1'
des = 'sala'
origen = mi_grafo.search_vertice(ori)
destino = mi_grafo.search_vertice(des)
camino_mas_corto = None

if origen is not None and destino is not None:
    if mi_grafo.has_path(ori, des):
        camino_mas_corto = mi_grafo.dijkstra(ori, des)
        fin = des
        if camino_mas_corto:
            distancia_total = 0
            camino_str = f"{ori}"
            while camino_mas_corto.size() > 0:
                value = camino_mas_corto.pop()
                distancia_total += value[1]
                camino_str += f" -> {value[0]}"
            print("---------------------------------------------------------------------------------")
            print(f"Se debería instalar un cable desde {ori} hasta {des} de {distancia_total} metros")
            print(f"Camino más corto: {camino_str}")
            print("---------------------------------------------------------------------------------")

