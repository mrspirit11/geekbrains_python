def edit_file(file, line_numb: str, text: str):
    with open(file, 'r+', encoding='UTF-8') as f_in:
        if line_numb == '1':
            cur = 0
        i = 0
        while i < int(line_numb) - 1:
            line = f_in.readline()
            cur = f_in.tell()
            i += 1
        if line_numb == '1' or line:
            # print(line)
            f_in.seek(cur)
            f_in.write(text)
            f_in.truncate(len(line) + len(text))
        else:
            print('Нет такой строки')


if __name__ == '__main__':
    import sys
    # if len(sys.argv) == 3:
    #     edit_file('bakery.csv', *sys.argv[1:])
    # else:
    #     print("Введите агрументы в формате: номер_строки исправленный текст")

    edit_file('bakery.csv', '2', '00000000')
    with open('bakery.csv', 'rb') as f:
        print(f.read())
