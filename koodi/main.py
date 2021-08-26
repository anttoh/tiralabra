"""Mooduli sisältää ohjelman päämetodin"""


import time
from algoritmit.ratkaisija import IDAStar
from algoritmit.generoi import generoi_ratkaistava_pulma
from algoritmit.ratkaistavissa import on_ratkaistavissa
from tietorakenteet.pulma import Pulma


def main():
    """Ohjelman päämetodi"""

    info = """Komenntot:
        h = listaa komennot
        q = lopettaa ohjelman
        1 = luo annetun levyisen ja korkuisen pulman
        2 = yrittää luoda pulman annetusta listasta lukuja, esim. 8 6 7 2 5 4 3 0 1"""

    print(info)

    while True:
        komento = input('Komento: ')
        if komento == 'q':
            break

        if komento == 'h':
            print(info)

        elif komento == '1':
            koko = int(input('Koko: '))
            pulma = generoi_ratkaistava_pulma(koko)
            pulma.tulosta()
            ratkaisija = IDAStar()

            alkoi = time.time()
            liikkeet = ratkaisija.ratkaise(pulma)
            loppui = time.time()

            __tulosta_ratkaisu(pulma, liikkeet)
            print("--- %s sekuntia ---" % (loppui - alkoi))

        elif komento == '2':
            lista = input('Lista: ')
            lista = lista.strip()
            lista = lista.split(' ')
            lista = list(map(int, lista))
            pulma = Pulma(tuple(lista))
            pulma.tulosta()
            if on_ratkaistavissa(pulma):
                ratkaisija = IDAStar()

                alkoi = time.time()
                liikkeet = ratkaisija.ratkaise(pulma)
                loppui = time.time()

                __tulosta_ratkaisu(pulma, liikkeet)
                print("--- %s sekuntia ---" % (loppui - alkoi))
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
