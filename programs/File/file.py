fh = open('file.txt')
for line in fh:
    print(line.rstrip().upper())
