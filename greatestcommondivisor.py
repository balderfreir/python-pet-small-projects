def greatest_common_divisor(a, b):
    # узнаем какое число меньше
    # и кладем в smaller
    smaller = b if a > b else a
    # теперь в цикле будем проверять
    # числа от 1 до наименьшего
    for i in range(1, smaller + 1):
        # если оба числа делятся без остатка
        # то мы нашли делитель
        if (a % i == 0) and (b % i == 0):
            # присваеваем его меременной gcd
            gcd = i
    return gcd


# проверим как работает наша функция
a = 7
b = 35
print(f"НОД для {a} и {b} самописный {greatest_common_divisor(a, b)}")
# в math есть готовое решение
from math import gcd

print(f"НОД для {a} и {b} встроенный {gcd(a, b)}")
