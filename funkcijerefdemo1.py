#!/usr/bin/env python

"""
Primer: prenos po vrednosti za nepromenljive tipove
Elementi: funkcije i prenost argumenata
"""

def ref_demo(x): 
    print("x=",x," id=",id(x)) 
    x=42
    print("x=",x," id=",id(x))

y = 12
print("y=",y," id=",id(y)) 
ref_demo(y)
print("y=",y," id=",id(y)) 
