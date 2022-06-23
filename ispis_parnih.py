#!/usr/bin/env python

"""
Primer: ispisivanje sume svih parnih brojeva u zadatom opsegu 1..n 
Elementi: for petlja
"""

n = int(input("Unesi n: "));
suma = 0
for i in range(1, n+1):
    #print(i if i % 2 == 0 else '', end=' ')
    suma += i if i % 2 == 0 else 0
print(suma)

suma = 0
for i in range(2, n+1, 2):
    suma += i
print(suma)
