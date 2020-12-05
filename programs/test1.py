i=0
x = [[1,2,3],[4,5,6]]
il = len(x)
while i<il :
    print(i,"Outer loop is executed only once")
    j=0
    x1 = x[i]
    while j<=3:
        print(j,"Inner loop is executed until to completion")
        j += 1
    i += 1;
