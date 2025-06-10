import datetime

now = datetime.datetime.now()  # сейчас (дата и время)
clean_time = now.replace(microsecond=0)  # убираем микросекунды

print("Время без микросекунд:", clean_time)
