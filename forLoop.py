# for可以用来遍历
seperate = '\n----------------------\n'
str1 = 'zhousc66'
for i in str1:
    print(i, end=' ')
print(seperate, end='')
# 加入条件判断
str2 = 'zhshch2011'
for i in str2:
    if i != '2':
        print(i, end=' ')
    else:
        continue
print(seperate,end='')
for i in str2:
    if i == '2':
        print('遇到2不打印',end='')
        break
    print(i, end=' ')
print(seperate, end='')
sum = 5
for i in range(sum):
    print(i)
print(seperate, end='')
testInt = int(input('Enter a number:'))
for i in range(testInt):
    if i == 4:
        print('遇到4不打印')
        break
    print(i)
else:
    print('打印完了，里面没有4')
print(seperate, end='')
# 控制循环，遇到4直接跳过
for i in range(10):
    if i == 4:
        continue
    else:
        print(i)
print(seperate,end='')
# 控制循环，遇到4直接终结
for i in range(10):
    print(i)
    if i == 4:
        break
print(seperate, end='')
for i in range(10):
    if i == 4:
        break
    print(i)
'''
break语句就是完全终止了整个循环，哪怕是有else语句也不会执行，但是continue就是跳过当次循环，比如满足了某个特定条件
'''