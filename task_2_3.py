# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьезнее, чем может сначала показаться.

in_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(in_list), end=' = ')
i = 0
while i < len(in_list):
    if in_list[i].isdigit() or in_list[i][0] in ('+', '-'):
        if len(in_list[i]) == 1:
            in_list[i] = f'0{in_list[i]}'
        elif in_list[i][0] in ('+','-') and len(in_list[i]) == 2:
            in_list[i] = f'{in_list[i][0]}0{in_list[i][1:]}'
        in_list.insert(i,'"')
        in_list.insert(i+2,'"')
        i += 2
    i += 1
print(id(in_list))
print(in_list)

print(' '.join(in_list))

for _ in range(len(in_list)):
    if in_list[_] == '"':
        in_list[_] = ''
    elif in_list[_].isdigit() or in_list[_][0] in ('+', '-'):
        in_list[_] = f'"{in_list[_]}"'
print(' '.join(in_list))