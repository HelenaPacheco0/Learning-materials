a = float(input("Upišite prvi brojnik: "))
b = float(input("Upišite prvi nazivnik: "))
c = float(input("Upišite drugi brojnik: "))
d = float(input("Upišite drugi nazivnik: "))
while a == 0 or b == 0 or c == 0 or d == 0:
    print("Učitane vrijednosti nisu različite od nule.")
    a = float(input("Upišite prvi brojnik: "))
    b = float(input("Upišite prvi nazivnik: "))
    c = float(input("Upišite drugi brojnik: "))
    d = float(input("Upišite drugi nazivnik: "))
broj = a*d
naz = c*b
print('{0:.2f}/{1:.2f} / {2:.2f}/{3:.2f} = {4:.2f}/{5:.2f}'.format(a,b,c,d,broj,naz))

rezu = (a/b) / (c/d)

print("Konačni rezultat je = {:.4f}".format(rezu))
