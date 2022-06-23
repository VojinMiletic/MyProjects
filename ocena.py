#!/usr/bin/env python

"""
Primer: odredjivanje ocene za zadati broj poena
Elementi: grananja u programu, visestruki if
"""

print("Odredjivanje ocene na Programiranju 1!")
poeni = float(input("Unesite broj poena:"))

if poeni > 90:
    ocena = 10
elif poeni > 80:
    ocena = 9
elif poeni > 70:
    ocena = 8
elif poeni > 60:
    ocena = 7
elif poeni > 50:
    ocena = 6
else:
    ocena = 5

print("Dobili ste ocenu:", ocena)

"""
Primer: ispisuje da li je student polozio ispit na osnovu ocene
Elementi: koriscenjem if naredbe
"""

if ocena > 5:
    poruka = "Da!"
else:
    poruka = "Ne, pokusajte ponovo!"
print("Polozio:", poruka)

"""
Primer: ispisuje da li je student polozio ispit na osnovu ocene
Elementi: koriscenjem uslovnog izraza naredbe
"""
poruka = "Da!" if ocena > 5 \
          else "Ne, pokusajte ponovo!"
print("Polozio:", poruka)
