'''
输入A、B，输出A+B。
输入一行，两个整数，空格分隔，输出A+B的结果
'''
ab = input()
a, b = ab.split(' ')  # 这是解包操作，当元组的元素个数和变量的个数相同时，可以使用解包操作
# print(ab.split())  # split是字符串的方法，返回一个列表，默认是以空格分隔
a = int(a)
b = int(b)
print(a + b)
