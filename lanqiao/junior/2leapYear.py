'''
给定一个年份，判断这一年是不是闰年。

当以下情况之一满足时，这一年是闰年：

1. 年份是4的倍数而不是100的倍数；

2. 年份是400的倍数。

其他的年份都不是闰年。
输入包含一个整数y，表示当前的年份。
输出一行，如果给定的年份是闰年，则输出yes，否则输出no。
'''
year = int(input())
if year % 4 == 0 or (year % 100 != 0 and year % 4 == 0):
    print('yes')
else:
    print('no')
    