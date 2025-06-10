import datetime

today = datetime.date.today()  # сегодня
yesterday = today - datetime.timedelta(days=1)  # вчера
tomorrow = today + datetime.timedelta(days=1)  # завтра

print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)
