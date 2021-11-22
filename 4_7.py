from math import factorial


def gen_fact(x):
    """
    function generator factorials of numbers up to x inclusive
    :param x: factorial is calculated from numbers up to X inclusive
    :return: the function returns a generator object.
    """
    for el in range(1, x + 1):
        yield factorial(el)


int1 = int(input('Введите число для генератора факториалов '))
for i in gen_fact(int1):
    print(i)
