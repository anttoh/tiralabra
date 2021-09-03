"""Mooduli sisältää funktion, joka luo ratkaitavissa olevan pulman"""

from random import randint
from tietorakenteet.pulma import Pulma


def generoi_ratkaistava_pulma(leveys) -> Pulma:
    """Generoi ja palauttaa annetun leveysisen pulman"""

    pulma = Pulma(__generoi_tuple(leveys), leveys*leveys-1)
    for _ in range(100000):
        __liikuta_satunnaisesti(pulma)
    return pulma


def __generoi_tuple(leveys) -> tuple:
    pituus = leveys * leveys
    lista = []
    for i in range(pituus):
        lista.append(i + 1)
    lista[pituus - 1] = 0

    return tuple(lista)


def __liikuta_satunnaisesti(pulma):
    luku = randint(0, 3)
    if luku == 0 and pulma.voi_liikkua_vasenmalle():
        pulma.liiku_vasenmalle()
    elif luku == 1 and pulma.voi_liikkua_oikealle():
        pulma.liiku_oikealle()
    elif luku == 2 and pulma.voi_liikkua_ylospain():
        pulma.liiku_ylospain()
    elif luku == 3 and pulma.voi_liikkua_alaspain():
        pulma.liiku_alaspain()
