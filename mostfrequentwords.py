from collections import Counter
text = []
# открываем и читаем фаил
with open('th_felowshp_of_te_rng.txt', 'r') as f:
    for line in f:
        # записываем каждую строку в список,
        # предварительно разбив ее на слова
        text.extend(line.split())
# создаем экземляр счетчика
counter = Counter(text)
# находим топ 10 слов по частоте
top10 = counter.most_common(10)
print(top10)
