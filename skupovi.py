#!/usr/bin/env python

"""
Primer: http://e.raspored.rs/mat/5/Skupovi.pdf, brojevi od 0 do 200
U skupu A su neparni brojevi
U skupu C su parni brojevi
U skupu B su brojevi deljivi sa 3
U skupu D su brojevi deljivi sa 7
Elementi: skupovi
"""

A = set()
B = set()
C = set()
D = set()
for n in range (1,201): 
    if not n%2:
       A.add(n)
    else:
       C.add(n)
    if not n%3:
       B.add(n)
    if not n%7:
          D.add(n)

X = ((A | B | C) & D) - B
Y = ((A & D) | (C & D)) - B
Z = (D - B) & (A | C)

print(len(X), len(Y), len(Z))
if X==Y==Z:
   print ("Skupovi X, Y i Z su jednaki")
print ("Skupovi X, Y i Z sadrze: ", X)
