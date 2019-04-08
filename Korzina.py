#*ЗАДАЧА 1:
#1. Создать класс корзина, у которого можно выставить разную вместительность #для разных объектов.
#В объекты класса корзина можно помещать разные объекты;
#2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
#3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
#4. Если вместимости недостаточно, сказать, что объект поместить нельзя.

class Korzina(object):
    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('Эта корзина размером = {}'.format(self. size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} это помещено в корзину'. format(smth))
        else:
            print('{} слишком большой для корзины с этим размером = {}'.format(smth, self.size))


class Directory(Korzina):
    def get_size(self):
        print('Это размер Директории корзины = {}'.format(self.size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} это перемещено в Директорию'.format(smth))
        else:
            print('{} это слишком размер для Директории = {}'.format(smth, self.size))

class Thing(object):
    def __init__(self, size):
        self.size = size


box1 = Korzina(20)
box1.get_size()

bag1 = Directory(123)
bag1.get_size()

smth1 = Thing(10)
smth2 = Thing(30)
smth3 = Thing(300)

box1.put_smth(smth1)
box1.put_smth(smth2)
