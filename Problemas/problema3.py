from typing import *

from algoritmia.datastructures.queues import Fifo

from Problemas.problema1 import create_labyrint
from algoritmia.datastructures.digraphs import UndirectedGraph
from random import seed
from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


# traspa 14  <---- CAMBIA
def recorredor_aristas_anchura(g: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas

# traspa 37
def recuperador_camino(lista_aristas: List[Edge], v_final: Vertex) -> List[Vertex]:
    v = v_final
    # Crea un dicionario de punteros hacia atrás (backpointers)
    bp = {}
    for orig, dest in lista_aristas:
        bp[dest] = orig
    # Reconstruye el camino yendo hacia atrás
    camino = []
    camino.append(v)
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    # Invierte el camino pues lo hemos obtenido al revés
    camino.reverse()
    return camino


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Vertex]:
    lista_aristas = recorredor_aristas_anchura(g, source)
    return recuperador_camino(lista_aristas, target)


# -- PROGRAMA PRINCIPAL ------------------------------------------
if __name__ == '__main__':
    seed(1)  # Esto es para que siempre salga el mismo grafico, lo ejecutes donde lo ejecutes
    num_rows = 60
    num_cols = 80
             # El 1000 en [create_laberinth -> n], son las paredes que quitas, Si no ponemos nada es 0, el grafo normal
    graph = create_labyrint(num_rows, num_cols, 1000)
    camino = shortest_path(graph, (0, 0), (num_rows-1, num_cols-1))
    print("Camino: ", camino)
    print("Tamaño camino: ", (len(camino)))
    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.add_path(camino,'blue')
    lv.run()