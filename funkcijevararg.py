#!/usr/bin/env python

"""
Primer: funkcije sa varijabilnim brojem argumenata
Elementi: funkcije i prenos argumenata
"""

def varparfu(*x):
    print(x)
    return

def aritmeticka_sredina(x, *l):
    """ Racuna aritmeticku sredinu 
    ne-nultog broja brojeva """ 
    sum = x 
    for i in l:
        sum += i 
    return sum / (1.0 + len(l))


varparfu()
varparfu(71, "ETF", "sala 309")

print(aritmeticka_sredina(1,2,3))
l=[5,6,7,8]
print(aritmeticka_sredina(*l))

