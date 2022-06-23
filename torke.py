#!/usr/bin/env python

"""
Primer: vracanje rezultata funkcije u obliku torke
Elementi: torke
"""

def analiza (tekst, rec):
    x=tekst.count(rec)
    y=tekst.find(rec)
    z=tekst.rfind(rec)
    return x,y,z
tekst='ANA VOLI MILOVANA'
rec='ANA'
a,b,c = analiza(tekst, rec)
print (a,b,c)
