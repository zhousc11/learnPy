# 列表的基本操作
name_list = ['Joe', 'Tom', 'Mary', 'Steve', 'Joe']
result = 'Joe' in name_list
print(result)  # in可以算是一个运算符，然后用于判断其中是否有某个元素
print('-------------------')
print(name_list.count('Joe'))  # 2，因为joe出现了两次

print(name_list.index('Joe'))

try:
    print(name_list.index('Joe', 1, 2))
except ValueError as result1:
    print('No such item!')
    print(result1)

