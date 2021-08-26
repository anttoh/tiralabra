"""Mooduli sisältää pulmaa kuvaavan luokan"""

from math import sqrt


class Pulma:
    """Luokka pulman sisällön kuvaamiseen

    Luokka käyttää sisäisesti listaa pulman sisällön
    tallentamiseen, mutta sisältö annetaan tuplena.
    Sijainti tarkoittaa tyhjän ruudun eli luvun 0 sijaintia annetussa tuplessa.
    Metodien vasen, oikea, ylos ja alas
    nimet kuvaavat minne tyhjä ruutu liikkuisi ruudukossa."""

    def __init__(self, sisalto: tuple, sijainti: int):
        self.__lista = list(sisalto)
        self.__koko = len(self.__lista)
        self.__leveys = int((sqrt(self.__koko)))
        self.__sijainti = sijainti

    def tuplena(self) -> tuple:
        """Palauttaa pulman sisällön tuplena"""

        return tuple(self.__lista)

    def koko(self) -> int:
        """Palauttaa pulman ruutujen määrän"""

        return self.__koko

    def leveys(self) -> int:
        """Palauttaa pulman leveyden/korkeuden"""

        return self.__leveys

    def sijainti(self) -> int:
        """Palauttaa pulman tyhjän ruudun sijainnin listassa"""

        return self.__sijainti

    def voi_liikkua_vasenmalle(self) -> bool:
        """Palauttaa true, jos tyhjää ruutua voi siirtä vasemmalle"""

        return self.__sijainti % self.__leveys != 0

    def voi_liikkua_oikealle(self) -> bool:
        """Palauttaa true, jos tyhjää ruutua voi siirtä oikealle"""

        return (self.__sijainti + 1) % self.__leveys != 0

    def voi_liikkua_ylospain(self) -> bool:
        """Palauttaa true, jos tyhjää ruutua voi siirtä ylöspäin"""

        return self.__sijainti - self.__leveys >= 0

    def voi_liikkua_alaspain(self) -> bool:
        """Palauttaa true, jos tyhjää ruutua voi siirtä alaspäin"""

        return self.__sijainti + self.__leveys < self.__koko

    def liiku_vasenmalle(self):
        """Siirtää tyhjää ruutua vasemmalle"""

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti - 1]
        self.__lista[self.__sijainti - 1] = 0
        self.__sijainti -= 1

    def liiku_oikealle(self):
        """Siirtää tyhjää ruutua oikealle"""

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti + 1]
        self.__lista[self.__sijainti + 1] = 0
        self.__sijainti += 1

    def liiku_ylospain(self):
        """Siirtää tyhjää ruutua ylöspäin"""

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti - self.__leveys]
        self.__lista[self.__sijainti - self.__leveys] = 0
        self.__sijainti -= self.__leveys

    def liiku_alaspain(self):
        """Siirtää tyhjää ruutua alaspäin"""

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti + self.__leveys]
        self.__lista[self.__sijainti + self.__leveys] = 0
        self.__sijainti += self.__leveys

    def tulosta(self):
        """Tulostaa pulman sisällön taulukkona"""

        ruudun_leveys = len(str(self.__koko))
        for i in range(self.__koko):
            if i % self.__leveys == 0:
                print()
                print(end='|')
            ruutu = "{:>{l}}".format(self.__lista[i], l=ruudun_leveys)
            print(ruutu, end='|')
        print()
