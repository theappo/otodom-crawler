"""
scraps otodom.pl in order to get the offers of flats
based on: https://www.youtube.com/watch?v=XjNm9bazxn8
"""

import requests
from bs4 import BeautifulSoup

#saves every print() output in *.txt file
import sys
sys.stdout=open("otodom_mieszkania_gdansk_part2.txt","w")


def spider(max_page):
    """ finds links to offers """
    page = 150
    while page <= max_page:
        url = "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?page=" + str(page)
        source = requests.get(url)
        plain = source.text
        soup = BeautifulSoup(plain, "html.parser")
        for link in soup.findAll("header", {"class": "offer-item-header"}):
            find_href = link.a
            href = find_href.get("href")
            #print(href)
            get_data(href)
        page += 1


def get_data(url):
    """ scraps the needed data """
    source = requests.get(url)
    plain = source.text
    soup = BeautifulSoup(plain, "html.parser")
    print("_!_!_")
    for title in soup.findAll('h1', {'itemprop': 'name'}):
        title_text = title.text
        print(title_text)
    for adres in soup.findAll('h3', {'class': 'price-comparison-subtitle'}):
        adres = adres.text
        print("dzielnicaadres:" + adres)
        print("k_ad")
    for main in soup.findAll('ul', {'class': 'main-list'}):
        main_text = main.text
        print(main_text)
    for sub in soup.findAll('ul', {'class': 'sub-list'}):
        sub_text = sub.text
        print(sub_text)
    for add in soup.findAll('ul', {'class': 'dotted-list'}):
        add_text = add.text
        print(add_text)


spider(380)


#	"https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?page="
#    40,   https://www.otodom.pl/sprzedaz/mieszkanie/sopot/?search%5Bdist%5D=0&page=2
# 160, https://www.otodom.pl/sprzedaz/mieszkanie/gdynia/?search%5Bdescription%5D=1&search%5Bdist%5D=0&page=2
sys.stdout.close()
