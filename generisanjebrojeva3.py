#!/usr/bin/env python

"""
Primer: generisanje nejedinstvenih pseudoslucajnih brojeva u opsegu normalnom raspodelom
Elementi: generisanje pseudoslucajnih brojeva, fajlovi
"""

import random

mu = int(input("Unesite srednju vrednost: "))
sd = int(input("Unesite standardnu devijaciju: "))
k = int(input("Unesite broj elemenata: "))

brojevi = [int(random.normalvariate(mu, sd)) for i in range(k)]

imefajla = "numbers_" + str(k) + "_normal.txt"
f = open(imefajla, "w")
for i in brojevi:
    print(i, end=" ", file=f)
f.close()
