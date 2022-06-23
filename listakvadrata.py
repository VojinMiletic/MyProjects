#!/usr/bin/env python

"""
Primer: formiranje liste kvadrata
Elementi: list comprehensions
"""

def kvadrati_1(n):
    kvadrati = []
    for i in range (n+1):
        kvadrati.append(i*i)
    return kvadrati

def kvadrati_2(n):
    return [i*i for i in range(n+1)]

def kvadrati_3(n):
    return [i*i for i in range(n+1) \
            if i % 3 == 0]

def aps_vred(arr):
    return [i if i > 0 else -i for i in arr]

def matrica(m, n):
    return [[i for i in range(n)] for _ in range(m)]

print(kvadrati_1(10))
print(kvadrati_2(10))

