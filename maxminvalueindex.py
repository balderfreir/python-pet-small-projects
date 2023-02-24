a = [23, 76, 45, 20, 70, 65, 15, 54, 22, 75, 31, 78, 0]


def max_value_index(list):
    mx_ix = 0
    for i, el in enumerate(list):
        if el > list[mx_ix]:
            mx_ix = i
    return mx_ix


def min_value_index(list):
    mn_ix = 0
    for i, el in enumerate(list):
        if el < list[mn_ix]:
            mn_ix = i
    return mn_ix


def value_index(list):
    mx_ix = 0
    mn_ix = 0
    for i, el in enumerate(list):
        if el > list[mx_ix]:
            mx_ix = i
        elif el < list[mn_ix]:
            mn_ix = i
    return mx_ix, mn_ix


print(f'Индекс максимального значения в списке: {max_value_index(a)}')
print(f'Индекс минимального значения в списке: {min_value_index(a)}')
print(f'Все и сразу: {value_index(a)}')
