import calendar
import datetime
# Текущие дата и время
today = datetime.datetime.today().date()
# Создаем TextCalendar
cal = calendar.TextCalendar()
# Вызываем formatmonth()
month_str = cal.formatmonth(2023, 2)
# Выводим
print(month_str)
# Короткий вариант для ленивых =)
print(calendar.month(today.year, today.month))



