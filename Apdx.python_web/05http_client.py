import urllib.request, urllib.parse, urllib.error

url = 'http://www.google.com'
stream = urllib.request.urlopen(url)
res = stream.read()
print(res)