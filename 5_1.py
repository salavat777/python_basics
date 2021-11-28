__author__ = 'Сафиулин Салават Тельманович'

# Задача-1: Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

user_file = open('text_1.txt', 'w')
while True:
    user_str = input('Input text to file or press Enter to complete input :')
    if user_str == '':
        print('file written')
        break
    else:
        user_file.write(user_str + '\n')
user_file.close()
