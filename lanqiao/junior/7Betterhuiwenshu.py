n = int(input())

for i in range(10000, 1000000):
    i_sum = 0
    i_str = str(i)
    for j in i_str:
        i_sum = i_sum + int(j)
    if i_sum == n:
        if i_str == i_str[::-1]:
            print(i)

