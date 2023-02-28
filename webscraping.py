# импортируем/устанавливаем либы
import csv
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

# источник данных, часть ссылки на рус нуждается в предобработке
html = urlopen("https://ru.wikipedia.org/wiki/" + quote("Фильмография_Джеки_Чана"))
soup = BeautifulSoup(html, "html.parser")
# на вики нам нужна только таблица, через инспектора смотрим ее класс
table = soup.findAll("table", {"class": "wikitable"})[0]
# стоки занесены в тег tr
rows = table.findAll("tr")
# сохраняем таблицу в фаил
with open("Jackie_Chan_filmography.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:  # проходимся по строкам таблицы
        row = []  # в этот список будем записывать данные
        # в каждей строке находми тег td
        for cell in i.findAll(["td"]):
            # записываем его содержание в список убирая лишнее
            row.append(cell.get_text().strip())
        writer.writerow(row)  # записываем список в фаил

import pandas as pd
# посмотрим что получилось
a = pd.read_csv("Jackie_Chan_filmography.csv", names=['year', 'drop_it', 'name_ru', 'name_chi', 'role'])
a.drop(columns=['drop_it', 'name_chi'], inplace=True)
print(a.info())
print(a.head(), a.tail(), sep='\n')
