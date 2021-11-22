list_source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list_source if list_source.count(el) == 1]
print(new_list)
