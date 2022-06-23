#!/usr/bin/env python

"""
Primer:  prostor imena
Elementi: funkcije
"""

def spoljna_funkcija():
    a = 20
    def unutrasnja_funkcija():
        a = 30
        print('a =',a)
    unutrasnja_funkcija()
    print('a =',a)

def spoljna_funkcija2():
    global b
    b = 20
    def unutrasnja_funkcija():
        global b
        b = 30
        print('b =',b)
    unutrasnja_funkcija()
    print('b =',b)

a = 10
spoljna_funkcija()
print('a =',a)

b = 10
spoljna_funkcija2()
print('b =',b)
