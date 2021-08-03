"""Mooduli sisältää pulmaa kuvaavan luokan"""

from math import sqrt


class Pulma:
    """Luokka pulman sisällön kuvaamiseen

    Luokka käyttää sisäisesti listaa pulman sisällön
    tallentamiseen. Metodien vasen, oikea, ylos ja alas
    nimet kuvaavat minne tyhjä ruutu liikkuisi ruudukossa."""

    def __init__(self, lista):
        self.__lista = lista
        self.__koko = len(self.__lista)
        self.__leveys = int((sqrt(self.__koko)))
        self.__sijainti = 0
        self.__aseta_sijainti()

    def __aseta_sijainti(self):
        for i in range(self.__koko):
            if self.__lista[i] == 0:
                self.__sijainti = i
                break

    def listaa(self) -> list:
        """Palauttaa pulman sisällön listana"""

        return self.__lista

    def koko(self) -> int:
        """Palauttaa pulman ruutujen määrän"""

        return self.__koko

    def leveys(self) -> int:
        """Palauttaa pulman leveyden/korkeuden"""

        return self.__leveys

    def sijainti(self) -> int:
        """Palauttaa pulman tyhjän ruudun sijainnin listassa"""

        return self.__sijainti

    def vasen(self) -> bool:
        """Siirtää tyhjää ruutua vasemmalle, jos mahdollista"""

        if self.__sijainti % self.__leveys == 0:
            return False

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti - 1]
        self.__lista[self.__sijainti - 1] = 0
        self.__sijainti -= 1
        return True

    def oikea(self) -> bool:
        """Siirtää tyhjää ruutua oikealle, jos mahdollista"""

        if (self.__sijainti + 1) % self.__leveys == 0:
            return False

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti + 1]
        self.__lista[self.__sijainti + 1] = 0
        self.__sijainti += 1
        return True

    def ylos(self) -> bool:
        """Siirtää tyhjää ruutua ylöspäin, jos mahdollista"""

        if self.__sijainti - self.__leveys < 0:
            return False

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti - self.__leveys]
        self.__lista[self.__sijainti - self.__leveys] = 0
        self.__sijainti -= self.__leveys
        return True

    def alas(self) -> bool:
        """Siirtää tyhjää ruutua alaspäin, jos mahdollista"""

        if self.__sijainti + self.__leveys >= self.__koko:
            return False

        self.__lista[self.__sijainti] = self.__lista[self.__sijainti + self.__leveys]
        self.__lista[self.__sijainti + self.__leveys] = 0
        self.__sijainti += self.__leveys
        return True

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
