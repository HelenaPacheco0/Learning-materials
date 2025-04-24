global broj
broj = 100
veciOdSto = int(input("Unesite troznamenkasti broj veći od 100:"))

def generirajBroj(veciOdSto):
    if veciOdSto < 101 or veciOdSto > 999:
        print("Broj ne valja")
        return 150
    else:
        import random
        genBroj = random.randint(broj, veciOdSto)
        print("Generiran je slučajni broj: {}".format(genBroj))
        return genBroj

def vratiZbroj(veciOdSto):
    if veciOdSto > 100 and veciOdSto < 999:
        prvaZnamenka = veciOdSto % 10
        drugaZnamenka = (veciOdSto // 10) % 10
        trecaZnamenka = veciOdSto //100
        return prvaZnamenka + drugaZnamenka + trecaZnamenka

    
