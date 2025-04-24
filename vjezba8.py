def fun1(broj):
    lista = []
    while broj:
        rijec = str(input("Upišite riječ: "))
        if rijec in lista:
            print("Ponovite unos!")
            continue
        else:
            lista.append(rijec)
            broj -= 1
        if rijec == "":
            lista.pop()
            print("Ponovite unos!")
            broj += 1
    return lista

            
def fun2(lista):
    results = []
    for i in range(0, len(lista)):      #petlja kroz listu -  za svaku riječ
        rijec = lista[i]            
        rijec = rijec.lower()
        indexRijeci = i
        
        brojPalindroma = 0
        b = 0
        for i in range(0, len(rijec)):      #petlja kroz riječ - za svaki znak
            dio = rijec[0: i + 1]
            if dio == dio[::-1] and len(dio) > 1:
                brojPalindroma += 1
                b += 1
                results.append(dio)
                if b == 2:
                    b -= 1
                    results.pop()
                    results.pop()
                    results.append(dio)
        if brojPalindroma == 0:
            results.append(rijec[0])
    return results

def main():
    lista_rijeci = []
    lista_palindroma = []
    broj = int(input("Koliko riječi? "))
    lista_rijeci = fun1(broj)                   #lista riječi
    lista_palindroma = fun2(lista_rijeci)       #lista palindroma
    print("Lista riječi:" , lista_rijeci)
    print("Lista palindroma:" ,lista_palindroma)

    minPal = []
    for i in range(0, len(lista_palindroma)):
        rijec = lista_palindroma[i]
        if len(rijec) >= 2:
            minPal.append(lista_palindroma[i])      #filtrirana lista palindroma

    minimum = len(min(minPal, key=len))
               
    print("Minimalni broj znakova je ", minimum)

    index = 0
    for x, y in enumerate(minPal):
        if len(y) == minimum:
            index = x
            
            
    print("Minimalni palindrom je na indeksu {} u listi palindroma.".format(index))

if __name__ == "__main__":
    main()
    
