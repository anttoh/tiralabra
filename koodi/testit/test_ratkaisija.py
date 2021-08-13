from tietorakenteet.pulma import Pulma
from algoritmit.ratkaisija import IDAStar


def test_ratkaisija_toimii():
    pulma = Pulma([2, 3, 6, 1, 5, 8, 0, 4, 7])
    ratkaisija = IDAStar()
    liikkeet = ratkaisija.ratkaise(pulma)
    assert len(liikkeet) == 10
