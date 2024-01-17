# 字符串的修改，例如大小写转换什么的
str1 = 'this is a cat. That is my computer.'


def capital_letter(str0):
    ok_str = str0.capitalize()
    return ok_str


def title_allletter(str0):
    ok_str = str0.title()
    return ok_str


def lowerletter(str0):
    return str0.lower()


def upper(str0):
    return str0.upper()


print(f'Origin: {str1}')
print(capital_letter(str1))  # 首字母大写了
print(title_allletter(str1))  # 每个单词首字母大写了
print(lowerletter(str1))  # 所有字母小写了
print(upper(str1))  # 所有字母大写了
str2 = '  ' + str1 + '   '
print()
print(f'Original: {str2}')
print(str2.lstrip())
print(str2.rstrip())
print(str2.lstrip().rstrip())  # 连续调用也是可以的
print(str2.strip())  # 直接把两边的空格全部给去除了
