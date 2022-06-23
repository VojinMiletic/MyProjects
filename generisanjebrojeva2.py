#!/usr/bin/env python

"""
Primer: generisanje nejedinstvenih pseudoslucajnih brojeva u opsegu
Elementi: generisanje pseudoslucajnih brojeva, fajlovi
"""

import random

donja = int(input("Unesite donju granicu: "))
gornja = int(input("Unesite gornju granicu: "))
k = int(input("Unesite broj elemenata: "))
p = int(input("Unesite procenat elemenata koji se ponavlja: "))

brojevi = [random.randint(donja, gornja) for i in range(k - k//p)]
#for i in range(k):
#    brojevi.append(random.randint(donja, gornja))
brojevi.extend(random.sample(brojevi, k//p))
random.shuffle(brojevi)

imefajla = "numbers_" + str(k) + "_nonunique.txt"
f = open(imefajla, "w")
for i in brojevi:
    print(i, end=" ", file=f)
f.close()
