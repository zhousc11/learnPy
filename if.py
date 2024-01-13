print(f'Internet Cafe access system')
print(f'---------------------------')
age = input(f'Enter your age: ')

try:
    age = int(age)
    if age >= 18:
        print(f'You are an adult, Welcome!')
    else:
        print(f'You are a minor, Sorry!')
except ValueError:
    print(f'Invalid age!')
    exit()
print(f'---------------------------', end='\n\n')

while True:
    print('Internet cafe entering system')
    print('-----------------------------')
    age1 = input('Enter your age: ')
    try:
        age1 = int(age1)
    except ValueError:
        print('Invalid age!')
        continue
    if age1 >= 18:
        print('You are an adult, Welcome!')
        # exit()
        break
    else:
        print('You are a minor, Sorry!')
        # exit()
        break

print('-----------------------------', end='\n\n')

money = True
seat = False

if money:
    print('You can buy a ticket!')
    if seat:
        print('You can sit down!')
    else:
        print('You can stand!')
else:
    print('You can not buy a ticket!')
