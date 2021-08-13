"""Mooduli sisältää funktion, joka luo ratkaitavissa olevan pulman"""

from random import randint
from tietorakenteet.pulma import Pulma


def generoi_ratkaistava_pulma(koko) -> Pulma:
    """Generoi ja palauttaa annetun kokoisen pulman"""

    pulma = Pulma(__generoi_tuple(koko))
    for _ in range(100000):
        __liikuta_satunnaisesti(pulma)
    return pulma


def __generoi_tuple(koko) -> tuple:
    pituus = koko * koko
    lista = []
    for i in range(pituus):
        lista.append(i + 1)
    lista[pituus - 1] = 0

    return tuple(lista)


def __liikuta_satunnaisesti(pulma):
    luku = randint(0, 3)
    if luku == 0:
        pulma.vasen()
    elif luku == 1:
        pulma.oikea()
    elif luku == 2:
        pulma.ylos()
    else:
        pulma.alas()
