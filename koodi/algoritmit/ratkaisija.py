"""Mooduli sisältää pulman ratkaisijan"""

from tietorakenteet.pulma import Pulma


class IDAStar:
    """Iterative deepening A* algoritmin toteutus"""

    def __init__(self):
        self.__ratkaistu_enum = object()

        self.__polku = []
        self.__polku_liikkeet = []
        self.__on_polulla = {()}
        self.__sijainnit = []

        self.__maali = ()

        self.__heuristiikka = heuristiikka_funktio(1, self.__maali)

        self.__naapurit = naapurit_funktio(self.__heuristiikka)

        self.__raja = 0

    def ratkaise(self, pulma) -> list:
        """Ratkaisee annetun pulman IDA* algoritmin avulla ja
        palauttaa listan, joka sisältää liikkeet, jotka johtavat
        pulman alkutilasta pulman ratkaistuun tilaan."""

        juuri = pulma.tuplena()

        self.__polku = [juuri]
        self.__polku_liikkeet = []
        self.__on_polulla = {juuri}
        self.__sijainnit = [pulma.sijainti()]

        pituus = pulma.leveys() * pulma.leveys()
        self.__maali = list(range(1, pituus + 1))
        self.__maali[pituus - 1] = 0
        self.__maali = tuple(self.__maali)

        self.__heuristiikka = heuristiikka_funktio(
            pulma.leveys(), self.__maali)

        self.__naapurit = naapurit_funktio(self.__heuristiikka)

        self.__raja = self.__heuristiikka(juuri)

        while True:
            t = self.__haku(0)

            if t == self.__ratkaistu_enum:
                return self.__polku_liikkeet

            self.__raja = t

    def __haku(self, g: int) -> object:
        noodi = self.__polku[-1]
        f = g + self.__heuristiikka(noodi)

        if f > self.__raja:
            return f

        if noodi == self.__maali:
            return self.__ratkaistu_enum

        minimi = float('inf')
        for seuraava, sijainti, liike in self.__naapurit(noodi, self.__sijainnit[-1]):
            if seuraava in self.__on_polulla:
                continue

            self.__polku.append(seuraava)
            self.__polku_liikkeet.append(liike)
            self.__on_polulla.add(seuraava)
            self.__sijainnit.append(sijainti)

            t = self.__haku(g + 1)

            if t == self.__ratkaistu_enum:
                return self.__ratkaistu_enum

            if t < minimi:
                minimi = t

            self.__polku.pop()
            self.__polku_liikkeet.pop()
            self.__on_polulla.remove(seuraava)
            self.__sijainnit.pop()

        return minimi


def naapurit_funktio(heuristiikka):
    """Tämä funktio palauttaa funktion n, joka palauttaa noodin naapurit"""

    def __n(noodi: tuple, sijainti: int) -> list:
        """Funktio palauttaa listan annetun noodin (Pulman tilan) naapureista,
        eli tiloista joihin annetusta noodista pääsee yhdellä liikkeellä.
        Lista järjestetään annetun heuristiikan mukaan. Sijainti on
        tyhjän ruudun (luvun 0) siijainti """

        pulma = Pulma(noodi, sijainti)

        naapurit = []
        if pulma.voi_liikkua_ylospain():
            pulma.liiku_ylospain()
            naapurit.append((pulma.tuplena(), pulma.sijainti(), 'y'))
            pulma.liiku_alaspain()
        if pulma.voi_liikkua_alaspain():
            pulma.liiku_alaspain()
            naapurit.append((pulma.tuplena(), pulma.sijainti(), 'a'))
            pulma.liiku_ylospain()
        if pulma.voi_liikkua_vasenmalle():
            pulma.liiku_vasenmalle()
            naapurit.append((pulma.tuplena(), pulma.sijainti(), 'v'))
            pulma.liiku_oikealle()
        if pulma.voi_liikkua_oikealle():
            pulma.liiku_oikealle()
            naapurit.append((pulma.tuplena(), pulma.sijainti(), 'o'))
            pulma.liiku_vasenmalle()

        naapurit.sort(key=lambda naapuri: heuristiikka(naapuri[0]))

        return naapurit

    return __n


def heuristiikka_funktio(n: int, maali: tuple):
    """Tämä funktio palauttaa heuristikka funktion h.
    Parametreina ovat pulman leveys/korkeus n
    ja pulman ratkaistu tila tuplena"""

    walking_distance = __luo_walking_distance_taulu(n)
    oikeat_ruudut = {i: maali.index(i) for i in maali}
    nn = n*n

    def __h(noodi: tuple) -> int:
        """Walking distance heuristiikka"""

        vaaka = [0]*nn
        pysty = [0]*nn
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

    nn = n*n
    maali_konfiguraatio = [0]*nn
    for i in range(0, nn, n+1):
        maali_konfiguraatio[i] = n
    maali_konfiguraatio[nn-1] -= 1

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
