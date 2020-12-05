def con(text) :
    p = text.find(':')
    dis = text[p-2:p]
    return dis

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try :
    fh = open(name)
except :
    print('File Invalid!')
    quit()

count = dict()
counts = list()
lst = list()
for line in fh :
    if not line.startswith("From") or  line.startswith("From:") :
        continue
    a = con(line)
    counts.append(a)
for i in counts :
        count[i] = count.get(i,0)+1
b = sorted([(x,y) for x,y in count.items()])
for x,y in b:
    print(x,y)
