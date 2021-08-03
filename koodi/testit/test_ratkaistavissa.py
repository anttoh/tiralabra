from tietorakenteet.pulma import Pulma
from algoritmit.ratkaistavissa import on_ratkaistavissa


def test_on_ratkaistavissa_palauttaa_false_kun_pulmaa_ei_voi_ratkaista():
    pulma = Pulma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0])
    assert not on_ratkaistavissa(pulma)


def test_on_ratkaistavissa_palauttaa_true_kun_pulman_voi_ratkaista():
    pulma = Pulma([1, 2, 3, 4, 5, 8, 6, 7, 0])
    assert on_ratkaistavissa(pulma)
    pulma = Pulma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 13, 14, 0])
    assert on_ratkaistavissa(pulma)
    pulma = Pulma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 12, 13, 15, 14])
    assert on_ratkaistavissa(pulma)
