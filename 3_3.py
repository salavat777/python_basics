def my_sum(x, y, z):
    """
    the function takes three numbers and returns the sums of the two maximum numbers
    :param x, y, z: three numbers
    :return: sums of the two maximum numbers
    """
    iter_obj = [x, y, z]
    return sum(iter_obj) - min(iter_obj)


print('Сумма равна ', my_sum(5, 10, 15))
