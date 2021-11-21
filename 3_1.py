def my_division(arg1, arg2):
    """
    the function returns the result of dividing two numbers
    :param arg1: first number
    :param arg2: second number
    :return: the result of dividing two numbers
    """
    try:
        arg1 / arg2
    except ZeroDivisionError:
        return print('division by zero')
    return arg1 / arg2


div1 = float(input('Введите делимое число '))
div2 = float(input('Введите делитель '))
print(my_division(div1, div2))
