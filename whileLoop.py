# 循环
print()
i = 0
while i < 10:
    print(i)
    i += 1
# 执行了10次
i = 1
while i <= 10:
    print(i)
    i += 1
print('----------------------------------')
# 执行了10次，用的小于等于
print(f'1+2+3+......+100\n', end='')
print('----------------------------------')
i = 1
result = 0
while i <= 100:
    result = result+i
    i = i+1
print(result)
print('----------------------------------')
# 条件控制
i = 1
result = 0
while i <= 100:
    if i % 2 ==0:
        result = result+i
    else:
        pass
    i = i+1
print(result)
print('----------------------------------')
# 计数器控制
i = 0
result = 0
while i <= 100:
    result = result + i
    i = i + 2
print(result)
print('----------------------------------')
i = j = 0  # 计数器 = 0
while i < 5:  # 有5行
    j = 0  # 行内的循环
    while j < 5:  # 每一行有5个
        print('*', end='')
        j = j + 1
    print('\n', end='')  # 打完得换行
    i = i + 1
print('----------------------------------')
i = j = 0
while i < 5:  # 一共有5行
    j = 0  # 行内的循环
    while j < i:  # 行数等于星星的个数
        print('*', end='')  # 不换行
        j = j + 1  # 每一行内循环的次数等于星星个数
    print('\n', end='')  # 每一行换行
    i = i + 1
print('----------------------------------')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} x {i} = {i*j}\t', end='')
        j = j + 1
    print()
    i = i + 1
# while...else语句，可以用来判断循环是否正常，for语句也可以用来检查循环是否正常进行
i = 5
while i <= 10:
    if i == 4:
        print('不打印4')
        break
    print(i)
    i = i + 1
else:
    print('打印完了，里面没有4')




