#!/usr/bin/env python

"""
Primer: konverzija temperature
Elementi: asertacije, izuzeci
"""

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Hladnije od apsolutne nule!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
