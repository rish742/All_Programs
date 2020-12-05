fh = open('file.txt')
for line in fh:
    words = line.split()
    print(words[2])
