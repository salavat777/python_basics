def my_pow1(x, y):
    """
    the function returns the number raised to the power of y in base x
    :param x, y: base - x, degree - y
    :return: degree y base x
    """
    return x ** y


def my_pow2(x, y):
    """
    the function returns the number raised to the power of y in base x. Сyclical method
    :param x, y: base - x, degree - y
    :return: degree y base x
    """
    i = 0
    multiplication = 1
    while i < abs(y):
        multiplication *= x
        i += 1
    if y > 0:
        return multiplication
    elif y < 0:
        return 1 / multiplication
    else:
        return 1


print('Первая функция отрицательная степень', my_pow1(2, -2))
print('Первая функция положительная степень', my_pow1(2, 2))
print('Первая функция степень равна нулю', my_pow1(2, 0))
print('Вторая функция отрицательная степень', my_pow2(2, -2))
print('Вторая функция положительная степень', my_pow2(2, 2))
print('Вторая функция степень равна нулю', my_pow2(2, 0))
