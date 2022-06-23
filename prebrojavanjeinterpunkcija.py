#!/usr/bin/env python

"""
Primer: prebrojavanje znakova interpunkcije u stringu
Elementi: stringovi, regularni izrazi
"""

def punct_count1(line):
    punct = ['.', ',', ';', ':', '!', '?']
    num_punct = 0
    for p in punct:
        if p in line:
            num_punct += line.count(p)
    return num_punct

def punct_count2(line):
    punct = ['.', ',', ';', ':', '!', '?']
    return len([l for l in line if l in punct])

import re
def punct_count3(line):
    punct = r"[.,;:!?]"
    return len(re.findall(punct, line))

line = """To be, or not to be, that is the question:
Whether tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them."""

print(punct_count1(line))
print(punct_count2(line))
print(punct_count3(line))

