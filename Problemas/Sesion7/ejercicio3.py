#*****************  EL PROBLEMA DEL BUSCA PICO *****************************************
#      - DIVIDE Y VENCERAS -
#
#
#
#
##***************************************************************************************
from typing import *


def suma_max(a: List[int]) -> Tuple[int, int, int]:
    def rec(b: int, e: int) -> Tuple[int, int, int]:
        num_elem = e-b
        if num_elem==0:             #is simple
            return 0, 0, 0
        if num_elem == 1:           #is_simple
            return a[b], b, b+1   #trivial_solution
        else:
            h = (b+e)//2
            mejor_izq=rec(b,h)
            mejor_der=rec(h,e)
            mejor_centro = ... #TODO

            return max(mejor_izq, mejor_der, mejor_centro)

    return rec(0, len(a))


if __name__ == '__main__':
    #    0   1  2   3  4  5   6  7   8
    v= [-10, 6, 4, -2, 2, 8, -9, 5, -4]
    print(suma_max(v))