#!/usr/bin/env python

"""
Primer: Euklidov algoritam za odredjivanje NZD(m,n), m > n
Elementi: while petlja
"""

m = int(input("Unesite m: "))
n = int(input("Unesite n: "))

m, n = (m, n) if m > n else (n, m)

a, b = m, n
r = a % b
while r > 0:
    a = b
    b = r
    r = a % b
    
nzd = b
print("nZD(", m, ",", n, ")=", nzd)
