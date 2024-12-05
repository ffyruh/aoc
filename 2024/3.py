input = open('3.in', 'r')
data = input.read()
input.close()

import re

# p1
sum = 0
a = re.findall("mul\([\d]+,[\d]+\)", data)
for i in a:
    a,b = [int(x) for x in i[4:-1].split(',')]
    sum += a*b
print(sum) # 164730528

# p2
sum = 0
a = re.findall("don't\(\)|do\(\)|mul\([\d]+,[\d]+\)", data)
flag = True
for i in a:
    if i[:3] == 'don':
        flag = False
    elif i[:3] == 'do(':
        flag = True
    else:
        if flag:
            a,b = [int(x) for x in i[4:-1].split(',')]
            sum += a*b
print(sum) # 70478672