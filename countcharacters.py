def count_characters(str):
    """Не учитывает регистр или пробелы,
    т.е. Е != е и ' ' - так же отдельный символ"""
    counter = {}  # создаем словать
    for ch in str:  # идем по каждому эл строки
        # если он есть в словаре, увеличиваем значение
        if ch in counter:
            counter[ch] += 1
        # если его нет, то записываем со значением 1
        else:
            counter[ch] = 1
    return counter

string = 'Some string for counting letters'
print(count_characters(string))
