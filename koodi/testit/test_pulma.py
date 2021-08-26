from tietorakenteet.pulma import Pulma


def pulma_testaukseen() -> Pulma:
    return Pulma([1, 2, 3, 4, 0, 5, 6, 7, 8], 4)


def test_getterit_toimivat():
    pulma = pulma_testaukseen()
    assert pulma.koko() == 9
    assert pulma.leveys() == 3
    assert pulma.sijainti() == 4
    assert pulma.tuplena() == (1, 2, 3, 4, 0, 5, 6, 7, 8)


def test_liikkuminen():
    pulma = pulma_testaukseen()

    assert pulma.voi_liikkua_vasenmalle()
    pulma.liiku_vasenmalle()
    assert not pulma.voi_liikkua_vasenmalle()
    pulma.liiku_oikealle()

    assert pulma.voi_liikkua_oikealle()
    pulma.liiku_oikealle()
    assert not pulma.voi_liikkua_oikealle()
    pulma.liiku_vasenmalle()

    assert pulma.voi_liikkua_ylospain()
    pulma.liiku_ylospain()
    assert not pulma.voi_liikkua_ylospain()
    pulma.liiku_alaspain()

    assert pulma.voi_liikkua_alaspain()
    pulma.liiku_alaspain()
    assert not pulma.voi_liikkua_alaspain()
    pulma.liiku_ylospain()

    assert pulma.tuplena() == (1, 2, 3, 4, 0, 5, 6, 7, 8)


def test_tulosta_tulostaa_pulman_ruudukkona(capsys):
    pulma_testaukseen().tulosta()
    tulostettu_ruudukko = capsys.readouterr().out
    toivottu_tulostus = "\n|1|2|3|\n|4|0|5|\n|6|7|8|\n"
    assert tulostettu_ruudukko == toivottu_tulostus
