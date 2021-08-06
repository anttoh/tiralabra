"""Mooduli sisältää ohjelman päämetodin"""

from tietorakenteet.pulma import Pulma
from algoritmit.ratkaistavissa import on_ratkaistavissa
from algoritmit.generoi import generoi_ratkaistava_pulma


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
            # ratkaise pulma

        elif komento == '2':
            lista = input('Lista: ')
            lista = lista.strip()
            lista = lista.split(' ')
            lista = list(map(int, lista))
            pulma = Pulma(lista)
            pulma.tulosta()
            if on_ratkaistavissa(pulma):
                print("Mahdollista ratkaista")
                # ratkaise pulma
            else:
                print("Mahdoton ratkaista")

        else:
            print('Tuntematon komento')


if __name__ == "__main__":
    main()
