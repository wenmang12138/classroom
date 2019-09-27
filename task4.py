import random

choice = int(input('1 开始游戏 2 好的，再见！\n'))
if choice == 1:
    times = 0    #游戏轮数
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
                #bingo = True
                print('第%d次猜中！'%count)
                break
        choice2 = input('=======继续游戏or退出======\n')
        if choice2 !='继续游戏':
            print('您一共玩了%d轮，胜负率为%.2f。'%(times,times/count))
            break
else:
    print('好的，再见！')
        
        

    

