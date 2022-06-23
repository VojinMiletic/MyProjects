#!/usr/bin/env python

"""
Primer:  ping-pong, indirektna rekurzija
Elementi: rekurzivne funkcije
"""

def ping(i):
    if i>0:
        return pong(i-1)
    else:
        return "0"
def pong(i):
    if i>0:
       return ping(i-1)
    else:
       return "1"

print(ping(3))
print(ping(4))
print(pong(3))
print(pong(4))
