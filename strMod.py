# 字符串的修改操作
str1 = '1a2b3c4d'
str1.replace('1a', '2b')
print(str1)  # 和下面的一样
print(str1.replace('1a', '2b'))

str2 = 'This is a peach. And This is a pink peach. That is a pear. These are apples.'
str2.replace('This', 'That', 10)
print(str2)  # 输出的还是没有修改的，因为实际上并未修改str2变量
print(str2.replace('This', 'That', 10))  # 三个参数，旧的字符串，新的字符串，还有替换次数，比如有多个词语

list2 = str2.split()  # 空白
print(list2)

list2 = str2.split('.')
print(list2)

list2 = str2.split('.', 2)
print(list2)

print('_'.join(list2))

str3 = 'Sorry about that'
str3 = str3.split(' ')
print(str3)
