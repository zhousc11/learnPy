# 输出列表中第二大的数字
import random
list1 = []
for i in range(0, 10):
    int1 = random.randint(1, 100)
    list1.append(int1)
print(list1)

# 输出第二大的
i = list1.index(max(list1))
print(f'最大的数字的索引是{i}')
del list1[i]
print(max(list1))
