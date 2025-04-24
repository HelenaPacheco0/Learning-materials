def ucitaj():
    while True:
        a=int(input('Ucitaj'))
        b=int(input('Ucitaj'))
        if (a%2) and (b%2) and (a<b):
            return a,b
            break
        else:
            print('ucitani krivi brojevi')

def main():
    a,b=ucitaj()
    djelitelj=int(input('Unesi cijeli broj'))
    import sys
    sys.path.append('C:\\...\\moji')
    import Generiraj
    import Ispitaj
    x,y=Generiraj.kreiraj2(a,b,djelitelj)
    print('generirano {} i {}'.format(x,y))

main()
