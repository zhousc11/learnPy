# input用来输入
a = input("Input a float number:")
# 默认的输入是字符串，需要转换
a = float(a)
b = bool(input("Input a bool value:"))
print(f'The number is {a}, remain 2 digits: {a:.2f}')
print('The number is %s, remain 2 digits: %.2f' % (a, a))
print(f'Bool value is {b}')
