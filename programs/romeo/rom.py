fh = open('romeo.txt')
#fname = input("Enter file name: ")
#fh = open(fname)
i = 0
lst = list()
x = list()
xlst = list()
for line in fh:
     l1 = line.split()
     lst.append(l1)
while i < len(lst):
    j = 0
    x = lst[i]
    while j < len(x):
        xlst.append(x[j])
        j += 1
    i += 1
xlst.sort()
xlst = list(dict.fromkeys(xlst))
print(xlst)
