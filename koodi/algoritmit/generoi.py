"""Mooduli sisältää funktion, joka luo ratkaitavissa olevan pulman"""

from random import randint
from tietorakenteet.pulma import Pulma


def generoi_ratkaistava_pulma(koko) -> Pulma:
    """Generoi ja palauttaa annetun kokoisen pulman"""

    pulma = Pulma(__generoi_tuple(koko), koko*koko-1)
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
        if pulma.voi_liikkua_vasenmalle():
            pulma.liiku_vasenmalle()
        else:
            pulma.liiku_oikealle()
    elif luku == 1:
        if pulma.voi_liikkua_oikealle():
            pulma.liiku_oikealle()
        else:
            pulma.liiku_vasenmalle()
    elif luku == 2:
        if pulma.voi_liikkua_ylospain():
            pulma.liiku_ylospain()
        else:
            pulma.liiku_alaspain()
    else:
        if pulma.voi_liikkua_alaspain():
            pulma.liiku_alaspain()
        else:
            pulma.liiku_ylospain()
