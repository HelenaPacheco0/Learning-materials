#zadatak drugi za Helenu

a = int(input("Unesite broj:"))                 # za broj 20

for x in range(a , 0 , -1):                    #petlja for koja ispisuje jedan po jedan redak, umanjuje broj a, te ga ispisuje za svaki red
    print("Za broj {} :".format(x), end = " ") #end se stavlja da bi se brojevi ispisali u redu a ne u stupcu
    for y in range (2 , x+1, 2):               #kada prva for petlja ispiše "Za broj: 20" , tada druga petlja ispisuje sve parne brojeve do tog broja. (2 , x+1, 2)
        print(y , end = " ")
    print()                                 #nakon što druga petlja završi sa ispisom, program ide dalje i pomoću funkcije print() prelazi u novi redak.
                                            # tada se radnja ponavlja. Prva petlja nastavlja i ispisuje "Za broj :19", a druga petlja ispisuje sve parne brojeve do 19
                                            # itd...


#zadatak prvi za Helenu

    #Program koji unosi dva broja i jedno slovo (p ili m)
    #Ako je slovo p onda ide prvi potencija drugi, a ako je m onda ide prvi modulo drugi.
    #Ako je drugi nula onda ispisuje da ne može računati modulo

a = int(input("Unesite prvi broj:"))
b = int(input("Unesite drugi broj:"))
c = str(input("Unesite slovo m ili p:"))


if b == 0 and c == "m":
    print("Helena ne želi modulo sa nulom. ")
    
elif c == "p" or c == "m" and b != 0:
    print("Prvi broj je {}".format(a))
    print("Drugi broj je {}".format(b))
    print("Slovo je: {}".format(c))
    if c == "p":
        print("{0} {1} {2} = {3}".format(a,"**",b, a**b))
    else:
        print("{0} {1} {2} = {3}".format(a,"%",b, a%b))
else:
    print("Ne valja znak.")

        
