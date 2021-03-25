# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой


class MyZeroDevisionErr(ZeroDivisionError):
    def __str__(self) -> str:
        return '\33[91mДеление на ноль\33[0m'

class MyDiv:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    @property
    def div(self) -> float:
        try:
            if self.b == 0:
                raise MyZeroDevisionErr
            else:
                return self.a/self.b
        except MyZeroDevisionErr as e:
            print(e)
            return 0


a = MyDiv(4,2).div
print(a)