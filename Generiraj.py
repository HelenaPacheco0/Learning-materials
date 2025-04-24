def kreiraj2(m,n,k):
    global gg
    gg=200
    import random
    while True:
        a=random.randint(m,n)
        b=random.randint(m,n)
        if not a%k and not b%k:
            return a,b
        else:
            print('kreiraj2 krivi brojevi')
    
