import random
from functools import reduce

# 2.1
new_list = random.sample(range(0, 10), 5)
print('№2.1')
print(new_list)
print('---------------------------------')

# 2.2
max_value = list(filter(lambda a: a == max(new_list), new_list))
print('№2.2')
print(*max_value)
print('---------------------------------')

# 2.3
sum = reduce(lambda a, b: a + b, new_list)
print('№2.3')
print(sum)
print('---------------------------------')

# 2.4
mult = reduce(lambda a, b: a * b, new_list)
print('№2.4')
print(mult)
print('---------------------------------')

# 2.5
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

fact = factorial(*max_value)
print('№2.5')
print(fact)
print('---------------------------------')

# 2.6
def random_string(len):
    letters = 'AaBbCcDdEe'
    str = ''.join(random.choice(letters) for i in range(len))
    return str

new_str = random_string(*max_value)
print('№2.6')
print(new_str)
print('---------------------------------')

# 2.7
def register(str):
    str_arr = list(str)
    upper_letters = list(filter(lambda x: x.isupper(), str_arr))
    sum_upper = len(upper_letters)
    lower_letters = list(filter(lambda x: x.islower(), str_arr))
    sum_lower = len(lower_letters)
    return f'Заглавных букв: {sum_upper}, строчных: {sum_lower}'

print('№2.7')
print(register(new_str))
print('---------------------------------')

# 2.8
def PrintPascalTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [a + b for a, b in zip([0] + row, row + [0])]

print('№2.8')
PrintPascalTriangle(7)