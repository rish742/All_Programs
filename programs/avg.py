count = 0
sum = 0.0
avg = 0.0
while True:
    num = input('Enter a number :')
    if num == 'exit':
        break
    try:
        n = float(num)
    except:
        print('Bad Data Invalid Input')
        continue
    sum += n
    count += 1

avg = sum/count
print(sum,count,avg)
