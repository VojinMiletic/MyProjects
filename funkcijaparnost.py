#!/usr/bin/env python

"""
Primer: primer funkcije za odredjivanje parnosti
Elementi: funkcije
"""

def parnost( i ):
    """
    Vraca True ako je ceo broj i paran, 
    a False ako je neparan
    """
    print("unutar funkcije parnost")
    return i%2 == 0

res = parnost (3)
print(res)
