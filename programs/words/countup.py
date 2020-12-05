fh = open('file.txt')
d = dict()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        d[word] = d.get(word,0)+1

tmp = list()
for k,v in d.items() :
    new = (v,k)
    tmp.append(new)

tmp = sorted(tmp, reverse=True)

for v,k in tmp :
    print(k,v)
