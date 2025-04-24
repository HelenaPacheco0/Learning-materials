a = int(input("Unesite prirodan parni broj: "))
while a % 2 != 0 and a <= 2:
    print("Učitani broj ne ispunjava uvjete.")
    a = int(input("Unesite prirodan parni broj: "))
br = 0
while br < 100:
    for i in range(1,100):
        if i // 1 == 1 and i % i == 0:
            for j in range(1,100):
                if j // 1 == j and j % j == 0:
                    if a == i + j:
                        print("Broj {} je zbroj prostih brojeva {} i {}".format(a,i,j))
                        br += 1
        else:
            break

print("Bilo je {} para prostih brojeva.".format(br))
