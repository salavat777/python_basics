from sys import argv

script_name, hours, pay_hour, bonus = argv
profit = round(int(hours) * float(pay_hour) + float(bonus), 2)
print(profit)
