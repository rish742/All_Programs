#fn = input("Enter File name : ")
try:
    fh = open('words.txt')
except:
    print('No file with that name!!')
    quit()
for line in fh :
    l = line.rstrip()
    lu = l.upper()
    print(lu)
