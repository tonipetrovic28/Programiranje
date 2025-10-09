#stop-words
STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da']

#Funkcija za učitavanje teksta iz datoteke 
def ucitaj_tekst(filepath):
    try:
        # Kod za otvaranje datoteke ide ovdje
        with open(filepath, 'r', encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Greška: Datoteka na putanji '{filepath}' nije pronađena")
        return None # Vratit ćemo 'ništa' ako datoteka ne postoji

# Funkcija za pročišćavanje teksta 
def ocisti_tekst(tekst):
    # Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci

def broj_rijeci(lista_rijeci):
    # Rječnik za spremanje svake riječi i koliko se puta riječ ponovila
    brojac_rijeci = {}
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] += 1
        else:
            brojac_rijeci[rijec] = 1
    return brojac_rijeci

# ZADATAK 1: Uklanjanje stop-words
def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik

# ZADATAK 2: Sortiranje i ispis rezultata
def sortiraj_i_ispisi(rjecnik_frekvencija):
    sortirana_lista = sorted(rjecnik_frekvencija.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Top 15 najčešćih riječi ---")
    for i, (rijec, frekvencija) in enumerate(sortirana_lista[:15]):
        print(f"{i+1}. {rijec}: {frekvencija}")
    print("------------------------------")

if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        print("Učitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke.")

    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)

        # brojanje riječi i ispis
        brojac_rijeci = broj_rijeci(ucitani_tekst)
        print("Broj riječi u tekstu")
        print(brojac_rijeci)
        
        # Uklanjanje stop-words
        frekvencija_bez_stop = ukloni_stop_words(brojac_rijeci, STOP_WORDS)
        print("Broj riječi bez stop-words:")
        print(frekvencija_bez_stop)

        # sortiranje i ispis
        sortiraj_i_ispisi(frekvencija_bez_stop)

    else:
        print("Greška pri očišćavanju teksta.")

