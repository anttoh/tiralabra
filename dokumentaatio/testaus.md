## Testausdokumentti

Yksikkötestauksen kattavuusraportti löytyy codecovista.

En kerennyt tekemään mitään suuria suorituskykytestejä, vaan tein pientä manuaalista testaamista. Kaikki alla olevat testit voi toistaa antamalla ohjelmalle komennon 2 ja testissä käytetyn listan lukuja, jotka kuvaavat pulmaa. Ohjelma antaa ratkaisuun kuluneen ajan.

15-pelin, eli 4x4 pulman yleisin lyhimmän polun pituus on 52. Vanhalla Windows läppärilläni pulman 15 14 1 6 9 11 4 12 0 10 7 3 13 8 5 2, jonka lyhimmän polun pituus on 52, ratkaisemiseen meni n. 122 sekuntia.

Pulman 2 5 13 15 3 8 10 6 9 14 0 11 1 4 12 7 lyhimmän polun pituus on 54 ja tämän ratkaisemiseen meni n. 96 sekuntia. Vaikka lyhimmän polun pituus olikin pidempi kuin edellisessä testissä, niin ratkaisu löytyi kuitenkin nopeammin.

Pulman 13 11 1 14 5 7 6 0 9 2 3 12 10 15 8 4 lyhimmän polun pituus on 50 ja tämän ratkaisemiseen kului n. 59 sekuntia.

Pulman 14 3 5 10 1 0 7 4 9 15 8 13 12 6 2 11 lyhimmän polun pituus on 48 ja ratkaisemiseen kuluin n. 13 sekuntia.

Pulman 3 10 11 1 13 15 6 5 2 8 0 12 14 7 4 9 lyhimmän polun pituus on 50, mutta ratkaisemiseen kului vain n. 2.3 sekuntia.

Pulman 10 4 1 15 7 2 13 14 12 8 6 3 5 0 9 11, jonka lyhimmän polun pituus on 50, ratkeamiseen kului yllättävän vähän aikaa, vain n. 0.85 sekuntia.

Pisimmillään lyhimmän polun pituus on 80 liikettä, jolloin ratkaisun löytämiseen tulee todennäköisesti kulumaan useita tunteja.

8-pelin, eli 3x3 pulman pisin mahdollinen lyhimmän polun pituus on 31. Alla on ainoat laudat, joiden lyhimmän polun pituus on 31.

8 6 7 2 5 4 3 0 1 

6 4 7 8 5 0 3 2 1

Molempien kohdalla ratkaisuun kului vain n 0.15 sekuntia. Testaillessani ohjelman satunnaisesti tuottamia 3x3 pulmia, en törmännyt yhteenkään pulmaan, jonka ratkaisemiseen olisi kulunut yli 0.15 sekuntia.
