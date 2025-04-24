#zadatak 1

def kalkulator (a,b):  #funkcija uzima dva argumenta
    zbroj = a + b      #i vraća njihov zbroj, što znači da kada ćemo koristiti tu
    return zbroj       #funkciju, morat ćemo joj dati dva argumenta- dva broja koja će zbrojiti


while True:         #while True ponavlja radnju neograničen broj puta
    prvi = int(input("Unesite prvi broj:"))
    drugi = int(input("Unesite drugi broj:"))

    print(kalkulator(prvi, drugi))   #ispis 
                                     #zovemo funkciju "kalkulator" i kao
                                     #argumente joj šaljemo "prvi" i "drugi" -dva broja koja ta funkcija mora zbrojiti


#zadatak 2

def zbrojBrojeva (a):   #funkcija uzima jedan argument
    b=0                 # i ispisuje zbroj svih brojeva od nule do broja iz argumenta ("+1" uključuje i taj broj)
    for i in range (0, a+1):
        b += i                   #kad budemo koristili tu funkciju, moramo joj dati jedan argument- neki broj            
    return b                     #koji koristi za zadani broj u petlji 


broj = int(input("Unesite neki broj:"))
print(zbrojBrojeva(broj))       #ispis
                                #zovemo funkciju "zbrojBrojeva" i kao
                                #argument koristimo "broj"

#zadatak 3

#rezultat binomne jednadžbe mora biti pozitivan ili nula da bi nultočke bile realne (valjda (: )

def calc (a,b,c):               #funkcija "calc" prima tri argumenta i koristi ih za izračun vrijednosti funkcije
    rezultat = b*b - 4*a*c
    if rezultat >= 0:
        return True             #Ako je uvjet točan vraca True. U suprotnom vraca False
    else:
        return False

prvi = int(input("Upišite koeficijent a:"))
drugi = int(input("Upišite koeficijent b:"))
treci = int(input("Upišite koeficijent c:"))

print(calc (prvi, drugi, treci))    #U ispisu zovemo funkciju "calc" i dajemo joj tri broja kao argumente

#zadatak 4

def zbrojZnamenki (br):         #funkcija zbrojZnamenki vraća zbroj svih znamenki nekog broja
    suma = 0
    while br:               #while br ---- petlja radi za svaki broj od zadanog broja---recimo 527---
        suma += br % 10                      #-1.korak---suma = suma + 7 = 7 ---( 7 je ostatak kad se 527 dijeli sa 10)---
        br //= 10                            #- .korak---527 cjelobrojno sa 10 daje 52---broj 52 ulazi u sljedeći krug petlje
    return suma                              #-2.korak---suma = 7 + 2 = 9 ---(2 je ostatak kad se 52 dijeli sa 10)
                                             #- .korak---52 cjelobrojno sa 10 daje 5---sada broj 5 ulazi u sljedeći krug petlje
broj = int(input("Unesi neki broj:"))        #-3.korak---suma = 7 + 2 + 5 = 14--(5 je ostatak kad se 5 dijeli sa 10 (0.5)---
print(zbrojZnamenki(broj))                   #-x.korak---5 cjelobrojno sa 10 daje 0---nula daje False i petlja se prekida
                                        #Koliko broj ima znamenaka, toliko bi petlja odradila koraka jer svaki put se dijeli sa deset i tako se oduzima jedna znamenka za sljedeći korak 

#zadatak 5

def savrsen (c):            #funkcija "savrsen" trazi savrsene brojeve u rangu od 1 do zadanog broja
    zbrojDjelitelja = 0
    for i in range(1,c):
        if c%i == 0:                    #Program prolazi kroz petlju za svaki "i" -  1-2-3-4-...-do zadanog broja
            zbrojDjelitelja += i        #i provjerava da li je zadani broj djeljiv sa "i". Ako je tada ga zbraja u varijablu "zbrojDjelitelja"
    if zbrojDjelitelja == c:
        return True             #Ako zbroj djelitelja nije jednak zadanom broju tada taj broj nije savršen pa program vraća False...U suprotnom vraća True
    else:
        return False

def nSavrsenih(d):     #druga funkcija ispisuje sve savrsene brojeve od 1 do zadanog broja pri cemu koristi prethodnu funkciju
    brojac = 0          #za provjeru da li je "i" iz petlje for savrsen. Ako jest, tada ga ispisuje te zbraja u varijablu brojac koja
    for i in range(1, d):   #sluzi za sljedeci if blok koji provjerava da li je bilo savrsenih brojeva. Ako nije, ispisuje da nije.
        if savrsen(i) == True:
            brojac += 1
            print(i)
    if brojac == 0:
        print("Ne postoji ni jedan savršeni broj u rangu od 1 do {}.".format(d))

broj = int(input("Unesi neki broj:"))

nSavrsenih(broj)  #ovaj put pozivamo metodu izvan funkcije "print" zato što ta metoda kao rezultat u sebi već ima funkciju "print(i)"
                  #Kada bi pozvali tu funkciju unutar funkcije "print" zadnja vrijednost u ispisu bi nam bila "None" pa bi to bio višak ispisa
