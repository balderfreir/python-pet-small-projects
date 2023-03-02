with open('th_felowshp_of_te_rng.txt') as file:
    # создаем счетчик
    count = 0
    # заносим весь текст в переменную
    text = file.read()
    # проходимся по символьно
    for i in text:
        # является ли символ заглавным?
        if i.isupper():
            # если да, то увеличиваем на 1
            count += 1
print(count)
