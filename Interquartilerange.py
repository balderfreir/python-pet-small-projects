import numpy as np

data = list(range(20, 100, 5))
print(f'Наши данные: {data}')
# посчитаем 1,2 и 3-й квартили
Q1 = np.quantile(data, 0.25)
Q2 = np.quantile(data, 0.50)
Q3 = np.quantile(data, 0.75)
# посмотрим что получилось
print(f"Quartile 25 : {Q1}")
print(f"Quartile 50 : {Q2}")
print(f"Quartile 75 : {Q3}")

def interqrtl_rng(a, b):
    """Интерквартильный размах"""
    return a - b

print(f'{interqrtl_rng.__doc__} {interqrtl_rng(Q3, Q1)}')
