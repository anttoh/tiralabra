"""Mooduli sisältää ohjelman päämetodin"""

from tietorakenteet.pulma import Pulma
from algoritmit.ratkaistavissa import on_ratkaistavissa
from algoritmit.generoi import generoi_ratkaistava_pulma


def main():
    """Ohjelman päämetodi"""

    while True:
        komento = input('Komento: ')
        if komento == 'q':
            break

        if komento == '1':
            koko = int(input('Koko: '))
            pulma = generoi_ratkaistava_pulma(koko)
            if on_ratkaistavissa(pulma):
                print("Mahdollista ratkaista")
                pulma.tulosta()
            else:
                print("Mahdoton ratkaista")

        elif komento == '2':
            lista = input('Lista: ')
            lista = lista.split(' ')
            lista = list(map(int, lista))

            pulma = Pulma(lista)
            if on_ratkaistavissa(pulma):
                print("Mahdollista ratkaista")
            else:
                print("Mahdoton ratkaista")

        else:
            print('Tuntematon komento')


if __name__ == "__main__":
    main()
