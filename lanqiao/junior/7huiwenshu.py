'''
123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
'''
n = int(input())
result_list = []

for i in range(10000, 1000000):
    i_str = str(i)
    sum = 0
    for j in i_str:
        sum = sum + int(j)
    if sum == n:
        if (len(str(i)) == 5 and str(i)[0:2] == str(i)[-2:]) or (len(str(i)) == 6 and str(i)[0:3] == str(i)[-3:]):
            result_list.append(i)        
            print(f'{i}')
            