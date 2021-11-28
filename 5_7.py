__author__ = 'Сафиулин Салават Тельманович'

# Задача-7: Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно
# прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет
# средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

i_str = 0
list1 = []
average_profit = 0
user_list1 = []
user_dict_average_profit = {}
user_dict_firm_profit = {}
with open('text_7.txt', encoding="utf-8") as user_file:
    for line in user_file:
        list1 = line.split()
        key_udfp = list1[0]
        value_udfp = int(list1[2]) - int(list1[3])
        item_udfp = {key_udfp: value_udfp}
        user_dict_firm_profit.update(item_udfp)
        if value_udfp > 0:
            average_profit += value_udfp
            i_str += 1
average_profit = average_profit / i_str
user_dict_average_profit = {'average_profit': average_profit}
user_list1 = [user_dict_firm_profit, user_dict_average_profit]
print(user_list1)
with open('text_77.json', 'w', encoding="utf-8") as user_file:
    json.dump(user_list1, user_file, ensure_ascii=False, indent=4)
