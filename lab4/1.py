import datetime  # берём модуль даты и времени

today = datetime.date.today()  # сегодня
five_days = datetime.timedelta(days=5)  # 5 дней
new_date = today - five_days  # отнимаем 5 дней

print("Дата 5 дней назад:", new_date)
