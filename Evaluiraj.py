def kreiraj(a):
    x=a%10
    if x==0:
        x=1
    zadnja1=x*10+(x-1)
    zadnja2=zadnja1*10+(x-2)
    return zadnja2

def provjeri(a):
    if a%2:
        return True
    else:
        return False
