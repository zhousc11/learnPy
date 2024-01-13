# 数据类型之间的互相转换
num = input('Input sth:')
print(f'You just input {num}')
num = int(num)
print(f'You just input {num}')

tup = (1, 2, 3)
try:
    tup.append(4)
except AttributeError:
    print(f'This is a tuple, which cannot be appended.')
    print(AttributeError)
tup = list(tup)
tup.append(4)
print(tup)

tup = str(tup)
print(type(eval(tup)))
