__author__ = 'Сафиулин Салават Тельманович'


# Задача-4, 5, 6: Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

class Warehouse:
    def __init__(self):
        self.dict_wh = {}

    def add_equip(self, obj_oe, number):
        if self.dict_wh.get(obj_oe.list_oe) is None:
            num = 0
        else:
            num = self.dict_wh.get(obj_oe.list_oe)
        num += number
        self.dict_wh.update({obj_oe.list_oe: num})

    def del_equip(self, obj_oe, number):
        if self.dict_wh.get(obj_oe.list_oe) is None:
            print('Такой номенклатуры нет на складе')
            return
        else:
            num = self.dict_wh.get(obj_oe.list_oe)
            if num < number:
                print('Нет такого количества номенклатуры на складе')
                return
            else:
                num -= number
                self.dict_wh.update({obj_oe.list_oe: num})


class OfficeEquipment:
    def __init__(self, type_equip, brand, model, unit, price):
        self.type_equip = type_equip
        self.brand = brand
        self.model = model
        self.unit = unit
        self.price = price


class Copier(OfficeEquipment):

    def __init__(self, brand, model, paper_size, print_type, unit, price):
        super().__init__('Копир', brand, model, unit, price)
        self.paper_size = paper_size
        self.print_type = print_type
        self.list_oe = self.type_equip + '/' + self.brand + '/' + self.model + \
                       '/' + self.paper_size + '/' + self.print_type + '/' + self.unit + '/' + self.price


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, paper_size, resolution, interface, unit, price):
        super().__init__('Сканер', brand, model, unit, price)
        self.paper_size = paper_size
        self.resolution = resolution
        self.interface = interface
        self.list_oe = self.type_equip + '/' + self.brand + '/' + self.model + '/' + self.paper_size + '/' + \
                       self.resolution + '/' + self.interface + '/' + self.unit + '/' + \
                       self.price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, paper_size, print_type, chroma, unit, price):
        super().__init__('Принтер', brand, model, unit, price)
        self.paper_size = paper_size
        self.print_type = print_type
        self.chroma = chroma
        self.list_oe = self.type_equip + '/' + self.brand + '/' + self.model + '/' + self.paper_size + '/' + \
                       self.print_type + '/' + self.chroma + '/' + self.unit + '/' + self.price


c1 = Copier('Canon', 'imageRUNNER 2206', 'A3', 'лазерный', 'шт', '56320')
c2 = Copier('Canon', 'imageRUNNER 2206iF', 'A3', 'лазерный', 'шт', '125420')
c3 = Copier('Canon', 'imageRUNNER C3720', 'A3', 'цветной', 'шт', '148000')
p1 = Printer('Xerox', 'Phaser 3020', 'A4', 'лазерный', 'черно-белый', 'шт', '10490')
p2 = Printer('HP', 'Laser 107r', 'A4', 'лазерный', 'черно-белый', 'шт', '7990')
p3 = Printer('Epson', 'L805', 'A4', 'струйный', 'цветной', 'шт', '7990')
s1 = Scanner('HP', 'ScanJet Pro N4000 snw1', 'A4', '600x600dpi', 'USB|Ethernet|WiFi', 'шт', '39350')
s2 = Scanner('HP', 'ScanJet Pro 3000 s4', 'A4', '600x600dpi', 'USB', 'шт', '35690')
s3 = Scanner('Epson', 'WorkForce DS-410', 'A4', '600x600dpi', 'USB', 'шт', '42900')
nomenclature_obj = {1: c1, 2: c2, 3: c3, 4: p1, 5: p2, 6: p3, 7: s1, 8: s2, 9: s3}
WH1 = Warehouse()
WH1.add_equip(c1, 0)
WH1.add_equip(c2, 0)
WH1.add_equip(c3, 0)
WH1.add_equip(p1, 0)
WH1.add_equip(p2, 0)
WH1.add_equip(p3, 0)
WH1.add_equip(s1, 0)
WH1.add_equip(s2, 0)
WH1.add_equip(s3, 0)

while True:
    print('1) Оприходовать\n2) Списать\n3) Остатки на складе\n4) Выход из'
          ' программы')
    action = input('Введите номер действия: ').strip()
    if action == '4':
        break
    elif action == '1':
        for key, values in nomenclature_obj.items():
            print(f'{key} : {values.list_oe}')
        action_1 = input('Введите позицию номенклатуры: ').strip()
        if nomenclature_obj.get(int(action_1)) is None:
            print('Не существующая номенклатура')
        else:
            n = abs(int(input('Введите кол-во, которое необходимо оприходовать: ').strip()))
            WH1.add_equip(nomenclature_obj.get(int(action_1)), n)
    elif action == '2':
        for key, values in nomenclature_obj.items():
            print(f'{key} : {values.list_oe}')
        action_2 = input('Введите позицию номенклатуры: ').strip()
        if nomenclature_obj.get(int(action_2)) is None:
            print('Не существующая номенклатура')
        else:
            n = abs(int(input('Введите кол-во, которое необходимо списать: ').strip()))
            WH1.del_equip(nomenclature_obj.get(int(action_2)), n)
    elif action == '3':
        for key, values in nomenclature_obj.items():
            print(f'{key} : {values.list_oe} количество/{WH1.dict_wh.get(values.list_oe)}')
