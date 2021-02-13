# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
list_of_expressions = (15 * 3,
                       15 / 3,
                       15 // 2,
                       15 ** 2)
for expr in list_of_expressions:
    print(type(expr))
