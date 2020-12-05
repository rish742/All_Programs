import re
ta = input("sample or actual:")
if ta == 'sample':
    name = 'regex_sum_42.txt'
elif ta == 'actual':
    name = 'regex_sum_970554.txt'
try:
    fh = open(name)
except:
    print("Invalid file!!!")

sum = 0
for line in fh:
    nums = re.findall('[0-9]+',line)
    for num in nums:
        sum += int(num)

print(sum)
