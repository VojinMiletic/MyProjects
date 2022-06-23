#!/usr/bin/env python

"""
Primer: generisanje jedinstvenih pseudoslucajnih brojeva u opsegu
Elementi: generisanje pseudoslucajnih brojeva, fajlovi
"""

import random

donja = int(input("Unesite donju granicu: "))
gornja = int(input("Unesite gornju granicu: "))
k = int(input("Unesite broj elemenata: "))

random.seed()
brojevi = random.sample(range(donja, gornja + 1), k)

imefajla = "numbers_" + str(k) + "_unique.txt"
f = open(imefajla, "w")
for i in brojevi:
    print(i, end=" ", file=f)
f.close()
