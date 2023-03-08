def validate_anagrams(a=None, b=None):
    # проверяем, введены ли значения
    if not a or not b:
        ans = 'Ты шо то забыл...'
    # проверяем, не одно ли и тоже слова
    elif a.lower() == b.lower():
        ans = 'Почему слова одинаковые?'
    # проверка на анаграмность!
    elif sorted(a.lower()) == sorted(b.lower()):
        ans = 'Да это же анаграмы!!!'
    else:
        ans = 'Не анаграмы...'
    return f'a = {a},b = {b} ---> {ans}'

print(validate_anagrams("cinema"))
print(validate_anagrams("cool", "loco"))
print(validate_anagrams("men", "women"))
print(validate_anagrams("Finger", "finger"))
print(validate_anagrams("cinema", "iceman"))

