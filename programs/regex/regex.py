import re
#name  = input("Enter file name")
name = 'mbox-short.txt'
fh = open(name)
for line in fh:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)
