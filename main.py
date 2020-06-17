#!/usr/bin/python3

from homePageScrapper import homePageScrapper as hps
from htmlStringProvider import htmlStringProvider

print("\n\n=============================")
print('Welcome to python web scraper')
print("=============================\n\n")
print('Fetching links from home screen...')
homeUrl = 'https://www.amazon.in/b/?node=5403404031&ref_=Oct_CateC_2083423031_3&pf_rd_p=6b1b34ad-a02a-5f82-9297-20da055c3e65&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=2083423031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=K98ZHPW3H6XK5BK0185C&pf_rd_r=K98ZHPW3H6XK5BK0185C&pf_rd_p=6b1b34ad-a02a-5f82-9297-20da055c3e65'
htmlString = htmlStringProvider(homeUrl)
hps(htmlString)
# scrapper = Scraper(htmlString)
# scrapper.printHTML()