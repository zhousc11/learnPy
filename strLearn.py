str1 = 'HelloWorld'
str2 = '1a2b3c'
str3 = '''I'm Tom'''
'''
"I'm Tom"可以
'I\'m Tom也可以'
'''
print(str3)
# 字符串的下标操作
print(str1[1])  # e
print(str1[0])  # H

# 切片操作，字符串、列表、元组都支持切片
# 格式：开始位置，结束位置，步长
print(str2[0:4])  # 1a2b，只有四个字符
print(str2[0:1])  # 1，只有一个字符，结束的那个不算
print(str2[0:-1])  # 1a2b3
print(str2[::-1])  # 倒数着取字符
print(str2[::-2])  # 从倒数第一个，步长为2，结果为cba
# 切片操作不指定参数就是从头到尾，步长为1

# 字符串的查找，1a2b3c
print(str2.find('2b'))  # 2
print(str2.find('2b',2, 5))  # 虽然指定了查找范围，但是还是返回的是在整个字符串的位置，和查找范围无关
print(str2.find('666'))  # -1
print(str2.find('1a', 2,5))  # -1，不在查找范围

# index和这个查找差不多，不过会报错，而不是返回-1，所以需要异常处理
try:
    print(str2.index('666'))
except ValueError:
    success = 0
    print('字符串未找到')

print(str1.rfind('and'))
print(str1.rindex('World'))
