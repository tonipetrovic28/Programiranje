ANALIZA MARS PODATAKA

Ovaj projekt služi za obradu i analizu podataka prikupljenih s površine Marsa. Cilj je pronaći potencijalno zanimljive lokacije koje bi mogle ukazivati na prisutnost života ili uvjete pogodne za život.

Program učitava podatke iz dvije CSV datoteke (lokacije i uzorci), spaja ih po ID-u uzorka te uklanja sve nelogične ili neispravne vrijednosti. Podaci koji ne zadovoljavaju definirane uvjete spremaju se kao anomalije, dok se ispravni podaci koriste za daljnju analizu.

UVJETI ZA ISPRAVNE PODATKE:

* temperatura tla mora biti između -100 i 40 stupnjeva C
* pH vrijednost mora biti između 0 i 14
* udio vode mora biti između 0 i 100%

Nakon filtriranja, program generira nekoliko grafova:

* odnos temperature tla i količine vode
* karta s prikazom dubine bušenja
* prikaz lokacija s detekcijom metana
* karta potencijalnih kandidata za život

KANDIDATI ZA DALJNJE ISTRAŽIVANJE:
Kao kandidati se označavaju sve lokacije gdje je:

* detektiran metan
* potvrđena prisutnost organskih molekula

Te lokacije se posebno označavaju na karti i spremaju u JSON datoteku za daljnju obradu.

IZLAZNE DATOTEKE:

* cisti_podaci.csv (filtrirani podaci)
* anomalije.csv (neispravni podaci)
* graf1_temperatura_voda.png
* graf2_karta_dubine.png
* graf3_metan.png
* karta_kandidata.png
* misijska_karta_jezero.jpg
* nexus_payload.json

JSON IZLAZ:
Za svaki kandidat generira se zapis koji sadrži ID uzorka, GPS koordinate i popis akcija koje sustav treba izvršiti (navigacija, sondiranje, slanje podataka).

POKRETANJE:

1. instalirati potrebne biblioteke (pandas, matplotlib, seaborn)
2. pokrenuti Python skriptu

NAPOMENA:
Projekt se može dodatno proširiti uvođenjem naprednijih metoda analize, poput rangiranja kandidata ili korištenja strojnog učenja.

KRAJ

