def add_sale(file, *args) -> None:
    with open(file, 'a', encoding='UTF-8') as f_out:
        f_out.writelines([f'{s}\n' for s in args[0]])


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        add_sale('bakery.csv', sys.argv[1:])
    else:
        print('Enter a sum')
