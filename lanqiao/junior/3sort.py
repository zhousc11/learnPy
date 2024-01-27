'''
给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200
第一行为一个整数n。
第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
输出一行，按从小到大的顺序输出排序后的数列。
'''
n = int(input())
numbers = input()
num_list = numbers.split(' ')
# print(num_list)
num_list = [int(num) for num in num_list]  # 列表推导式的操作，遍历每一个元素并转换为int
# print(num_list)
num_list.sort()
# print(num_list)
for item in num_list[:-1]:
    print(item, end=' ')
print(num_list[-1], end=' ')
