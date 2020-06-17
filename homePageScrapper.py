from bs4 import BeautifulSoup as bs
from scraper import scraper

def homePageScrapper(html):
  soup = bs(html, 'lxml')
  targetSection = soup.find(id="mainResults")
  targetDivs = targetSection.findAll('div', {'class': 's-item-container'})
  links = {}
  for div in targetDivs:
    itemLink = div.find('a', {'class' : 'a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal'})
    itemName = div.find('h2', {'class' : 'a-size-base s-inline s-access-title a-text-normal'})
    links[itemName.text] = itemLink.get('href')

  file1 = open("data/homePageLinks.csv", "w")
  file2 = open("data/homePageLinks.txt", "w")
  file1.write('"Product Name","Link",\n')
  for key in links:
    fileEnrty = '"'+key+'"'+','+'"'+links[key]+'"'+'\n'
    file1.write(fileEnrty)
    file2.write(key + '~' + links[key] + '\n')
  file1.close()
  file2.close()
  print('\ncreated a file data/homePageLinks.csv\n')
  scraper("homePageLinks.txt")