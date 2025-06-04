command = "start"

# Используем match для сравнения значения переменной
match command:
    case "start":  # если значение равно "start"
        print("Запуск программы")
    case "stop":   # если значение равно "stop"
        print("Остановка программы")
    case _:        # если не совпало ни с одним case — "по умолчанию"
        print("Неизвестная команда")


day = 3

match day:
    case 1:
        print("Понедельник")
    case 2:
        print("Вторник")
    case 3:
        print("Среда")
    case 4:
        print("Четверг")
    case 5:
        print("Пятница")
    case _:
        print("Выходной день")


color = "red"

match color:
    case "red" | "orange" | "yellow":  # если color — один из этих
        print("Тёплый цвет")
    case "blue" | "green":             # если один из этих
        print("Холодный цвет")
    case _:                            # если ничего не подошло
        print("Неизвестный цвет")



point = (0, 5)

# Используем match для разбора координат точки
match point:
    case (0, y):  # если x == 0, а y любое — значит точка на оси Y
        print(f"На оси Y: y = {y}")
    case (x, 0):  # если y == 0 — точка на оси X
        print(f"На оси X: x = {x}")
    case (x, y):  # любая другая точка
        print(f"Внутри плоскости: x = {x}, y = {y}")



