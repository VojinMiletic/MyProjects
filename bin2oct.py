#!/usr/bin/env python

"""
Primer: prevodjenje broja u o0bliku stringa iz binarnog u oktalni oblik
Elementi: recnici
"""

prevod = { '000':'0', '001':'1', '010':'2',
           '011':'3', '100':'4', '101':'5',
           '110':'6', '111':'7'} 

def bin2oct(bin_cif): 
    n = len(bin_cif)
    nule = bin_cif.count('0')
    jed = bin_cif.count('1') 
    if nule + jed != n:
        return 'Greška'
    ost = n % 3
    oct_cifre = []
    if ost != 0: 
        oct_cifre.append(prevod[(3-ost)*'0' + bin_cif[0:ost]])
    for i in range(ost, n, 3): 
        oct_cifre.append(prevod[ bin_cif[i:i+3] ])
    return ''.join(oct_cifre)

print(bin2oct('001100010'))
