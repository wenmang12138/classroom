import random

with open ('d:\Python\guess.txt')as f:
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        print(data)

dict_data ={data[0]:(''.join(data[1:]))}
print(dict_data)
    

name = input()
total_times = 0    #游戏总轮数
totalfast_guess = []    #统计每轮游戏最快猜中次数到列表
game_data = dict_data.get(name)

if not game_data:
    print([0,0])
else:
    total_times += 1
    print('==========欢迎再次游戏==========')
    
            
choice = int(input('1 开始游戏 2 好的，再见！\n'))
if choice == 1: 
    times = 0    #游戏轮数
    total = []    #统计猜中次数到列表
    while True:
        num = random.randint(1,100)
        print('Guess what I think?')
        count = 0    #猜中次数
        times += 1
        while True:
            count += 1
            answer = int(input())
            if answer < num:
                print('too small!')
            elif answer > num:
                print('too big!')
            else:
                print('bingo!')
                print('第%d次猜中！'%count)
                total.append(count)
                break
        choice2 = input('=======继续游戏or退出======\n')
        if choice2 !='继续游戏':
            total.append(count)
            #print(total)
            fast_guess = total[0]    #最快猜中次数
            for i in total:
                if i < fast_guess:
                    fast_guess = i
            #print(fast_guess)
            print(name+',此次您一共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(times,times/count,fast_guess))    #此次游戏最好记录     
            break

        
totalfast_guess.append(fast_guess)
best_guess = totalfast_guess[0]    #更新至今为止游戏最快猜中次数
for i in totalfast_guess:
    if i < best_guess:
        best_guess = i
    print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_times+times,(total_times+times)/count,best_guess))    #全部游戏最好记录
else:
    print('好的，再见！')
    

data = (name+',您总共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_times+times,(total_times+times)/count,best_guess))

out = open('guess.txt','w')
out.write(data)
out.close()


    

