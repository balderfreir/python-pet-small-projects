#!pip install gingerit
from gingerit.gingerit import GingerIt

# Что будем исправлять?
text = input("Enter a sentence: ")
corrected_text = GingerIt().parse(text)
# Выводим результат
print(corrected_text['result'])
[print(msk) for msk in corrected_text['corrections']]
# how ar u? im fine fank yoy and yiu?
