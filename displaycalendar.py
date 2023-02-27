import calendar
# Создаем TextCalendar
cal = calendar.TextCalendar()
# Вызываем formatmonth()
month_str = cal.formatmonth(2023, 2)
# Выводим
print(month_str)
# Короткий вариант для ленивых =)
print(calendar.month(2023, 3))