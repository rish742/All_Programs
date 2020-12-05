max = None
min = None
#while loop
while True :
    num = input('Enter a number : ')
    if num == 'done':
        break
    try :
        n = int(num)
    except :
        print('Invalid input')
        continue
    if max is None and min is None :
        max = n
        min = n
    else :
        if max < n :
            max = n
        if min > n :
            min = n
print('Maximum is',max)
print('Minimum is',min)
