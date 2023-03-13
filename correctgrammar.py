#!pip install gingerit
from gingerit.gingerit import GingerIt

# Что будем исправлять?
text = input("Enter a sentence: ")
corrected_text = GingerIt().parse(text)
# Выводим результат
print(corrected_text['result'])