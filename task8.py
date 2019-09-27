import requests

def main():    #处理游戏记录主函数
    with open ('d:\Python\guess_result.txt')as f:
        lines = f.readlines()
        dict_data = {}    #字典记录所有游戏数据
        for line in lines:
            data = line.split()
            dict_data[data[0]] = data[1:]    #data[0]为用户名，data[1:]为游戏数据
            print(dict_data)
            
    name = input('请输入游戏名：')
    game_data = dict_data.get(name)

    if not game_data:    #如果没有记录，则初始化数据
        game_data = [0,0,0]
        

    total_games = int(game_data[0])    #游戏总轮数
    avg_times = float(game_data[1])    #统计平均猜测次数
    best_guess = int(game_data[2])    #统计每轮游戏最快猜中次数
    print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_games,avg_times,best_guess))    #游戏开始前，显示用户的游戏数据

    guess_games(total_games,avg_times,best_guess,dict_data,name)    #调用处理游戏结果函


def guess(num,times=0,count=0):    #猜数字函数
    print('==========欢迎进入游戏==========')
    
    print('Guess what I think?')
    times += 1    #游戏次数增加
    while True:
        count += 1    #猜中次数增加
        answer = int(input())
        if answer < num:
            print('too small!')
        elif answer > num:
            print('too big!')
        else:
            print('bingo!')
            print('第%d次猜中！'%count)
            break
    return (times,count)


def guess_games(total_games,avg_times,best_guess,dict_data,name):    #处理游戏结果函数
    while True:
        number = requests.get('https://python666.cn/cls/number/guess/')
        game_num = number.json()
        times,count = guess(game_num)    #调用猜数字函数

        total_games += times
        avg_times = times/count
        fast_guess = []
        fast_guess.append(count)    #最快猜中次数
        fast_guess.sort()    #最快猜中次数排序
        print(fast_guess[0])
        print('此次您一共玩了%d轮，猜中率为%.2f，最快猜中次数是第%s次。'%(total_games,avg_times,fast_guess[0]))
        

        totalfast_guess = []
        totalfast_guess.append(fast_guess)
        best_guess = totalfast_guess[0]    #更新至今为止游戏最快猜中次数
        for i in totalfast_guess:
            if i < best_guess:
                best_guess = i
                print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中记录是第%s次。'%(total_games,avg_times,best_guess[0]))    #全部游戏最好记录
                break

        dict_data[name] = [str(total_games),str(avg_times),str(best_guess[0])]
        fin_result = ''
        for x in dict_data:
            line = x+' '+' '.join(dict_data[x])+'\n'
            fin_result += line

        out = open('guess_result.txt','w')
        out.write(fin_result)
        out.close()

        choice = input('=======继续游戏or退出======\n')
        if choice !='继续游戏':
            print('结束游戏！')
            print(name+',您总共玩了%d轮，猜中率为%.2f，最快猜中记录是第%s次。'%(total_games,avg_times,best_guess[0]))
            break


    
main()
    



