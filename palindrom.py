#!/usr/bin/env python

"""
Primer: provera da li je string palindrom i za sve podstringove
Elementi: stringovi, rekurzija
"""

def palindromI(tekst):
    ''' da li je tekst palindorm '''
    n = len(tekst)
    limit = n//2
    for i in range(limit):
        if tekst[i] != tekst[-i-1]:
            return False
    return True

def palindromR(tekst):
    ''' da li je tekst palindorm '''
    if tekst == '': 
        return True 
    elif tekst[0] != tekst[-1]:
        return False
    else: 
        return palindromR(tekst[1 : -1])

tekst = input('tekst? ')
n = len(tekst)
for duzina in range(n, 0, -1):
    for pocetak in range(0, n-duzina+1):
        podtekst = tekst[pocetak : \
                         pocetak+duzina]
        if palindromR(podtekst):
            print(podtekst)
