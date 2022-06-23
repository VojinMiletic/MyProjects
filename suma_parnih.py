#!/usr/bin/env python

"""
Primer: suma parnih nenegativnih brojeva sa ulaza, za negativan ulaz se napusta progra  
Elementi: while petlja, continue
"""

suma = 0
while True:
    broj = int(input("Unesite broj: "))
    if broj < 0:
        break
    elif broj % 2:
        continue
    suma += broj
print("Suma = ", suma)
