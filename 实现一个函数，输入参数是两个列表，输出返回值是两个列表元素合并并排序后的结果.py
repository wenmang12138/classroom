#实现一个函数，输入参数是两个列表，输出返回值是两个列表元素合并并排序后的结果

def add_list(list1,list2):
    total_list = list1+list2
    total_list.sort()
    return total_list
print(add_list([1,3,5],[2,4,6]))
    

def add_list(list1,list2):
    list1.extend(list2)
    list1.sort()
    return list1
print(add_list([1,3,5],[2,4,6]))
