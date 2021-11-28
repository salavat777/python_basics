__author__ = 'Сафиулин Салават Тельманович'

# Задача-2: Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

i_line = 0
result_dict = {}  # словарь с результатами, ключи - номера строк, значения - кол-во слов в строке
user_file = open('text_1.txt')
for line in user_file:
    i_line += 1
    i_words = len(line.split())
    i_dict = {i_line: i_words}
    result_dict.update(i_dict)
print(result_dict)
user_file.close()
