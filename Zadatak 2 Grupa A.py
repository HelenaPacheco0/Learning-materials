kraj=False
r=0
while not kraj:
    a=int(input('Upiši troznamenkasti broj: '))
    if a<=99 and a>=1000:
        print('Nisi upisao troznamenkasti broj')
    else:
        k=a//2
        z=k
        if(a%2!=0):
            kraj=True
            print('Ne postoji zbroj dvaju neparnih brojeva')
        else:
            k=z-1
            z=z+1
            d=k+z
            print('Zbroj dvaju neparnih brojeva:{}+{}={}'.format(k,z,d))
            kraj=True
        
    
    
