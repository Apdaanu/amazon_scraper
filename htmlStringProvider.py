import urllib

def htmlStringProvider(url):
  return urllib.request.urlopen(url)
