#!/usr/bin/env python

"""
Primer:  racuanje faktorijela
Elementi: rekurzivne funkcije
"""

def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
