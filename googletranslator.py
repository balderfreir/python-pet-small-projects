from googletrans import Translator

translator = Translator()
# По умолчанию идет перевод на английский язык
# translate() объект с несколькими параметрами
# нам нужен толькот text
text = translator.translate('Привет!').text
print('1', text, end=' ')
# Для перевода на др язык, его можно указать
text = translator.translate('Привет!', dest='ja')
# посмотрим и перевод и произношение
print('2', text.text, text.pronunciation, end=' ')
# иногда лучше указывать язык исходника
text = 'veritas lux mea'
# определяем язык
ln = translator.detect(text).lang
# переводим фразу на русский
text_tr = translator.translate(text, src=ln, dest='ru').text
print('3', text_tr)
