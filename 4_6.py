from itertools import count
from itertools import cycle

# first task

my_list1 = []
int1 = int(input('Введите начальное значение последовательности '))
int2 = int(input('Введите конечное значение последовательности '))
for el in count(int1):
    if el > int2:
        break
    else:
        my_list1.append(el)
print(my_list1)

# Second task
str_trim = ''
my_str1 = input('Введите любую строку ')
int1 = int(input('Какая должна быть длина строки? '))
i = 1
for el in cycle(my_str1):
    if i > int1:
        break
    str_trim += el
    i += 1
print(str_trim)
