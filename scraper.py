from bs4 import BeautifulSoup as bs
import os
from htmlStringProvider import htmlStringProvider

def scraper(fileName):
  file = open(os.path.join('data', fileName), 'r')
  newFileName = fileName.replace(".txt", "")
  resFile = open(os.path.join('data', fileName + "_Result.csv"), 'a')
  line_count = 1
  for line in file:
    print('\n\nfetching link ' + str(line_count) + ' please wait...\n\n')
    line_count+=1
    arr = line.split("~")
    name = arr[0].replace("'", "")
    link = "https://amazon.in" + arr[1].replace("'", "").replace("\n", "")
    appendString = '"'+name+'"'+','
    htmlString = htmlStringProvider(link)
    soup = bs(htmlString, 'lxml')
    targetRating = soup.find(id="acrPopover")
    if(targetRating):
      rating = targetRating.get("title")
    else:
      rating = "none"
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

