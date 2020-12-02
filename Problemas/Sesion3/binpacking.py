from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    solucion = []
    espacio_libre_ultimo_contenedor = C
    indice_ultimo_contenedor = 0
    for w in W:
        if w > espacio_libre_ultimo_contenedor:  # NO CABE
            espacio_libre_ultimo_contenedor = C
            indice_ultimo_contenedor += 1
            espacio_libre_ultimo_contenedor -= w
            solucion.append(indice_ultimo_contenedor)
        else:  # SI CABE
            espacio_libre_ultimo_contenedor -= w
            solucion.append(indice_ultimo_contenedor)
        # Se puede quitar el else ya que las dos lineas estan en el if
    return solucion


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    solucion = []
    espacio_libre_en_contenedores = [C]
    for w in W:
        insertado = False
        # MIRA SI CABE EN LO QUE TENEMOS
        for nc in range(len(espacio_libre_en_contenedores)):  # nc = numero de contenedores
            if w <= espacio_libre_en_contenedores[nc]:
                solucion.append(nc)
                espacio_libre_en_contenedores[nc] -= w
                insertado = True
                break
        if not insertado:  # NO CABE EN LO QUE TENEMOS
            solucion.append(len(espacio_libre_en_contenedores))
            espacio_libre_en_contenedores.append(C - w)
    return solucion


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    solucion = [-1] * len(W)
    indices_ordenados = sorted(range(len(W)), key=lambda ind: - W[ind])
    espacio_libre_en_contenedores = [C]
    for i in indices_ordenados:
        w = W[i]
        insertado = False
        # MIRA SI CABE EN LO QUE TENEMOS
        for nc in range(len(espacio_libre_en_contenedores)):  # nc = numero de contenedores
            if w <= espacio_libre_en_contenedores[nc]:  # Si cabe
                solucion[i] = nc
                espacio_libre_en_contenedores[nc] -= w
                insertado = True
                break
        if not insertado:  # NO CABE EN LO QUE TENEMOS
            solucion[i] = len(espacio_libre_en_contenedores)
            espacio_libre_en_contenedores.append(C - w)
    return solucion


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10  # Lista de objetos en peso, y la capacidad de cada Camion
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
