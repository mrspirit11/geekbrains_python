# 5. Реализовать класс Stationery (канцелярская принадлежность).

# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'канцелярская принадлежность'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print(f'{self.title}, Запуск отрисовки')

class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print(f'Запуск отрисовки ({self.title})')

class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print(f'Запуск отрисовки "{self.title}"')

Stationery = [i.draw() for i in  [Stationery(), Pen(), Pencil(), Handle()]]