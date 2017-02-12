import urllib

url = 'http://www.google.com'
stream = urllib.urlopen(url)
res = stream.read()
print res