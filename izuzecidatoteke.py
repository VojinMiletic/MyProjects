#!/usr/bin/env python

"""
Primer: obrada izuzetaka
Elementi: try, except, else
Pokrenuti program bar dva puta da bi se bacio izuzetak.
"""
try:
   # The 'x' mode implies 'w' and raises an `FileExistsError` if the file already exists.
   fh = open("testdat.txt", "x")
   fh.write("Ovo je test rada sa izuzecima!!")
except IOError:
   print ("Ne mogu da pronadjem datoteku ili procitam ili pisem u datoteku!")
else:
   print ("Sadrzaj uspesno upisan")
   fh.close()

try:
   fh = open("testdat.txt", "x")
   try:
       fh.write("Ovo je test rada sa izuzecima!!")
   finally:
       print ("Zatvaram datoteku.")
       fh.close()
except IOError:
   print ("Ne mogu da pronadjem datoteku ili procitam ili pisem u datoteku!")
   

