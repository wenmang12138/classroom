with open('d:/report.txt.txt') as f:
    lines = f.readlines()
    print(lines)

subject = []      #处理第一行主题，添加名次，总分，平均分     
subject = lines[0].split()
subject.insert(0,'名次')
subject.append('总分')
subject.append('平均分')
print(subject)

all_grades = []
grades = []           
for line in lines[1:]:      #处理第二行学生成绩            
    grades = line.split()
    
    sum = 0
    for data in grades[1:]:      #grades[1:]是所有成绩列表
        sum += int(data)
        
    grades.append(str(sum))      #计算总分
    grades.append(str('%.2f'%(sum/9)))      #计算平均分              
    all_grades.append(grades)      #处理过的成绩添加到新列表
    
new_grades = sorted(all_grades, key=lambda x: x[-2], reverse=True)      #根据倒数第二列总分进行排序
print(new_grades)

average_score = []      #汇总每一科目的平均分和总平均分
for i in range(1,len(new_grades[0])):
    subject_average = 0
    for j in new_grades:
        subject_average += float(j[i])
    average = float('%.2f'%(subject_average/(len(new_grades))))
    average_score.append(str(average))
average_score.insert(0,'平均')
new_grades.insert(0,average_score)    
#print(average_score)
#print(new_grades)

for a in range(0,len(new_grades)):      
    new_grades[a].insert(0,str(a))      #添加名次
#print(new_grades)

for b in range(2,len(new_grades)):      #替换不及格
    for c in range(2,10):
        if float(new_grades[b][c])<60:
            new_grades[b][c]='不及格'  
#print(new_grades)
new_grades.insert(0,subject)
#print(new_grades)

fin_result = []      #将列表转化为字符串
for i in new_grades:
    fin = '  '.join(i)
    print(fin)
    fin_result.append(fin)

#for i in new_grades:      #另一种方法将列表转化为字符串
    #for j in i:
        #print(j,end = '  ')
    #print()



    
output = open('result_report.txt', 'w')
output.write('\n'.join(fin_result))
output.close()  

               

