#输入一个数输出对应高度的三角形

num = int(input())
for i in range (1,num+1):
    print(' '*(num-i)+'*'*(2*i-1))

for i in range(0,num+1):
    print(' '*(num-i),end='')
    print('*'*(i*2-1)) 

for i in range(0,num+1):
    for j in range(num-i):
        print(' ',end='')
    for j in range(i*2-1):
        print('*',end='')
    print()



for i in range(0,num+1):
    for j in range(num-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')   #或者print('*',end=' ')
    print()


for i in range (1,num+1):
    print(' '*(num-i)+'* '*i)

for i in range(0,num+1):
    print(' '*(num-i),end='')
    print('* '*i) 
