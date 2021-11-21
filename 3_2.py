def personal_data(first_name, second_name, birthday, city, email, tel):
    """
    the function converts your personal data into a formatted string
    :param first_name, second_name, birthday, city, email, tel: your personal data, type string
    :return: formatted string with your personal data
    """
    return print(f'Ваше ФИО {first_name} {second_name}, день рождения {birthday}, '
                 f'город проживания {city}, email {email}, телефон {tel}')


name = input('Имя: ')
surname = input('Фамилия: ')
birthday = input('д.р.: ')
city = input('город: ')
email = input('email: ')
tel = input('телефон: ')
personal_data(first_name=name, second_name=surname, birthday=birthday, city=city, email=email, tel=tel)
