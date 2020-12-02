#*****************  EL PROBLEMA DEL BUSCA PICO *****************************************
#      - REDUCE Y VENCERAS -
#
#
#
#
##***************************************************************************************
from typing import *

def busca_pico(a: List[int]) -> Optional[int]:  #Ó devuelve int o None
    def rec(b: int, e: int) -> Optional[int]:
        num_elem = e-b
        if num_elem==0:         #is_simple
            return None         #trivial_solution
        elif num_elem==1:       #is_simple
            return b            #trivial_solution
        elif num_elem==2:       #is_simple
            if a[b] <= a[b+1]:
                return b+1
        else:                   #decrease
            h = (b+e)//2
            if a[h] <= a[h+1]:
                return rec(h+1, e)     #recursividiad
            else:
                return rec(b, h+1)      #recursividiad

    return rec(0, len(a))

if __name__ == '__main__':
    #    0  1  2 3  4  5 6
    v= [10,20,15,2,23,90,67]
    print(busca_pico(v))