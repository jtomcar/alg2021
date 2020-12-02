from typing import *
from algoritmia.datastructures.queues import Fifo
from algoritmia.datastructures.digraphs import UndirectedGraph
from graph2dviewer import Graph2dViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def knight_graph(num_rows: int, num_cols: int) -> UndirectedGraph:

    #TODO Hay que modificar el problema del caballo del ajedrez

    vertices: List[Vertex] = [(r,c) for r in range(num_rows) for c in range(num_cols)]

    edges: List[Edge] = []
    #Creamos la arista de arriba e izquierda de cada vertice
    for r, c in vertices:  # r,c = (r,c) = v Desglosas la tupla
        for (ir, ic) in [(-2,-1),(-1,-2),(-2,1), (-1,2)]:
            if (0 <= (r+ir) < num_rows) and (0 <= (c + ic) < num_cols):
                edges.append(((r,c), (r+ir, c+ic)))

    return  UndirectedGraph(V=vertices, E=edges)

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
    num_rows = 8
    num_cols = 8
             # El 1000 en [create_laberinth -> n], son las paredes que quitas, Si no ponemos nada es 0, el grafo normal
    graph = knight_graph(num_rows, num_cols)
    camino = shortest_path(graph, (0, 0), (num_rows-1, num_cols-1))
    viewer = Graph2dViewer(graph, window_size=(1200, 800))
    viewer.run()
