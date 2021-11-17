__author__ = 'Сафиулин Салават Тельманович'

# Задача-6: Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

i = 1
list_name = []
list_price = []
list_count = []
list_unit = []
product_list = []
analitic_dict = {}
while True:
    print('1) Ввод товара')
    print('2) Вывод структуры')
    print('3) Аналитика товаров')
    print('0) Завершить программу')
    trigger = input('Выберите действие 1,2,3,0 ')
    if trigger == '0':
        break
    elif trigger == '1':
        name = input('Введите наименование товара ')
        price = float(input('Введите стоимость товара '))
        count = float(input('Введите кол-во товара '))
        unit = input('Введите единицу измерения товара ')
        product_dict = {'Наименование': name, 'Цена': price,
                        'Количество': count, 'ед': unit}
        product_list.append((i, product_dict))
        i += 1
    elif trigger == '2':
        print(product_list)
    elif trigger == '3':
        for k, val in product_list:
            list_name.append(val['Наименование'])
            list_price.append(val['Цена'])
            list_count.append(val['Количество'])
            list_unit.append(val['ед'])
        analitic_dict = dict(Наименование=list_name, Цена=list_price,
                             Количество=list_count, ед=list_unit)
        print(analitic_dict)
