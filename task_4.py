__author__ = 'Сафиулин Салават Тельманович'

# Задача-4: Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.
n = int(input('Введите целое положительное число '))
if n < 1:
    print('Число указано некорректно, должно быть больше 1')
else:
    num = n % 10
    m = n//10
    while m > 0:
        if num < (m % 10):
            num = m % 10
        m = m//10
print(f'Самая большая цифра в числе {n} = {num}')
