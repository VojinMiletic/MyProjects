#!/usr/bin/env python

"""
Primer: linearna jednačina a*x+b = 0. Ima resenje ako a!=0, nema ako je a==0
Elementi: grananja u programu, if
"""

a = float(input("Uneti a: "))
b = float(input("Uneti b: "))

if a != 0:
    x = -b / a
    print ("Resenje:", x)
    #print ("Resenje: {:0.2f}".format(x))
else:
    print("Nema jednoznacno resenje")
    if b != 0:
        print("Jednacina nema resenja")
    else:
        print("Jednacina ima beskonacno mnogo resenja - svaki realan broj je resenje")
