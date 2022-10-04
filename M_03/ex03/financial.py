#!/usr/bin/env python

from sys import argv
import requests
from bs4 import BeautifulSoup
import time


if __name__ == '__main__':
    if len(argv) == 3:
        ticker = argv[1].lower()
        my_field = argv[2]
        url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
        response = requests.get(url, headers={'User-Agent': 'Custom'})
        if response.status_code == 404:
            raise Exception('There is no such reference')
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string
        if title == 'Symbol Lookup from Yahoo Finance':
            raise Exception('ticker was not found')
        quotes = soup.find_all('span')
        caunt = 99
        s = []
        time.sleep(3)
        for quote in quotes:
            if quote.text == my_field:
                caunt = 0
            if caunt < 6:
                s.append(quote.text)
                caunt += 1
        print(tuple(s))
