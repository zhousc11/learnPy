# 字符串的修改操作
# replace, split, join
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

print('_'.join(list2))  # 使用前面的字符串把后面的拼接起来

str3 = 'Sorry about that'
str4 = str3.split(' ')  # 以空格为分隔符，分离尽可能多的次数
print(str3)
print(str3.split(' ', 1))

# join是用来组合字符串的，意思就是在后面的序列中插入前面的字符串
sentence = ' '.join(['This', 'is', 'water'])
print(sentence)

str5 = 'hello'
sentence1 = str5.join(['This', 'is'])  # Thishellois
print(sentence1)

# count方法
print(str2.count('This', 0, 99))
