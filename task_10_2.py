# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.

# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes_abstract(ABC):
    @abstractmethod
    def __init__(self, s_type, size) -> None:
        self.type = s_type
        self.size = size
        self.sum_qt_cloth = self.qt_cloth

class Clothes(Clothes_abstract):
    __cloth = 0
    __clothes_types = {
        'coat': lambda x: x / 6.5 + 0.5,
        'suit': lambda x: 2 * x + 0.3
    }

    def __init__(self, s_type, size) -> None:
        self.type = s_type
        self.size = size
        self.sum_qt_cloth = self.qt_cloth

    @property
    def qt_cloth(self):
        # Метод расчета кол-ва ткани
        if self.cloth_type:
            return self.cloth_type(self.size)
        else:
            print(f'Type "{self.type}" not in list, add new type')
            return 0

    @property
    def sum_qt_cloth(self):
        # Геттер для суммы всей ткани
        return Clothes.__cloth

    @sum_qt_cloth.setter
    def sum_qt_cloth(self, c):
        # Сеттер для суммы всей ткани
        Clothes.__cloth += c

    @property
    def cloth_type(self) -> dict:
        # Геттер для типов ткани с формулой расчета
        if self.__clothes_types.get(self.type):
            return self.__clothes_types.get(self.type)

    @classmethod
    def add_cloth_type(cls, new_type):
        # Сеттер для добавления новых видов ткани
        cls.__clothes_types.update(new_type)

    def __str__(self) -> str:
        return f"Тип: {self.type}\nРазмер: {self.size}\nКоличество необходимой ткани: {self.qt_cloth:.02f}\n{'-'*10}"



if __name__ == '__main__':
    from random import choice, randint

    clo_list = ['coat', 'suit', 'gbl']
    Clothes.add_cloth_type({'gbl': lambda x: 2 * x + 0.3})

    clothes_obj = [Clothes(choice(clo_list), randint(10, 100)) for _ in range(10)]

    for obj in clothes_obj:
        print(obj)

    # print(sum(map(lambda x: x.qt_cloth, clothes_obj)))
    print('Всего необходимо ткани:', obj.sum_qt_cloth)
    