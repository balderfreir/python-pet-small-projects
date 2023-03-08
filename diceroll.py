from random import randint

print(f'Сколько костей?')
n = int(input())
print(f'Диапазон значений, через пробел')
min_v, max_v = input().split(" ")
print(f'Бросить кости? y/n:')
answer = input()
while answer == 'y':
    for _ in range(n):
        # int() нужен, т.к min/max пока строки
        print(randint(int(min_v), int(max_v)))
    print(f'Бросить ещё? y/n:')
    answer = input()

