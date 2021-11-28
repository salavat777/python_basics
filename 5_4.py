__author__ = 'Сафиулин Салават Тельманович'

# Задача-4: Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from translate import Translator

translator = Translator(from_lang='en', to_lang='ru')
user_file = open('text_4.txt')
user_file2 = open('text_4_ru.txt', 'w')
for line in user_file:
    i_str = line.split()
    i_str[0] = translator.translate(i_str[0])
    line_ru = ' '.join(i_str)
    user_file2.write(line_ru + '\n')
user_file.close()
user_file2.close()
