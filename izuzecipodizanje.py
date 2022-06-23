#!/usr/bin/env python

"""
Primer: obrada izuzetaka
Elementi: raise
"""
import math

def korenovanje( broj ):
   if broj <0:
      raise Exception("Negativan broj!", broj)
   return math.sqrt(broj)

try:
   k = korenovanje(-10)
   print ("koren = ",k)
except Exception as e:
   print ("Problem sa argumentom", e)
