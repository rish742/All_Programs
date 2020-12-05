#handle = open('mbox-short.txt')
fn = input('Enter File name: ')
try :
    fh = open(fn)
except :
    print('File Invalid!')
    quit()
    
counts = dict()
for line in fh :
    if not line.startswith("From") or  line.startswith("From:") :
        continue
    x = line.split()
    words = x[1]
    counts[words] = counts.get(words,0) + 1

bc = None
bw = None
for word,count in counts.items() :
    if bc is None or count > bc :
        bw = word
        bc = count
print(bw,bc)
