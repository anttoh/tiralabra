"""Mooduli sisältää pulman ratkaisijan"""

from tietorakenteet.pulma import Pulma


class IDAStar:
    """Iterative deepening A* algoritmin toteutus"""

    def __init__(self):
        self.ratkaistu_enum = object()

        self.polku = []
        self.polku_liikkeet = []
        self.on_polulla = {()}

        self.maali = ()

        self.heuristiikka = heuristiikka_funktio(1, self.maali)

        self.naapurit = naapurit_funktio(self.heuristiikka)

        self.raja = 0

    def ratkaise(self, pulma) -> list:
        """Ratkaisee annetun pulman IDA* algoritmin avulla ja
        palauttaa listan, joka sisältää liikkeet, jotka johtavat
        pulman alkutilasta pulman ratkaistuun tilaan."""

        juuri = pulma.tuplena()

        self.polku = [juuri]
        self.polku_liikkeet = []
        self.on_polulla = {juuri}

        self.maali = list(range(1, pulma.koko() + 1))
        self.maali[pulma.koko() - 1] = 0
        self.maali = tuple(self.maali)

        self.heuristiikka = heuristiikka_funktio(
            pulma.leveys(), self.maali)

        self.naapurit = naapurit_funktio(self.heuristiikka)

        self.raja = self.heuristiikka(juuri)

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

    def __n(noodi: tuple) -> list:
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

    return __n


def heuristiikka_funktio(n: int, maali: tuple):
    """Tämä funktio palauttaa heuristikka funktion h.
    Parametreina ovat pulman leveys/korkeus n
    ja pulman ratkaistu tila tuplena"""

    walking_distance = __luo_walking_distance_taulu(n)
    oikeat_ruudut = {i: maali.index(i) for i in maali}

    def __h(noodi: tuple) -> int:
        """Walking distance heuristiikka"""

        vaaka = [0]*n*n
        pysty = [0]*n*n
        etaisyys = 0

        for i, luku in enumerate(noodi):
            if luku == 0:
                continue

            oikea_ruutu = oikeat_ruudut[luku]
            x_nykyinen = i % n
            y_nykyinen = i // n
            x_oikea = oikea_ruutu % n
            y_oikea = oikea_ruutu // n
            vaaka[n * y_nykyinen + y_oikea] += 1
            pysty[n * x_nykyinen + x_oikea] += 1

            if y_nykyinen == y_oikea:
                for k in range(i + 1, i - i % n + n):
                    if (
                        noodi[k]
                        and oikeat_ruudut[noodi[k]] // n == y_nykyinen
                        and oikeat_ruudut[noodi[k]] < oikea_ruutu
                    ):
                        etaisyys += 2

            if x_nykyinen == x_oikea:
                for k in range(i + n, n * n, n):
                    if (
                        noodi[k]
                        and oikeat_ruudut[noodi[k]] % n == x_nykyinen
                        and oikeat_ruudut[noodi[k]] < oikea_ruutu
                    ):
                        etaisyys += 2

        etaisyys += walking_distance[tuple(vaaka)]
        etaisyys += walking_distance[tuple(pysty)]

        return etaisyys

    return __h


def __luo_walking_distance_taulu(n: int) -> dict:
    """Luo ja palauttaa walking distance taulun"""

    maali_konfiguraatio = [0]*n*n
    for i in range(0, n*n, n+1):
        maali_konfiguraatio[i] = n
    maali_konfiguraatio[n*n-1] -= 1

    maali_konfiguraatio = tuple(maali_konfiguraatio)

    taulu = {}
    vieraile = [(maali_konfiguraatio, 0, n-1)]

    while vieraile:
        konfiguraatio, hinta, rivi = vieraile.pop(0)
        if konfiguraatio in taulu:
            continue

        taulu[konfiguraatio] = hinta

        for i in [-1, 1]:
            r = rivi + i
            if r < 0 or r >= n:
                continue

            for j in range(n):
                if konfiguraatio[n*r + j] > 0:
                    konf = list(konfiguraatio)
                    konf[n*r + j] -= 1
                    konf[n*rivi + j] += 1
                    vieraile.append((tuple(konf), hinta + 1, r))

    return taulu
