def show_sales(file,_from=0, _to=0):
    _from, _to = map(int, [_from, _to])
    with open(file, encoding='UTF-8') as f_in:
        if _from and _to:
            for line in f_in.readlines()[_from - 1:_to + 1]:
                print(line.strip())
        elif _from:
            for line in f_in.readlines()[_from - 1:]:
                print(line.strip())
        else:
            for line in f_in:
                print(line.strip())


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        show_sales('bakery.csv', *sys.argv[1:3])
    else:
        show_sales('bakery.csv')
