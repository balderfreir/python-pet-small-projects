# ипортируем подкласс встроенного класса dict()
from collections import defaultdict
# небольшая заготовка для проверки работы
words = ["tea", "bat", "eat", "ate", "arc", "car",
         "ears", "ares", "rase", "hare", "hear"]
# функция выполняющая группировку
def group_anagrams(words):
    dic = defaultdict(list)
    for i in words:
        key = "".join(sorted(i))
        dic[key].append(i)
    for key in dic.keys():
        print(key, ":", dic[key])
# запускаем, проверяем
print('Дано', words[:6], words[6:], sep='\n')
group_anagrams(words)
