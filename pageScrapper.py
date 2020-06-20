from bs4 import BeautifulSoup as bs
from scraper import scraper

def pageScrapper(html, index):
  soup = bs(html, 'lxml')
  targetDivs = soup.findAll('div', {'class': 'a-section a-spacing-medium'})
  print(len(targetDivs))
  links = {}
  for div in targetDivs:
    itemLink = div.find('a', {'class' : 'a-link-normal a-text-normal'})
    itemName = div.find('span', {'class' : 'a-size-medium a-color-base a-text-normal'})
    links[itemName.text] = itemLink.get('href')

  file1 = open("data/pageLinks"+str(index)+".csv", "w")
  file2 = open("data/pageLinks.txt", "w")
  file1.write('"Product Name","Link",\n')
  for key in links:
    fileEnrty = '"'+key+'"'+','+'"'+links[key]+'"'+'\n'
    file1.write(fileEnrty)
    file2.write(key + '~' + links[key] + '\n')
  file1.close()
  file2.close()
  print('\ncreated a file data/pageLinks'+str(index)+'.csv\n')
  scraper("pageLinks.txt")