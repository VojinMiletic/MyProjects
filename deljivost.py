#!/usr/bin/env python

"""
Primer: odredjivanje ocene za zadati broj poena
Elementi: grananja u programu, visestruki ugnezdeni if
"""

num = int(input("Unesite broj: "))
if num % 2 == 0:
   if num % 3 == 0:
      print("Deljiv sa 2 i 3")
   else:
      print("Deljiv sa 2, nije deljiv sa 3")
else:
   if num % 3 == 0:
      print("Nije deljiv sa 2, deljiv sa 3")
   else:
      print("Nije deljiv sa 2, nije deljiv sa 3")
