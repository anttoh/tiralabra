from algoritmit.ratkaistavissa import on_ratkaistavissa
from algoritmit.generoi import generoi_ratkaistava_pulma


def test_generoi_ratkaistava_pulma_palauttaa_oikean_kokoisen_pulman():
    pulma = generoi_ratkaistava_pulma(3)
    assert pulma.leveys() == 3


def test_generoi_ratkaistava_pulma_palauttaa_ratkaistavissa_olevan_pulman():
    pulma = generoi_ratkaistava_pulma(10)
    assert on_ratkaistavissa(pulma)
