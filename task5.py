import random
name = input()
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
            print('玩家'+name+',您一共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(times,times/count,fast_guess))
            break
else:
    print('好的，再见！')



data = ('玩家'+name+',您一共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(times,times/count,fast_guess))
            

out = open('guess.txt','w')
out.write(data)
out.close()
        
