import requests
from random import randint

def htmlStringProvider(url):
  # opener = urllib.build_opener()
  # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  # res = opener.open(url)
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(randint(30, 72))+'.0.2171.95 Safari/537.36'}
  res = requests.get(url, headers=headers)
  return res.text
