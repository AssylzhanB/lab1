import datetime

date1 = datetime.datetime(2024, 6, 1, 12, 0, 0)  # дата 1
date2 = datetime.datetime(2024, 6, 2, 12, 0, 0)  # дата 2

diff = date2 - date1  # находим разницу
seconds = diff.total_seconds()  # получаем в секундах

print("Разница в секундах:", seconds)
