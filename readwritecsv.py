import pandas as pd
# записываем наш путь до фаила
path = 'test_data.csv'
# создает dataframe
df = pd.read_csv(path, sep=';')
print('Данны без изменений:')
print(df.info(), end='\n')
# удоляем первую колонку
del df[df.columns [0]]
print('Данные после изменений: ')
print(df.info(), end='\n')
# сохраняем новую таблицу в фаил
df.to_csv('test_data_1.csv')
