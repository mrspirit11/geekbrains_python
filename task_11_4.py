# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, numb: complex) -> None:
        self.numb = complex(numb)

    def __add__(self, obj):
        return Complex(self.numb + obj.numb)

    def __mul__(self, obj):
        return Complex(self.numb * obj.numb)

    def __str__(self):
        return str(self.numb)

a = Complex(-5 + 3j)
b = Complex(4 + 2j)
c = a + b
d = a * b
print(c)
print(d)

