__author__ = 'Сафиулин Салават Тельманович'

# Задача-5: Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

list1 = [randint(0, 1000) for i in range(randint(0, 10))]
str1 = ' '.join(map(str, list1))
print('Строка чисел для записи в файл: ', str1)
user_file = open('text_5.txt', 'w+')
user_file.write(str1 + '\n')
user_file.seek(0)
str2 = user_file.read()
user_file.close()
list2 = str2.split()
sum1 = 0
for i in list2:
    sum1 += int(i)
print('Сумма чисел из файла: ', sum1)
