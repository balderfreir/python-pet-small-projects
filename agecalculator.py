# импортируем библ для работы с форматом дат
import datetime
# запрашиваем у пользователя его др "дд мм гггг"
b_day_str = input('Введите дату рождения через пробел: ')
# приобразуем строку в форматы даты
b_day_date = datetime.datetime.strptime(b_day_str, '%d %m %Y')
# так, а какое сегодня число? 0_0
today = datetime.datetime.now().date()
# выводим возраст в годах. учитываем текущий месяц и день
print("Ваш возраст на текущий момент: ",
      today.year - b_day_date.year if (today.month, today.day) >=
     (b_day_date.month, b_day_date.day) else today.year - b_day_date.year - 1)
