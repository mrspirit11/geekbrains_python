# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...


# @type_logger
# def calc_cube(x):
#    return x ** 3


# >>> a = calc_cube(5)
# 5: <class 'int'>


# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):

    def wrap(*args, **kwargs):
        func_val = func(*args, **kwargs)
        args_str = [f'{i}: {type(i)}' for i in args] + [f'{k}={v}: {type(v)}' for k, v in kwargs.items()]
        print(f'{func.__name__}({", ".join(args_str)})', f'-> {type(func_val)}')
        return func_val
    return wrap


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def s_sum(x, y, z):
    return x + y + z


if __name__ == '__main__':

    print(calc_cube(3))
    print(s_sum(2, 5, z=2.5))
