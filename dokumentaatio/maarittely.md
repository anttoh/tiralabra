# N-Puzzle Solver

## Määrittelydokumentti
Työn tavoitteena on luoda ohjelma, jolle annetaan syötteenä jokin nxn kokoinen taulukko (esim. 15-pelin kohdalla 4x4 taulukko) ja ohjelma tulostaa merkkijonon, joka kuvastaa taulukon järjestämiseen tehtyjä liikkeitä. Taulukkoa ei ole aina mahdollista saada järjestykseen, jolloin ohjelma ilmoittaa tästä. Ohjelmalla tulisi olla ainakin kaksi ratkaisija algoritmia, joista ensimmäinen antaa jonkin ratkaisun mahdollisimman nopeasti ja toinen, joka antaa mahdollisimman vähän liikkeitä vaativan ratkaisun.

Toteutan ohjelman Pythonilla. Ohjelmalle ei ole tarvetta toteuttaa sen kummoisempaa käyttöliittymää, vaan ohjelmalle annetaan komentorivillä tarvittavat argumentit, kuten ratkaistava taulukko ja käytettävä algoritmi.

Algoritmin, joka tarkistaa onko annettu taulukko mahdollista saada järjestykseen, aikavaativuus on O(n²) ja tilavaatisuus on O(n). Algoritmi perustuu taulukossa olevien inversioiden laskemiseen. Kyseisestä algomirmista tietoa [täältä](https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/)

Algoritmiksi, joka ratkaisee pulman käyttäen mahdollisimman vähän liikkeitä, sopii [IDA*](https://en.wikipedia.org/wiki/Iterative_deepening_A*), jonka aikavaativuus on O(b^d), missä b on branching factor ja d on ratkaisun syvyys. Algoritmin tilavaativuus on O(d).

Algoritmi, joka ratkaisee pulman mahdollisimman nopeasti, toimii O(n³) ajassa. Algoritmista löytyy tietota [täältä](http://cseweb.ucsd.edu/~ccalabro/essays/15_puzzle.pdf)

**Opinto-ohjelma**: Tietojenkäsittelytieteen kandidaatti (TKT) 

**Projektin kieli**: Suomi
