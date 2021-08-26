"""Mooduli sisältää algoritmin, joka tarkistaa onko
pulma ratkaistavissa, funktiot"""


def on_ratkaistavissa(pulma) -> bool:
    """Palauttaa true, jos pulman voi ratkaista ja false muuten"""

    leveys = pulma.leveys()
    inversiot = __inversiot(pulma)
    rivi = __tyhjan_rivi(pulma)

    if __pariton(leveys) and __parillinen(inversiot):
        return True

    if __parillinen(leveys) and __pariton(inversiot) and __parillinen(rivi):
        return True

    if __parillinen(leveys) and __parillinen(inversiot) and __pariton(rivi):
        return True

    return False


def __parillinen(luku) -> bool:
    return luku % 2 == 0


def __pariton(luku) -> bool:
    return luku % 2 != 0


def __inversiot(pulma) -> int:
    # tätä voi tehostaa, jos on tarvetta

    inversiot = 0
    lista = pulma.tuplena()

    for i in range(pulma.koko()):
        for j in range(i + 1, pulma.koko()):
            if(lista[i] and lista[j] and lista[i] > lista[j]):
                inversiot += 1

    return inversiot


def __tyhjan_rivi(pulma) -> int:
    """Palauttaa rivin numeron, jolla tyhjä ruutu sijaitsee,
    ruudukon alaosasta laskettuna (alin rivi on 1))."""

    y_koordinaatti = int(pulma.sijainti() / pulma.leveys())
    return pulma.leveys() - y_koordinaatti
