num = 20
print('Guess what I think?')
for answer in range (1,4):

    answer = int(input())

    if answer > num:
        print('too big!')
    elif answer < num:
        print('too small!')
    else:
        print('good!')
