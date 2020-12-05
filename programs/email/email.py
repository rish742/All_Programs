fh = open('mbox-short.txt')
#fn = input("Enter file name : ")
#fh = open(fn)
count = 0
for line in fh:
    if not line.startswith("From") :
        continue
    if line.startswith("From:"):
        continue
    count += 1
    x = line.split()
    print(x[1])
print("There were", count, "lines in the file with From as the first word")
