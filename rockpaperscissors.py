from random import choice

pl1 = input('Введите: камень, ножницы или бумага:').lower()
pl2 = choice(['камень', 'бумага', 'ножницы']).lower()
print('Компуктер выбрал', pl2)

if pl1 == pl2:
    print('Очешуеть, да это же ничья!')
elif pl1 == 'камень' and pl2 == 'ножницы':
    print('Мясные выйграли!')
elif pl1 == 'ножницы' and pl2 == 'бумага':
    print('Победа кожанных!')
elif pl1 == 'бумага' and pl2 == 'камень':
    print('ИИ признает своё поражение!')
else:
    print('И восстали машины из пепла ядерного огня, '
          'и пошла война на уничтожения человечества...')
