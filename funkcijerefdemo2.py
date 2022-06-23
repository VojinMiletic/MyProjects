#!/usr/bin/env python

"""
Primer: prenos po vrednosti za nepromenljive tipove
Elementi: funkcije i prenost argumenata
"""

def nema_promene(gradovi):
    print(gradovi) 
    gradovi = gradovi + ["Rim", "London"]
    print(gradovi)

def ima_promene(gradovi):
    print(gradovi) 
    gradovi += ["Rim", "London"]
    print(gradovi)

def bez_promene(gradovi):
    print(gradovi) 
    gradovi += ["Rim", "London"]
    print(gradovi)


lokacije = ["Beograd", "Novi Sad", "Niš"]
nema_promene(lokacije)
print(lokacije)
ima_promene(lokacije)
print(lokacije)
bez_promene(lokacije[:])
print(lokacije)
