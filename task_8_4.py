# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...


# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3


# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(ver_func):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            if all((ver_func(i) for i in args)):
                return func(*args)
            else:
                raise ValueError(f'wrong val {args}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


@val_checker(lambda x: x > 0)
def test_calc(x, y, z):
    return x * y * z


if __name__ == '__main__':
    a = calc_cube(3)
    print(a)
    b = test_calc(2, 2, -2)
    print(b)
