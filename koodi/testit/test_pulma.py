from tietorakenteet.pulma import Pulma


def pulma_testaukseen() -> Pulma:
    return Pulma([1, 2, 3, 4, 0, 5, 6, 7, 8])


def test_getterit_toimivat():
    pulma = pulma_testaukseen()
    assert pulma.listaa() == [1, 2, 3, 4, 0, 5, 6, 7, 8]
    assert pulma.koko() == 9
    assert pulma.leveys() == 3
    assert pulma.sijainti() == 4


def test_vasen_toimii():
    pulma = pulma_testaukseen()
    assert pulma.vasen()
    assert not pulma.vasen()


def test_oikea_toimii():
    pulma = pulma_testaukseen()
    assert pulma.oikea()
    assert not pulma.oikea()


def test_ylos_toimii():
    pulma = pulma_testaukseen()
    assert pulma.ylos()
    assert not pulma.ylos()


def test_alas_toimii():
    pulma = pulma_testaukseen()
    assert pulma.alas()
    assert not pulma.alas()
