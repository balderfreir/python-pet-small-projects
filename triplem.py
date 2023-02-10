# mean — это среднее значение всех значений в наборе данных.
def mean_calc(arr):
    mean = sum(arr) / len(arr)
    return mean


# median — это среднее значение среди всех значений в отсортированном порядке.
def median_calc(arr):
    arr.sort()
    len_arr = len(arr)
    index = len_arr // 2
    if len_arr % 2 == 0:
        m1, m2 = arr[index], arr[index - 1]
        median = (m1 + m2) / 2
    else:
        median = arr[index]
    return median


# mode — наиболее часто встречающимся значением среди всех значений
def mode_calc(arr):
    frq = {}
    for el in arr:
        if el in frq.keys():
            frq[el] += 1
        else:
            frq[el] = 1
    return [k for k, v in frq.items() if v == max(frq.values())]


nums = [12, 16, 20, 20, 12, 5, 7, 9, 30, 25, 23, 24, 20, 1]

print(f'Среднее арифметическое: {mean_calc(nums)}',
      f'Тоже среднее, но медиана: {median_calc(nums)}',
      f'Наиболее частое, мода: {mode_calc(nums)}', sep='\n')

from statistics import mean, median, mode

print(f'Среднее : {mean(nums)}',
      f'Медиана: {median(nums)}',
      f'Мода: {mode(nums)}', sep='\n')
