sum_final = 0
flag_break = 0
while True:
    my_str = input('Введите строку чисел разделенных пробелами')
    str1 = my_str.split()
    sum_str1 = 0
    for i in str1:
        if i.isdigit():
            sum_str1 += int(i)
        elif i == 'q':
            flag_break = 1
            break
        else:
            print("Error!")
    sum_final += sum_str1
    print(f'Сумма {sum_final} ({sum_str1})')
    if flag_break:
        break
