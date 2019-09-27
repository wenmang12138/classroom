#统计下这段文字里，不同单词出现的次数

s = '''
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
'''

word = s.split()
count = {}
for w in word:
    if w in count:
        count[w]+= 1
    else:
        count[w] = 1
print(count)
