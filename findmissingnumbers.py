# список чисел, они не соритораны, есть повторы и пропуски
numbers = [2, 5, 1, 4, 8, 6, 3, 0, 10, 15, 1, 5]
# функция принимает на вход список чисел
def find_missing_num(n_list):
    # убираем повторы
    num_u = set(n_list)
    # сортируем отчищеный от дублей
    num = sorted(num_u)
    out = []  # список для пропусков
    # цикл в диапазоне от 0 до старшего числа
    for i in range(num[-1]):
        if i not in num:
            out.append(i)
    print(f'Дано {n_list}', f'Уникальные {num_u}',
          f'Сортированные {num}', f'Пропущенные: {out}', sep='\n')
# запускаем, проверяем
find_missing_num(numbers)
