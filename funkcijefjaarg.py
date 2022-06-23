#!/usr/bin/env python

"""
Primer: funkcije funkcijom kao argumentom
Elementi: funkcije i prenos argumenata
"""

def funkcija(fnc,arg):
    """ Argument funkcije je druga funkcija 
    fnc, dok je arg numericki argument """ 
    x=fnc(arg) 
    return x
    
def f1(arg):
    return arg+1
 
def f2(arg):
    return arg-1

print(funkcija(f1,5))
print(funkcija(f2,5))
import math
print(funkcija(math.factorial,4))
print(funkcija(math.sqrt,100))
