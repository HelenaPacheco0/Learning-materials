#zadatak 11.
import random

broj = random.randint(20,60)

print(broj)

#zadatak 24.

broj = int(input("Unesi neki broj manji od 100:"))

while broj !=0:
    broj -= 1			#Ako uneseš broj 10, on se u petlji smanjuje za 1 dok ne dođe do 0 (broj -= 1)
    print("#",end=" ")

print()
#zadatak 25.

import string			#Unosi slova engleske abecede - string.ascii_uppercase

for i in string.ascii_uppercase:
    print(i, end=" ")

print()
#zadatak 26.

broj = int(input("Upiši neki broj:"))

print("Parni brojevi u rangu do {} su:".format(broj))

for i in range(2, broj, 2):
    print(i, end=" ")
print(broj)


print("Neparni brojevi u rangu do {} su:".format(broj))

for i in range(1, broj, 2):
    print(i, end=" ")

print()

print("Prvih {0} parnih brojeva su:".format(broj))

for i in range(1, broj):
    print(i+i, end=" ")
print(broj*2)

print("Prvih {} neparnih brojeva su:".format(broj))

for i in range(1,broj):
    print(i+i-1, end=" ")
print(broj*2-1)


#zadatak 27.

print()
print()

broj = int(input("Upiši neki prirodan broj:"))
print()
print("{} - {}".format(broj, broj*broj))
for i in range (broj, 1, -1):    
    broj -= 1     
    print("{} - {}".format(broj, broj*broj))



#zadatak 28.
print()

broj = int(input("Upiši neki broj:"))
broj += 1
a=1
for i in range (1,broj):
    a *= i
print(a)    


#zadatak 29.

n = int(input("Unesite broj objekata:"))
m = int(input("Unesite broj različitih:"))


p=n - m
p += 1      #Pošto se varijabla n (n+=1) mijenja ispred prve petlje potrebno
            #je deklarirati varijablu p za drugu petlju ispred prve petlje jer 
a=1         #tako n ostaje isti broj a ne veći za 1
n += 1
for i in range(1, n): #Za broj 39 iz primjera
    a *= i

b=1
for i in range(1, p):  #Za broj 32 iz primjera
    b *= i

c=1
m+=1
for i in range(1, m):  #Za broj 7 iz primjera
    c *= i
    
rezultat = a // (b*c)

print(rezultat)


#zadatak 30.

import random

broj = int(input("Unesi neki prirodan broj:"))

parni = 0
neparni = 0
for i in range(0, broj):
    br = random.randint(1, 15)
    print(br)
    if(br % 2):
        neparni += br
    else:
        parni += br

print("Zbroj parnih brojeva je: {}".format(parni))
print("Zbroj neparnih brojeva je: {}".format(neparni))
        

#zadatak 31.

broj = int(input("Unesite neki broj:"))

a = 0
for i in range (1, broj):
    if broj % i == 0:
        a += i

if a == broj:
    print("Broj je savršen.")
else:
    print("Broj nije savršen")

#zadatak 32.

broj = int(input("Unesi neki prirodan broj:"))

a = 0
b = 0
broj += 1
for i in range(0, broj):
    i += i
    b = i*i
    a += b
print(a)    


#zadatak 33.

broj = int(input("Unesi neki broj:"))

broj += 1
a=1
for i in range(1, broj):
    i += i - 1
    a *= i
print(a)


#zadatak 34.

a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))

veci_broj = a

if b>a:
    veci_broj = b

najveci_zajednicki = 0

for i in range(1,veci_broj):
    if a % i == 0:
        if b % i == 0:
            if i > najveci_zajednicki:
                 najveci_zajednicki = i

print(najveci_zajednicki)
            
















