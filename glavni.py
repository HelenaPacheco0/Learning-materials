import sys

sys.path.append("brojeviModul.py")  #relativna putanja kad su oba .py fajla na desktopu

import brojeviModul

def vrati(a, b, c):
    global br
    br = 10
    a += br
    b += br
    c += br
    return min(a , b, c)

def main():

    prviBroj = int(input("Unesite prvi broj: "))
    drugiBroj = int(input("Unesite drugi broj: "))
    treciBroj = int(input("Unesite treci broj: "))

    genPrva = brojeviModul.generirajBroj(prviBroj)
    genDruga = brojeviModul.generirajBroj(drugiBroj)
    genTreca = brojeviModul.generirajBroj(treciBroj)

    vratiPrvi = brojeviModul.vratiZbroj(genPrva)
    vratiDrugi = brojeviModul.vratiZbroj(genDruga)
    vratiTreci = brojeviModul.vratiZbroj(genTreca)

    minimalnaVrijednost = vrati(vratiPrvi, vratiDrugi, vratiTreci)

    print("Najmanja vracena vrijednost je: {}.".format(minimalnaVrijednost))

if __name__ == "__main__":
    main()
