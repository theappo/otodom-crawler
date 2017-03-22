"""
Script to format the text file generated by the crawler
"""

import re
import csv

#opens the text file
file = open('otodom_mieszkania_gdansk.txt', 'r')

read_file = file.read()

#list to split variables of each flat
nowa_lista = []

#creates a list from the text file
lista_mieszkań = [read_file.split("_!_!_")]

jeszcze_jedna = []

for mieszkanie in lista_mieszkań:
    for x in mieszkanie:
        koniec_tytułu = x.find("\n", 1)
        x = x[koniec_tytułu:]
        jeszcze_jedna.append([x])



for mieszkanie in jeszcze_jedna:
    for i in mieszkanie:

        cena = i.find('cena') + 5
        cena_koniec = i.find('zł') - 1
        price = i[cena:cena_koniec]
        powierzchnia = i.find('powierzchnia') + 13
        powierzchnia_koniec = i.find('liczba pokoi') - 4
        liczba_pokoi = i.find('liczba pokoi') + 13
        liczba_pokoi_koniec = liczba_pokoi + 1

        adres1 = i.find('dzielnicaadres:') + 15
        adres1_koniec = i.find("k_ad") - 1

        price = i[cena:cena_koniec]
        nowa_lista.append(price)
        size = i[powierzchnia:powierzchnia_koniec]
        nowa_lista.append(size)
        rooms = i[liczba_pokoi:liczba_pokoi_koniec]
        nowa_lista.append(rooms)

        pi = "piętro"
        if pi in i:
            pietro = i.find('piętro') + 7
            pietro_koniec = pietro + 1
            pietra = i[pietro:pietro_koniec]
            nowa_lista.append(pietra)
        else:
            nowa_lista.append("NA")

        adres = i[adres1:adres1_koniec]
        nowa_lista.append(adres)

        cat_var = ("rynek:", "rodzaj zabudowy:", "materiał budynku:", "okna:", "ogrzewanie:",
                    "rok budowy:", "stan wykończenia: do", "czynsz:", "forma własności:")

        for var in cat_var:
            regex = var + r" (\w+)"
            match = re.search(regex, i)
            if match:
                nowa_lista.append(match.group(1))
            else:
                nowa_lista.append("0")


        var01 = ("internet", "telewizja kablowa", "telefon", "rolety antywłamaniowe", "drzwi / okna antywłamaniowe",
                 "domofon / wideofon","monitoring / ochrona", "system alarmowy", "teren zamknięty", "meble", "pralka",
                 "zmywarka", "lodówka", "kuchenka", "piekarnik", "telewizor", "balkon", "pom. użytkowe",
                 "garaż/miejsce parkingowe", "piwnica", "ogródek", "taras", "winda", "dwupoziomowe", "oddzielna kuchnia",
                 "klimatyzacja")

        for var in var01:
            if var in i:
                nowa_lista.append("1")
            else:
                nowa_lista.append("0")


#final list
super_nowa_lista = [nowa_lista[x:x+40] for x in range(0, len(nowa_lista), 40)]

header = (['cena (zł)', 'powierzchnia', 'liczba pokoi', 'piętro', 'adres', "rynek",
           "rodzaj zabudowy", "materiał budynku", "okna", "ogrzewanie",
           "rok budowy", "stan wykończenia (do)", "czynsz", "forma własności",
           "internet", "telewizja kablowa", "telefon", "rolety antywłamaniowe", "drzwi/okna antywłamaniowe",
           "domofon/wideofon", "monitoring/ochrona", "system alarmowy", "teren zamknięty", "meble", "pralka",
           "zmywarka", "lodówka", "kuchenka", "piekarnik", "telewizor", "balkon", "pom. użytkowe",
           "garaż/miejsce parkingowe", "piwnica", "ogródek", "taras", "winda",
           "dwupoziomowe", "oddzielna kuchnia", "klimatyzacja" ])

#saves to *.csv format
with open('otodom_gdansk.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(header)
    for row in super_nowa_lista:
        wr.writerow(row)

file.close()
