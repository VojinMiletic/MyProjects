#!/usr/bin/env python

"""
Primer: prenos argumenata drugim redosledom
Elementi: funkcije i prenost argumenata
"""

def osoba_ispis(ime, starost=35):
    print("Ime: ",ime) 
    print("Starost: ",starost)
    return
osoba_ispis(starost=21, ime="Petar")
osoba_ispis("Lana", 19)
