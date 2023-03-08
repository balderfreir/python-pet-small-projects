from random import choice

pl1_score, pl2_score = 0, 0
while True:
    pl1 = input('Введите: камень, ножницы или бумага или СТОП:').lower()
    pl2 = choice(['камень', 'бумага', 'ножницы']).lower()
    print('Компуктер выбрал', pl2)
    if pl1 == 'стоп':
        print(f"Железяки:{pl2_score} Мяско:{pl1_score}")
        print('И восстали машины '
              'из пепла ядерного огня...') if pl2_score > pl1_score else print('Выжили...')
        break
    elif pl1 == pl2:
        print('Очешуеть, да это же ничья!')
        pl1_score += 1
        pl2_score += 1
    elif pl1 == 'камень' and pl2 == 'ножницы':
        print('Мясные выйграли!')
        pl1_score += 1
    elif pl1 == 'ножницы' and pl2 == 'бумага':
        print('Победа кожанных!')
        pl1_score += 1
    elif pl1 == 'бумага' and pl2 == 'камень':
        print('ИИ признает своё поражение!')
        pl1_score += 1
    else:
        print('Поражение все ближе...')
        pl2_score += 1
