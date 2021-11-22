list_source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_source[i + 1] for i in range(len(list_source) - 1)
            if int(list_source[i + 1]) > int(list_source[i])]
print(new_list)
