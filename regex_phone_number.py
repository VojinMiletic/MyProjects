#!/usr/bin/env python

"""
Primer: primer uparivanja brojeva telefona razlicitim regularnim izrazima
Elementi: regularni izrazi, findall
"""

import re

telefoni = ['011/1234-567', '011~1234~567', 'telefon: 011/7654-321 drugi telefon: 0111234567', '3218456',
            '011jemojbrtel', '011/1234567890']

print ("prvi slucaj:")
for telefon in telefoni:
    print (re.findall(r'011/\d+', telefon))

print ("drugi slucaj:")
for telefon in telefoni:
    print (re.findall(r'011/?\d+-?\d+', telefon))


print ("treci slucaj:")
for telefon in telefoni:
    print (re.findall(r'011/?\d{4}-?\d{3}', telefon))

print ("cetvrti slucaj:")
for telefon in telefoni:
    print (re.findall(r'(?:011/?)?\d{4}-?\d{3}', telefon))


print ("peti slucaj:")
for telefon in telefoni:
    print (re.findall(r'(?:011/?)?(\d{4}-?\d{3})', telefon))

print ("sesti slucaj:")
for telefon in telefoni:
    print (re.findall(r'(011/?)?(\d{4}-?\d{3})', telefon))

print ("Primer za match:")
mo = re.match(r"(011/)(\d{3})(\d{4})", '011/1234567')
if mo:
    for i in range(0,mo.lastindex+1):
        print (mo.group(i), " pocinje na poziciji ", mo.start(i),", a zavrsava se na poziciji ", mo.end(i))
        print (" nalazi se u opsegu:", mo.span(i))

print ("")
print ("primer za search:")
mo = re.search(r"(011/)(\d{3})(\d{4})", 'ddd011/1234567, 011/9876543')
if mo:
    for i in range(0,mo.lastindex+1):
        print (mo.group(i), " pocinje na poziciji ", mo.start(i),", a zavrsava se na poziciji ", mo.end(i))
        print (" nalazi se u opsegu:", mo.span(i))

print ("")
print ("Primer za finditer:")
zurka = "Mika Geek 011/1234567, Pera Kosac 011-9876543, Metalac Ika 064222-333, zovi i Cicu 322-444, super Iva 064888999"
for s in re.finditer(r'([0-9]{3}[/-]?)(\d+)-?(\d+)', zurka ):
    print (s.group(0), s.group(1))

zurka2 = re.sub(r'([0-9]{3}[/-]?)(\d+)-?(\d+)', '***', zurka)
print(zurka2)
