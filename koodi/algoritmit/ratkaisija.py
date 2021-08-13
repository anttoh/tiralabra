"""Mooduli sisältää pulman ratkaisijan"""

from math import sqrt
from tietorakenteet.pulma import Pulma


class IDAStar:
    """Iterative deepening A* algoritmin toteutus"""

    def __init__(self):
        self.ratkaistu_enum = object()

        self.heuristiikka = heuristiikka_funktio(0)
        self.naapurit = naapurit_funktio(self.heuristiikka)
        self.polku = []
        self.polku_liikkeet = []
        self.on_polulla = {}
        self.maali = ()
        self.raja = 0

    def ratkaise(self, pulma) -> list:
        """Ratkaisee annetun pulman IDA* algoritmin avulla ja
        palauttaa listan, joka sisältää liikkeet, jotka johtavat
        pulman alkutilasta pulman ratkaistuun tilaan."""

        koko = pulma.koko()
        juuri = pulma.tuplena()

        self.heuristiikka = heuristiikka_funktio(koko)
        self.naapurit = naapurit_funktio(self.heuristiikka)
        self.polku = [juuri]
        self.polku_liikkeet = []
        self.on_polulla = {juuri}
        self.raja = self.heuristiikka(juuri)
        self.maali = list(range(1, koko + 1))
        self.maali[pulma.koko() - 1] = 0
        self.maali = tuple(self.maali)

        while True:
            t = self.__haku(0)

            if t == self.ratkaistu_enum:
                return self.polku_liikkeet

            self.raja = t

    def __haku(self, g: int) -> object:
        noodi = self.polku[-1]
        f = g + self.heuristiikka(noodi)

        if f > self.raja:
            return f

        if noodi == self.maali:
            return self.ratkaistu_enum

        minimi = float('inf')
        for seuraava, liike in self.naapurit(noodi):
            if seuraava in self.on_polulla:
                continue

            self.polku.append(seuraava)
            self.polku_liikkeet.append(liike)
            self.on_polulla.add(seuraava)

            t = self.__haku(g + 1)

            if t == self.ratkaistu_enum:
                return self.ratkaistu_enum

            if t < minimi:
                minimi = t

            self.polku.pop()
            self.polku_liikkeet.pop()
            self.on_polulla.remove(seuraava)

        return minimi


def naapurit_funktio(heuristiikka):
    """Tämä funktio palauttaa funktion n, joka palauttaa noodin naapurit"""

    def n(noodi: tuple) -> list:
        """Funktio palauttaa listan annetun noodin (Pulman tilan) naapureista,
        eli tiloista joihin annetusta noodista pääsee yhdellä liikkeellä.
        Lista järjestetään annetun heuristiikan mukaan."""

        pulma = Pulma(noodi)

        naapurit = []
        if pulma.ylos():
            naapurit.append((pulma.tuplena(), 'y'))
            pulma.alas()
        if pulma.alas():
            naapurit.append((pulma.tuplena(), 'a'))
            pulma.ylos()
        if pulma.vasen():
            naapurit.append((pulma.tuplena(), 'v'))
            pulma.oikea()
        if pulma.oikea():
            naapurit.append((pulma.tuplena(), 'o'))
            pulma.vasen()

        naapurit.sort(key=lambda naapuri: heuristiikka(naapuri[0]))

        return naapurit

    return n


# tätä tulee parantaa...
def heuristiikka_funktio(koko: int):
    """Tämä funktio palauttaa heuristikka funktion h"""

    leveys = int(sqrt(koko))

    def h(noodi: tuple) -> int:
        """Heuristiikka funktio, joka laskee pulman ruutujen
        manhattan etäisyyksiä niiden lopullisiin paikkoihin nähden,
        sekä rivien ja sarakkeiden lineaari konflikteja."""

        etaisyydet = 0
        rivit = [[]]*leveys
        sarakkeet = [[]]*leveys
        for i in range(koko):
            luku = noodi[i]
            y1 = int(i / leveys)
            x1 = int(i % leveys)
            y2 = int(luku / leveys)
            x2 = int(luku % leveys)
            etaisyys = abs(y2 - y1) + abs(x2 - x1)
            etaisyydet += etaisyys

            if y1 == y2 and x1 != x2:
                sarakkeet[y1].append(luku)

            if x1 == x2 and y1 != y2:
                rivit[x1].append(luku)

        for i in range(leveys):
            rivi = rivit[i]
            pituus = len(rivi)
            if pituus < 2:
                continue
            edellinen = rivi[0]
            for j in range(1, pituus):
                if rivi[j] < edellinen:
                    etaisyydet += 2
                edellinen = rivi[j]

        for i in range(leveys):
            sarake = sarakkeet[i]
            pituus = len(sarake)
            if pituus < 2:
                continue
            edellinen = sarake[0]
            for j in range(1, pituus):
                if sarake[j] < edellinen:
                    etaisyydet += 2
                edellinen = sarake[j]

        return etaisyydet

    return h
