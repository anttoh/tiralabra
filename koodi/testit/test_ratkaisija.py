from tietorakenteet.pulma import Pulma
from algoritmit.ratkaisija import IDAStar


def test_ratkaisija_toimii():
    pulma = Pulma([8, 6, 7, 2, 5, 4, 3, 0, 1])  # Haastavin 3x3 pulma
    ratkaisija = IDAStar()
    liikkeet = ratkaisija.ratkaise(pulma)
    assert len(liikkeet) == 31
