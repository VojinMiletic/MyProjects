#!/usr/bin/env python

"""
Primer: generisanje prostih brojeva od 2 do n Eratostenovim sitom
Elementi: list comprehensions
"""

import math

def Eratosten_1(n):
    compounds = []
    for i in range(2, math.ceil(n**0.5) + 1):
        for j in range(i*2, n+1, i):
            compounds += [j]
    print(compounds)
    
    primes = []
    for i in range(2, n + 1):
        if not i in compounds:
            primes += [i]
    return primes
        
def Eratosten_2(n):
    compounds = [j for i in range(2, math.ceil(n**0.5) + 1) for j in range(i*2, n+1, i)]
    print(compounds)
    primes = [x for x in range(2, n+1) if x not in compounds]

    return primes
