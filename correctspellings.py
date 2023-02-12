import spellchecker
"""The currently supported dictionaries are:
English - ‘en’, Spanish - ‘es’, French - ‘fr’, Portuguese - ‘pt’
German - ‘de’, Russian - ‘ru’, Arabic - ‘ar’"""
corrector = spellchecker.SpellChecker(language='ru')
# цикл while True позволяет постоянно запрашивать у вас слово
while True:
    word = input("Что проверяем? : ")
    if word in corrector:
        print("Верно!")
    else:
        correct_word = corrector.correction(word)
        print("Мне кажется, что правильнее будет: ", correct_word)