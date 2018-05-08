#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Formatuje dane pobrane przez pajączka do #csv.
"""

import re
import csv

# otwiera plik txt z ofertami
file = open('ustka.txt', 'r')

read_file = file.read()

lista_mieszkania_zmienne = []

lista_mieszkan = [read_file.split("_!_!_")]

podzielona_lista_mieszkan = []

for mieszkanie in lista_mieszkan:
    for x in mieszkanie:
        koniec_tytulu = x.find("dzielnicaadres:", 1)
        x = x[koniec_tytulu:]
        podzielona_lista_mieszkan.append([x])


for mieszkanie in podzielona_lista_mieszkan:
    for i in mieszkanie:

        id = i.find('Nr oferty w Otodom:') + 20
        id_koniec = id + 8
        id_oferty = i[id:id_koniec]

        cena = i.find('Cena') + 5
        cena_koniec = i.find('zł') - 1
        powierzchnia = i.find('Powierzchnia') + 13
        powierzchnia_koniec = i.find('Liczba pokoi') - 4
        liczba_pokoi = i.find('Liczba pokoi') + 13
        liczba_pokoi_koniec = liczba_pokoi + 1


        adres1 = i.find('dzielnicaadres:') + 39
        adres1_koniec = i.find('- Zobacz na mapie')

        lista_mieszkania_zmienne.append(id_oferty)
        price = i[cena:cena_koniec]
        lista_mieszkania_zmienne.append(price)
        size = i[powierzchnia:powierzchnia_koniec]
        lista_mieszkania_zmienne.append(size)
        rooms = i[liczba_pokoi:liczba_pokoi_koniec]
        lista_mieszkania_zmienne.append(rooms)

        pi = "Piętro"
        if pi in i:
            pietro = i.find('Piętro') + 7
            pietro_koniec = pietro + 1
            pietra = i[pietro:pietro_koniec]
            lista_mieszkania_zmienne.append(pietra)
        else:
            lista_mieszkania_zmienne.append("NA")

        adres = i[adres1:adres1_koniec]
        lista_mieszkania_zmienne.append(adres)

        longitude = i.find('data-lat=') + 10
        latitude = i.find('data-lon=') + 10
        longitude_koniec = latitude - 12
        latitude_koniec = i.find('data-poi-lat=') - 2

        dlugosc = i[longitude:longitude_koniec]
        lista_mieszkania_zmienne.append(dlugosc)
        szerokosc = i[latitude:latitude_koniec]
        lista_mieszkania_zmienne.append(szerokosc)

        cat_var = ("Rynek:", "Rodzaj zabudowy:", "Materiał budynku:", "Okna:", "Ogrzewanie:",
                    "Rok budowy:", "Stan wykończenia: do", "Czynsz:", "Forma własności:")

        for var in cat_var:
            regex = var + r" (\w+)"
            match = re.search(regex, i)
            if match:
                lista_mieszkania_zmienne.append(match.group(1))
            else:
                lista_mieszkania_zmienne.append("0")

        var01 = ("internet", "telewizja kablowa", "telefon", "rolety antywłamaniowe", "drzwi / okna antywłamaniowe",
                 "domofon / wideofon","monitoring / ochrona", "system alarmowy", "teren zamknięty", "meble", "pralka",
                 "zmywarka", "lodówka", "kuchenka", "piekarnik", "telewizor", "balkon", "pom. użytkowe",
                 "garaż/miejsce parkingowe", "piwnica", "ogródek", "taras", "winda", "dwupoziomowe", "oddzielna kuchnia",
                 "klimatyzacja")

        for var in var01:
            if var in i:
                lista_mieszkania_zmienne.append("1")
            else:
                lista_mieszkania_zmienne.append("0")

lista_do_csv = [lista_mieszkania_zmienne[x:x + 43] for x in range(0, len(lista_mieszkania_zmienne), 43)]

# usuwa duplikaty
import itertools
lista_do_csv.sort()
lista_do_csv = list(lista_do_csv for lista_do_csv,_ in itertools.groupby(lista_do_csv))

header = (['id oferty','cena (zł)', 'powierzchnia', 'liczba pokoi', 'piętro', 'adres', "dlugosc", "szerokosc", "rynek",
           "rodzaj zabudowy", "materiał budynku", "okna", "ogrzewanie",
           "rok budowy", "stan wykończenia (do)", "czynsz", "forma własności",
           "internet", "telewizja kablowa", "telefon", "rolety antywłamaniowe", "drzwi/okna antywłamaniowe",
           "domofon/wideofon", "monitoring/ochrona", "system alarmowy", "teren zamknięty", "meble", "pralka",
           "zmywarka", "lodówka", "kuchenka", "piekarnik", "telewizor", "balkon", "pom. użytkowe",
           "garaż/miejsce parkingowe", "piwnica", "ogródek", "taras", "winda",
           "dwupoziomowe", "oddzielna kuchnia", "klimatyzacja" ])

# zapisuje do csv
with open('ustka.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(header)
    for row in lista_do_csv:
        wr.writerow(row)

file.close()
