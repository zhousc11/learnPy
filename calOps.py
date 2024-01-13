# 运算符的操作
a = 85
b = 5
c = -1
d = 0

print(type(c))
print(f'a + b = {a + b}')

print(f'a - b = {a - b}')

print(f'a * b = {a * b}')

print(f'a / b = {a / b}')

print(f'a / c = {a / c}')

print(f'a // c = {a // c}')

print(f'a % b = {a % b}')

print(f'a ** b = {a ** c}')  # 乘方

# x, y, z = 1, 2, [1, 2, 3]

# 逻辑运算符只输出True或False
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# and, or, not
print(True and False)
print(True or True)
print(False and True)

print(True or True)
print(True or False)
print((False or True))
print(False or False)

print(not True and False)
print(not False)

x, y, z = 0, 1, 2
print(x and y)
print(x or y)
print(y and z)
print(z and y)

print(x or y)
print(y or x)
print(y or z)