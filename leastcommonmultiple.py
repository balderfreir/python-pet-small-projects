# объявляем функцию
def least_common_multiple(a, b):
    # узнаем какое число больше
    # и кладем в greater
    greater = a if a > b else b
    # теперь в цикле будем проверять кратность a и b
    while True:
        # если они кратны (делятся без остатка)
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater  # тогда мы шанли НОК
            break  # выходми из цикла
        else:
            # если нет, то увеличиваем greater на 1
            greater += 1
    return lcm


print(least_common_multiple(10, 12))