def my_title(str1):
    """
    the function takes a string and capitalizes the first letter
    :param str1: type string
    :return: return string with capitalizes the first letter
    """
    str1 = str(str1)
    return str1[0].upper() + str1[1:]


str_title = ''
str_user = input('Введите строку ').split()
for i in str_user:
    str_title += my_title(i) + ' '
print(str_title)
