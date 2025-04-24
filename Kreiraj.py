def kreirajDva(m,n,k):
    import random
    while True:
        a=random.randint(m,n)
        b=random.randint(m,n)
        if a%k and b%k:
            return a,b
        else:
            print('kreirajDva krivi brojevi')

global g1
g1=100
        
