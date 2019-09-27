import random

name = input('请输入游戏名：')

with open ('d:\Python\guess.txt')as f:
    lines = f.readlines()

dict_data = {}    #字典记录所有游戏数据
for line in lines:
    data = line.split()
    dict_data[data[0]] = data[1:]    #data[0]为用户名，data[1:]为游戏数据
    print(dict_data)

game_data = dict_data.get(name)
if not game_data:    #如果没有记录，则初始化数据
    game_data = [0,0,0]


total_games = int(game_data[0])    #游戏总轮数
avg_times = float(game_data[1])    #统计平均猜测次数
best_guess = int(game_data[2])    #统计每轮游戏最快猜中次数


print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_games,avg_times,best_guess))    #游戏开始前，显示用户的游戏数据
print('==========欢迎进入游戏==========')

choice = int(input('1 开始游戏 2 好的，再见！\n'))

if choice == 1: 
    times = 0    #每次游戏轮数
    avg_times = 0    
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
            total_games += times
            avg_times = times/count
            #print(total)
            fast_guess = total[0]    #最快猜中次数
            for i in total:
                if i < fast_guess:
                    fast_guess = i
            #print(fast_guess)
            print(name+',此次您一共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(times,avg_times,fast_guess))    #此次游戏最好记录     
            break

    totalfast_guess = []        
    totalfast_guess.append(fast_guess)
    best_guess = totalfast_guess[0]    #更新至今为止游戏最快猜中次数
    for i in totalfast_guess:
        if i < best_guess:
            best_guess = i
        print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_games,avg_times,best_guess))    #全部游戏最好记录
else:
    print('好的，再见！')

    

dict_data[name] = [str(total_games),str(avg_times),str(best_guess)]
fin_result = ''
for x in dict_data:
    line = x+' '+' '.join(dict_data[x])+'\n'
    fin_result += line

    

out = open('guess.txt','w')
out.write(fin_result)
out.close()


    

