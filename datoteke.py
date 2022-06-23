
"""
Primer: citanje datoteke
Elementi: otvaranje, citanje u razlicitim rezimima, pisanje
"""

f = open('C:\\Users\\markom\\Dropbox\\Programiranje\\P1\\Python\\Predavanja\\Primeri\\test.txt')

for line in f:
    print(line, end='')

print()

f.seek(0)

for line in f:
    for c in line:
        print(c, end='')

f.close()

print()

with open('C:\\Users\\markom\\Dropbox\\Programiranje\\P1\\Python\\Predavanja\\Primeri\\test.txt')\
as f:
    for line in f:
        print(line, end='')

with open('C:\\Users\\markom\\Dropbox\\Programiranje\\P1\\Python\\Predavanja\\Primeri\\test2.txt', 'w')\
as f:
    year = 2000
    print("Hi there year", year, "!", file=f)
    print("Python is a great language!", file=f)
    
with open('C:\\Users\\markom\\Dropbox\\Programiranje\\P1\\Python\\Predavanja\\Primeri\\test3.txt', 'w')\
as f:
    year = 2000
    f.write("Hi there year " + str(year) + " !\n")
    f.write("Python is a great language!\n")

numbers = [1.22, 123.23, 3E-2]
num_out = open('num_out.txt', 'w')
for num in numbers:
    num_out.write("{}\n".format(num))
num_out.close()


num_out = open('num_out.txt', 'w')
num_out.writelines(["{}\n".format(num) for num in numbers])
num_out.close()

