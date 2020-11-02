from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle, seed
from labyrinthviewer import LabyrinthViewer

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def create_labyrint(num_rows: int, num_cols: int, n: int = 0) -> UndirectedGraph:

    vertices: List[Vertex] = []
    for r in range(num_rows):
        for c in range(num_cols):
            vertices.append((r,c))

    mfs:MergeFindSet[Vertex] = MergeFindSet()  #Merge es mezclar todas para que tengan la misma etiqueta
    for v in vertices: #Le damos a todos los vertices la misma etiqueta
        mfs.add(v)

    edges: List[Edge] = []
    #Creamos la arista de arriba e izquierda de cada vertice
    for r, c in vertices:  # r,c = (r,c) = v Desglosas la tupla
        if r > 0:
            edges.append( ((r,c),(r-1,c)) )      #r=row=fila
        if c > 0:
            edges.append( ((r,c),(r,c-1)) )     #c=colum=columna

    shuffle(edges) #baraja las aristas

    #Paso 4
    corridors:List[Edge] = [] #pasillos de nuestro grafo

    #Paso 5
    for u, v in edges:
        if (mfs.find(u)!=mfs.find(v)):
            mfs.merge(u,v)
            corridors.append( (u,v) )
        else:
            if n > 0:
                corridors.append((u, v))
                n -= 1
    #Paso 6
    return  UndirectedGraph(E=corridors)

# -- PROGRAMA PRINCIPAL ------------------------------------------
if __name__== '__main__':
    seed(42) #Esto es para que siempre salga el mismo grafico, lo ejecutes donde lo ejecutes
    graph = create_labyrint(2, 4)
    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.run()

