# Use the file name mbox-short.txt as the file name
def con(text) :
    p = text.find(':')
    dis = text[p+1:]
    f = float(dis)
    return f


#fname = input("Enter file name: ")
fh = open('mbox-short.txt')
avg = 0.0
s = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    l = con(line)
    count = count + 1
    s = s + l
avg = s/count
print('Average span confidence = ',avg)
