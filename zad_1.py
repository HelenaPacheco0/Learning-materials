a = int(input("Unesite prvi brojnik: "))
b = int(input("Unesite prvi nazivnik: "))
c = int(input("Unesite drugi brojnik: "))
d = int(input("Unesite drugi nazivnik: "))
while a == 0 or b == 0 or c == 0 or d == 0:
    print("Učitane vrijednosti nisu različite od nule!")
    a = int(input("Unesite prvi brojnik: "))
    b = int(input("Unesite prvi nazivnik: "))
    c = int(input("Unesite drugi brojnik: "))
    d = int(input("Unesite drugi nazivnik: "))

print('{0}/{1} - {2}/{3} = {4}/{5}'.format(a,b,c,d,(a*d - b*c),b*d))
