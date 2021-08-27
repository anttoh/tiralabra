from tietorakenteet.pulma import Pulma
from algoritmit.ratkaisija import IDAStar


def test_ratkaisija_toimii():
    ratkaisija = IDAStar()

    pulma = Pulma([8, 6, 7, 2, 5, 4, 3, 0, 1], 7)
    liikkeet = ratkaisija.ratkaise(pulma)
    assert len(liikkeet) == 31

    pulma = Pulma([10, 4, 1, 15, 7, 2, 13, 14, 12, 8, 6, 3, 5, 0, 9, 11], 13)
    liikkeet = ratkaisija.ratkaise(pulma)
    assert len(liikkeet) == 50
