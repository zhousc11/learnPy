for i in range(100, 1000):
    i_str = str(i)
    if int(i_str[0]) ** 3 + int(i_str[1]) ** 3 + int(i_str[2]) ** 3 == i:
        print(i)
