def palindrome(sentence):
    # ищем знаки препинания и убераем их
    for i in (",.'?/><}{{}}'"):
        sentence = sentence.replace(i, "")
    palindrome = []
    # разбиваем на слова по пробелу
    words = sentence.split(' ')
    # приводим слова к нижнему регистру
    for word in words:
        word = word.lower()
        # проверка на палиндромность
        if word == word[::-1]:
            palindrome.append(word)
    return palindrome

sen = input("Enter a sentence : ")
#  LOL, My interview went good. My Mom will be so happy.
print(palindrome(sen))