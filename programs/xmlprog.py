import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL :")
fhand = urllib.request.urlopen(url)
data =''
for line in fhand:
    data += line.decode()

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print('Count:', len(lst))

s = 0
for item in lst:
    s += int(item.find('count').text)
print('Sum :',s)
