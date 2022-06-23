#!/usr/bin/env python

"""
Primer: provera da li je uneti ceo broj prost  
Elementi: for petlja, else grana petlje
"""
import math
n = int(input("Unesite broj: "))
for i in range(2, math.ceil(n**0.5) + 1):
    if n % i == 0:
        print("Broj nije prost!")
        break
else:
    print("Broj je prost!")
