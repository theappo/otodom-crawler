#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


file = open("ustka.txt","w")

def spider(max_page):
    """ znajduje linki do ofert """
    page = 1
    while page <= max_page:
        url = "https://www.otodom.pl/sprzedaz/mieszkanie/ustka/?page=" + str(page)
        source = requests.get(url)
        plain = source.text
        soup = BeautifulSoup(plain, "html.parser")
        for link in soup.findAll("header", {"class": "offer-item-header"}):
            find_href = link.a
            href = find_href.get("href")
            get_data(href)
        page += 1


def get_data(url):
    """ pobiera dane """
    source = requests.get(url)
    plain = source.text
    soup = BeautifulSoup(plain, "html.parser")
    file.write("_!_!_")
    for title in soup.findAll('h1', {'itemprop': 'name'}):
        title_text = title.text
        file.write(title_text)
    for adres in soup.findAll('p', {'class': 'address-links'}):
        adres = adres.text
        file.write("dzielnicaadres:" + adres)
        file.write("k_ad")
    for main in soup.findAll('ul', {'class': 'main-list'}):
        main_text = main.text
        file.write(main_text)
    for sub in soup.findAll('ul', {'class': 'sub-list'}):
        sub_text = sub.text
        file.write(sub_text)
    for add in soup.findAll('ul', {'class': 'dotted-list'}):
        add_text = add.text
        file.write(add_text)
    for id in soup.findAll('section', {'class': 'section-offer-text updated'}):
        id_text = id.text
        file.write(id_text)
    for j in soup.select('#adDetailInlineMap'):
        file.write(str(j) + "\n")


spider(1)

file.close()
