#!/usr/bin/python3

from homePageScrapper import homePageScrapper as hps
from htmlStringProvider import htmlStringProvider
from pageScrapper import pageScrapper as ps

print("\n\n=============================")
print('Welcome to python web scraper')
print("=============================\n\n")
# homeUrl = 'https://www.amazon.in/b/?node=5403404031&ref_=Oct_CateC_2083423031_3&pf_rd_p=6b1b34ad-a02a-5f82-9297-20da055c3e65&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=2083423031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=K98ZHPW3H6XK5BK0185C&pf_rd_r=K98ZHPW3H6XK5BK0185C&pf_rd_p=6b1b34ad-a02a-5f82-9297-20da055c3e65'
# htmlString = htmlStringProvider(homeUrl)
for index in range(50, 61):
  print('Fetching links from page ' + str(index))
  url = "https://www.amazon.in/s?rh=n%3A976442031%2Cn%3A%21976443031%2Cn%3A2083423031%2Cn%3A5403404031&page=" + str(index)
  htmlString = htmlStringProvider(url)
  ps(htmlString, index)
# hps(htmlString)
# scrapper = Scraper(htmlString)
# scrapper.printHTML()
