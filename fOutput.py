# 格式化输出f
age = 21
name = 'Joe'
weight = 67.5
student_id = 2021116000649
height = 184.5
print('My name is %s' % name)
print('My student ID is %d' % student_id)
print('My age is %d' % age)
print('My weight is %.2f' % weight)
# 使用一下括号
print('This is test calculate:\nMy age is %d' % (age + 1))

# 汇总
print('My name is %s, my age is %d, my student ID is %d, my weight is %.1f, and Fake height is %d' % (
    name, age, student_id, weight, height + 5))

# 使用f函数试试，引号前面+f然后中间变量用{}包起来，遇到小数位要保留，就加冒号:.2f
print(
    f'My name is {name}, my age is {age}, my student ID is {student_id}, my height is {height}, and my weight is {weight:.2f} and my fake height is {height + 5}')
# 多尝试一下，要么就是前面完整的字符串，和C语言一样直接加要输出的字符串用%d，要么就是f函数，记得大括号

# 还有这个结束符号
print(age, end='666')  # 这样就没有换行符了
print('\n', end='')
print(height, end='\t')
