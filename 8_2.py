__author__ = 'Сафиулин Салават Тельманович'


# Задача-2: Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
# на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


div1 = input('Введите делимое: ')
div2 = input('Ведите делитель: ')

try:
    div1 = int(div1)
    div2 = int(div2)
    if div2 == 0:
        raise ZeroDivision('Деление на ноль')
except (ValueError, ZeroDivision) as err:
    print(err)
else:
    print(f'Частное = {div1/div2}')
