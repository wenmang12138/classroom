#生成10个随机数，输出里面第二大的数

import random
num_list = []
for i in range(10):
    num = random.randint(1,100)
    num_list.append(num)
print(num_list)
num_list.sort(reverse=True)
print(num_list[1])


first = 0
second = 0
a = []
for i in range(10):
    r = random.randint(1,100)
    print(r, end=' ')
    a.append(r)
    if r > first:
        second = first
        first = r
    elif r > second:
        second = r
a.sort()
print(a[-2])
print(second)
