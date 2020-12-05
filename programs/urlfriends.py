import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter Count: ')
pos = input('Enter Position: ')

count = int(count)
pos = int(pos)

while count != 0 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    c = 0;
    tags = soup('a')

    for tag in tags:
        url = tag.get('href', None)
        cont = tag.contents[0]
        c += 1
        if c == pos :
            print('Retriving :',url)
            break


    count -= 1
print('----------------------------------')
print('Last name :',cont)
print('----------------------------------')
