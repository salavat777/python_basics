__author__ = 'Сафиулин Салават Тельманович'

# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n1 = int(input('Введите целое положительное число '))
if n1 < 1:
    print('Число указано некорректно, должно быть больше 1')
else:
    n2 = int(str(n1)+str(n1))
    n3 = int(str(n1)+str(n1)+str(n1))
    sum = n1+n2+n3
    print(f'Сумма чисел {n1}+{n2}+{n3}={sum}')
