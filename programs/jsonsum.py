import json
import urllib.request
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL :")
fhand = urllib.request.urlopen(url)
data = fhand.read().decode()
info = json.loads(data)
d = info['comments']
print("Count :",len(d))
s = 0
for item in d:
    s += item['count']
print("Sum :",s)
