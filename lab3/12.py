import math  # импортируем модуль с числом пи

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)  # формула объёма сферы
    return volume

# Пример использования
r = float(input("Введите радиус сферы: "))
print("Объём сферы:", sphere_volume(r))
