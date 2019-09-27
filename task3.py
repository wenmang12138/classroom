import random
num = random.randint(1,100)
print('Guess what I think?')
bingo = False
count = 0
while bingo == False:
    answer = int(input())
    count += 1
    if answer > num:
        print('too big!')
    elif answer < num:
        print('too small!')
    else:
        print('bingo!')
        print('你第%s次猜对了!'%count)
        break
