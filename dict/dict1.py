# 创建字典
dict1 = {}
dict2 = {'name': 'Joe', 'age': '21', 'hobby': 'Cycling'}
dict3 = dict()
set1 = set()

dict1['name'] = 'Joe'
dict2['name'] = 'JoeJoe'  # 增加字典中的元素，如果已经存在，则修改

print(dict1['name'])
print(dict2['name'])

del dict2['age']  # 删除元素
dict2['age'] = '21'  # 给她加回去

dict1.clear()  # 清空字典 {}

print(dict2.get('age'))  # 21

print('-' * 10)

print(dict2.keys())  # 输出keys
print(dict2.values())  # 输出值
print(dict2.items())  # 输出整个字典
print(dict2)
print('-' * 10)

# 遍历字典操作
for key in dict2.keys():
    print(key)
print('-' * 10)

for value in dict2.values():
    print(value)

for key, value in dict2.items():
    if key == '21' or value == '21':
        print('ok')

age = '21'
# 等价于in
if age in dict2:
    print('yes')
else:
    print('no')
# 直接使用in运算符，检查的是key，而不是value
