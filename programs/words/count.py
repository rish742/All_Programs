fh = open('file.txt')
d = dict()
for line in fh:
    words = line.split()
    for word in words:
        d[word] = d.get(word,0)+1

lar = -1
theword = None
for k,v in d.items():
    print(k,v)
    if v > lar :
         lar = v
         theword = k
