# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10) (в том числе и в подпапках)
# значения — списки вида [<files_quantity>, [<files_extensions_list>]], например:
#
#   {
#       100: [15, ['txt']],
#       1000: [3, ['py', 'txt']],
#       10000: [7, ['html', 'css']],
#       100000: [2, ['png', 'jpg']]
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os, json
import copy


def get_all_size(s_path: str, max_size=9) -> tuple:
    full_path = (os.path.join(obj[0], f) for obj in os.walk(s_path) for f in obj[2])
    path_to_files = ((os.path.getsize(i), os.path.splitext(i)[1]) for i in full_path if os.path.isfile(i))

    sizes = {}
    sizes_list = [10 ** i for i in range(1, max_size + 1)]

    files_count = 0
    for file in path_to_files:
        files_count += 1
        for size in sizes_list:
            if file[0] < size:
                sizes.setdefault(size, [0, set()])
                sizes[size][0] += 1
                sizes[size][1].add(file[1])
                break
    return sizes, files_count


def json_save(dir_name: str, s_dict: dict):
    obj = copy.copy(s_dict)
    for key in obj:
        if isinstance(obj[key][1], set):
            obj[key] = list(obj[key][1])
    with open(f'{dir_name}_summary.json', 'w') as f_out:
        json.dump(obj, f_out)
    print('File saved')



if __name__ == '__main__':
    from pprint import pprint as pp
    dir_path = os.path.join('.')
    sizes_dict, files_count = get_all_size(dir_path)
    print(f'Файлов на диске: {files_count}', f'Файлов обработано: {sum(i[0] for i in sizes_dict.values())}', sep='\n')
    pp(sizes_dict)
    json_save(os.path.basename(dir_path), sizes_dict)
