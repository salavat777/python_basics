__author__ = 'Сафиулин Салават Тельманович'

# Задача-3: Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад
# менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

i_line = 0
sum_profit = 0
result_dict = {}  # словарь с результатами, ключи - ФИО, значения - оклады
user_file = open('text_3.txt', encoding="utf-8")
for line in user_file:
    i_str = line.split()
    name = i_str[0]
    profit = float(i_str[1])
    i_line += 1
    sum_profit += profit
    if profit < 20000:
        i_dict = {name: profit}
        result_dict.update(i_dict)
print('Сотрудники с окладами менее 20 тыс. - ', result_dict)
print(f'Средний оклад по всем сотрудникам {sum_profit/i_line:0.1f}')
user_file.close()
