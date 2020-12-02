#*****************  EL PROBLEMA DEL PUNTO FIJO  *****************************************
#      - REDUCE Y VENCERAS -
#
#     h=(b+e)//2   (begin y end)  El end tiene que apuntar al que va despues del ultimo
#     un vector de 0 al 7 elementos, e=8, e= len(a)
#
##***************************************************************************************
from typing import *

def punto_fijo(a: List[int]) -> Optional[int]:  #Ó devuelve int o None
    def rec(b: int, e: int) -> Optional[int]:
        num_elem = e-b
        if num_elem==0:         #is_simple
            return None         #trivial_solution
        elif num_elem==1:       #is_simple
            if a[b] == b:       #trivial_solution
                return b
        else:                   #decrease
            h = (b+e)//2
            if a[h] < h:
                return rec(h,e)       #recursividiad
            elif a[h]>h:
                return rec(b,h)     #recursividiad
            else:
                return h

    return rec(0, len(a))

def punto_fijo_while(a: List[int]) -> Optional[int]:  #Ó devuelve int o None
    b=0
    e=len(a)
    while e-b>1:
        h= (b+e)//2
        if a[h]<h:
            b=h
        elif a[h] >h:
            e = h
        else:
            return h

    if e-b == 0:
        return None
    if e-b == 1:
        if a[b] == b:
            return b
    return None

if __name__ == '__main__':
    v= [-10, -5, 1, 3, 10]
    print(punto_fijo(v))
    print(punto_fijo_while(v))