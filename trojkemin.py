#!/usr/bin/env python

"""
Primer: pronalazenje svih troclanih podnizova koji sadrze minimalni element celobrojne liste 
Elementi: petlje, liste
"""
n = int(input("Unesite broj elemenata liste: "))
lista = []
for i in range(n):
    lista.append(int(input()))
minimum = min(lista)
rezultat = []
for i in range(len(lista) - 2):
    trojka = lista[i:i+3]
    if minimum not in trojka:
        continue
    rezultat.append(trojka)
print(rezultat)

