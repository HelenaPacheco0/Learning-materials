def uvjet(M,N):
    if abs(M-N) >= 99 and M > 2:
        return True
    else:
        return False

def ispisi(M,N):
    a,b = 0, 0
    if M > N:
        a = N
        b = M
    else:
        a = M
        b = N
    for a in range (b + 1):
        if a % 5 == 0 and a % 7 != 0:
            print(a,end='')

def main():
    flag = True

    while flag:
        x = int(input('Unesi prvi prirodan broj: '))
        y = int(input('Unesi drugi prirodan broj: '))

        flag = uvjet(x,y)

        if flag:
            flag = False
        else:
            print('Učitani brojevi ne ispunjavaju uvjet.')
            flag = True

    ispis(x,y)

    return

if __name__ == '__main__':
    main()
