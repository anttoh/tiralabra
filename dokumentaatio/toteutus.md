## Toteutusdokumentti

Ohjelman olennaisin osa on pulman (8 tai 15-peli) ratkaisija algoritmi, joka löytyy ratkaisija.py tiedostosta. Toteuttamani ratkaisija on IDA* algoritmi, joka käyttää walking distance heuristiikkaa. IDA* algoritmin aikavaativuus on O(b^d) ja tilavaativuus on O(d), missä b on branching factor ja d ratkaisun syvyys (depth). Walking distance heuristiikka käyttää BFS algoritmia etäisyys taulun luontiin. Tämän aika- ja tilavaativuus O(b^d). 4x4 pulman kohdalla taulussa on 24964 avain-arvo-paria ja tämän luomiseen menee n. 0.25 sekuntia. Taulukon luontiin kulunut aika on kuitenkin hyvin pieni ratkaisun löytämiseen kuluvaan aikaan nähden useimmissa tapauksissa. Siispä ratkaisijan aikavaativuus on O(b1^d1) + O(b2^d2) ja tilavaativuus on O(d1) + O(b2^d2), missä b1 ja d1 ovat IDA\* algoritmin, ja b2 ja d2 ovat BFS algoritmin branching factor ja depth. Aikavaativuus on siin n. O(b1^d1) ja tilavaativuus n. O(b2^d2). 5x5 pulman kohdalla etäisyys taulu saattaa olla liian suuri, joten nykyinen toteutus toimii korkeintaan 4x4 pulmien ratkaisijana.

Lähteitä:

https://web.archive.org/web/20141224035932/http://juropollo.xe0.ru:80/stp_wd_translation_en.htm

http://www.ic-net.or.jp/home/takaken/e/15pz/wd.gif

https://rosettacode.org/wiki/15_puzzle_solver#Iterative_Depth_A.2A
