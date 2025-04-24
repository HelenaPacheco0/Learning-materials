def Ucitaj():
    while True:
        m=int(input('Unesi broj'))
        n=int(input('Unesi broj'))
        if m!=n and m<n:
            return m,n
        else:
            print('Ucitaj krivi brojevi')

def main():
    global g1
    g1=100
    import sys
    sys.path.append('C:\\...\\moji')
    import Kreiraj
    import Evaluiraj
    a,b=Ucitaj()
    djelitelj=int(input('Ucitaj cijeli broj'))
    x,y=Kreiraj.kreirajDva(a,b,djelitelj)
    print('Generirano {} i {}'.format(x,y))
    k1=Evaluiraj.kreiraj(x)
    k2=Evaluiraj.kreiraj(y)
    print('Kreirani brojevi su {} i {}'.format(k1,k2))
    razlika=k1-k2
    if razlika<0:
        razlika*=-1
    print('Razlika je {}'.format(razlika))
    provjera=Evaluiraj.provjeri(razlika)
    if provjera:
        print('Razlika je neparan broj')
    else:
        print('Razlika je paran broj')
    broj1,broj2=Ucitaj()
    if razlika<g1:
        if broj1>broj2:
            print('{}--{}'.format(broj1,broj2))
        else:
            print('{}--{}'.format(broj2,broj1))
    else:
        if broj1<broj2:
            print('{}--{}'.format(broj1,broj2))
        else:
            print('{}--{}'.format(broj2,broj1))
        
main()
