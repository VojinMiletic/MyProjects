#!/usr/bin/env python

"""
Primer: generisanje podskupova
Elementi: skupovi
"""

import itertools
def podskupovi(s, n): 
    return [set(i) \
    for i in itertools.combinations(s, n)]

s = {1, 2, 3, 4} 
n = 3
print(podskupovi(s, n))
