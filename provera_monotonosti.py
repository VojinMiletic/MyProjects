#!/usr/bin/env python

"""
Primer: provera monotonosti unosa 
Elementi: while petlja, break
"""

broj = -float("inf")
while True:
    unos = float(input("Unesite broj: "))
    if broj < unos:
        print("Sekvenca je rastuca!")
    else:
        print("Uneti broj prekida rastucu sekvencu!")
        break
    broj = unos
print("Kraj programa!")
    
    

