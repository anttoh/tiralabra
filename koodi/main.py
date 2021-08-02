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
            on_ratkaistavissa(pulma)

        elif komento == '2':
            lista = input('Lista: ')
            lista = lista.split(' ')
            for i in range(len(lista)):
                lista[i] = int(lista[i])

            pulma = Pulma(lista)
            on_ratkaistavissa(pulma)

        else:
            print('Tuntematon komento')


if __name__ == "__main__":
    main()
