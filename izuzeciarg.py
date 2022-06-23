#!/usr/bin/env python

"""
Primer: obrada izuzetaka
Elementi: try, except, else
Pokrenuti program bar dva puta da bi se bacio izuzetak.
"""

def konvertuj(var):
   try:
      return int(var)
   except ValueError as Arg:
      print ("Argument funkcije nije broj\n", Arg)

konvertuj("abc")
