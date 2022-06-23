import csv  # UVODIM CSV MODUL KOJI ĆE NAM POMOĆI PRI ČITANJU DATOTEKE

ulazna = input("Unesi ime datoteke:")
industrija = input("Unesi granu industrije:")


def obrada(
        fajl):  # OVA FUNKCIJA JE GLAVNA U PROGRAMU ONA PRAVI REČNIK KOJI ČINE IME GRADA(KAO KLJUC) I UKUPNA VREDNOST SVIH TRAZENIH KOMPANIJA IZ NJEGA
    rezultati = {}  # INICIJALIZUJEMO PRAZAN REČNIK
    citac = csv.reader(fajl)  # POZVAMO METODU KOJA JE OD NASU DATOTEKU RAZDVOJILA PO REDOVIMA NA LISTE
    for red in citac:
        vrednost = red[1]
        grad = red[2]
        delatnost = red[3]

        if delatnost == industrija:  # U OVOM BLOKU POPUNJAVAMO REČNIK
            kljuc = grad
            if kljuc not in rezultati:
                rezultati[grad] = float(vrednost)
            else:
                rezultati[grad] += float(vrednost)

    sortiraniPoVrednosti = dict(sorted(rezultati.items(), key=lambda x: x[0]))  # PRVO SORTIRAMO REČNIK PO KLJUCEVIMA(NA LEKSIKOGRAFSOM NIVOU)
    skrozSortirani = dict(sorted(sortiraniPoVrednosti.items(), key=lambda x: x[1], reverse=True))  # ONDA TAKO SORTIRANI REČNIK SORTIRAMO PO VREDNOSTIMA U OPADAJUCEM PORETKU
    return skrozSortirani


def imeDatoteke(string):  # OVA FUNKCIJA PRAVI IME DATOTEKE U KOJU TREBA DA UPISEMO TRAZENI REZULTAT
    nova = string.replace(" ", "_") + ".txt"  # OVDE SMO ZAMENILI BLANCO ZNAKE SA '_'
    return nova


def skupDelatnosti(
        fajl):  # OVA FUNKCIJA PRAVI SKUP SVIH INSUSTRIJA U DATOTECI(TO CE NAM TREBATI ZBOG PROVERE JEDNOG USLOVA)
    skupIndustrija = set()
    citac = csv.reader(fajl)
    for red in citac:
        skupIndustrija.add(red[3])
    skupIndustrija.remove(
        "Industry")  # AKO POGLEDATE NA VRH DATOTEKE VIDECETE KAO NASLOVNU JEDNU LINIJU, U NJOJ NAM SE NE NALAZE BITNI PODACI ZA OBRADU PA UKLANJAMO NJEN DOPRINOS OVOM SKUPU
    return skupIndustrija


try:  # TRY BLOK
    with open(ulazna, "r") as file:
        sveIndustrije = (skupDelatnosti(file))
    if industrija not in sveIndustrije:
        print("GRESKA", end="")  # U OVOM BLOKU SMO OBRADILI SLUCAJ KADA NAM SE UNESE NEPOSTOJECA INDUSTRIJA

    with open(ulazna, "r") as file:
        sortiraniRezultati = obrada(file)

    novaDatoteka = imeDatoteke(industrija)
    with open(novaDatoteka, "w") as file:  # OTVARAMO NOVU DATOTEKU U KOJU CEMO UPISIVATI TRAZENE REZULTATE
        for grad, vrednost in sortiraniRezultati.items():
            file.write("{}{}{:0.2f}\n".format(grad, "-", vrednost))
except IOError:  # OVA GRANA KAZE DA AKO SE UNESE NEPOSTOJECA DATOTEKA DA SE KOD PREKINE
    print("DAT_GRESKA", end="")

