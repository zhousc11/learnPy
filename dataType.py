# 整数
a = 1
print(type(a))
# 浮点数
b = 1.1
print(type(b))
# 字符串
c = 'hello world'
print(type(c))
# 布尔值
d = False
print(type(d))
# 列表
e = [1, 2, 3, 4, 5]
print(type(e))
# 元组
f = (1, 2, 3, 4, 5)
print(type(f))
# 字典
g = {'name': 'Joe', 'age': 21, 'Male': True}
print(type(g))

# 列表和元组都是可以迭代的，都是可以被遍历的
# 但是元组是不可变的，列表是可变的
# 比如 e.append(6) 是可以的，但是 f.append(6) 是不可以的

h = [1, 1, 2, 3, 4, 6]
h = set(h)
print(h)

i = None
if i:
    print('i is True')
else:
    print('i is False')