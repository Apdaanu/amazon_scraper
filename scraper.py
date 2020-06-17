from bs4 import BeautifulSoup as bs
import urllib
import os
from htmlStringProvider import htmlStringProvider

def scraper(fileName):
  file = open(os.path.join('data', fileName), 'r')
  newFileName = fileName.replace(".txt", "")
  resFile = open(os.path.join('data', fileName + "_Result.csv"), 'w')
  resFile.write('"Name", "Rating", "Description"\n')
  line_count = 0
  for line in file:
    if line_count == 0:
      line_count+=1
      continue
    print('\n\nfetching link ' + str(line_count) + ' please wait...\n\n')
    line_count+=1
    arr = line.split("~")
    name = arr[0].replace("'", "")
    link = arr[1].replace("'", "").replace("\n", "")
    appendString = '"'+name+'"'+','
    htmlString = htmlStringProvider(link)
    soup = bs(htmlString, 'lxml')
    targetRating = soup.find(id="acrPopover")
    rating = targetRating.get("title")
    appendString += '"'+rating+'"'+','+'"'
    targetDesc = soup.find(id="feature-bullets")
    spanArr = targetDesc.findAll('span', {'class': 'a-list-item'})
    for span in spanArr:
      text = span.text
      res = text.replace("'", "").replace("\n", "")
      appendString += res + "\n"
    appendString += '"\n'
    resFile.write(appendString)
  file.close()
  resFile.close()

