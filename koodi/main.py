"""Mooduli sisältää ohjelman päämetodin"""

from tietorakenteet.pulma import Pulma
from algoritmit.ratkaistavissa import on_ratkaistavissa
from algoritmit.generoi import generoi_ratkaistava_pulma
from algoritmit.ratkaisija import IDAStar


def main():
    """Ohjelman päämetodi"""

    info = """Komenntot:
        q = lopettaa ohjelman
        1 = luo annetun levyisen pulman
        2 = yrittää luoda pulman annetusta listasta lukuja"""

    print(info)

    while True:
        komento = input('Komento: ')
        if komento == 'q':
            break

        if komento == '1':
            koko = int(input('Koko: '))
            pulma = generoi_ratkaistava_pulma(koko)
            pulma.tulosta()
            ratkaisija = IDAStar()
            liikkeet = ratkaisija.ratkaise(pulma)
            __tulosta_ratkaisu(pulma, liikkeet)

        elif komento == '2':
            lista = input('Lista: ')
            lista = lista.strip()
            lista = lista.split(' ')
            lista = list(map(int, lista))
            pulma = Pulma(tuple(lista))
            pulma.tulosta()
            if on_ratkaistavissa(pulma):
                ratkaisija = IDAStar()
                liikkeet = ratkaisija.ratkaise(pulma)
                __tulosta_ratkaisu(pulma, liikkeet)
            else:
                print('Mahdoton ratkaista')

        else:
            print('Tuntematon komento')


def __tulosta_ratkaisu(pulma, liikkeet):
    print('')
    print('Ratkaisu:')
    pulma.tulosta()
    for liike in liikkeet:
        print('')
        if liike == 'y':
            print('ylös')
            pulma.ylos()
            pulma.tulosta()
        elif liike == 'a':
            print('alas')
            pulma.alas()
            pulma.tulosta()
        elif liike == 'v':
            print('vasen')
            pulma.vasen()
            pulma.tulosta()
        else:
            print('oikea')
            pulma.oikea()
            pulma.tulosta()

    print('')
    print('Liikkeitä: ' + str(len(liikkeet)))


if __name__ == "__main__":
    main()
