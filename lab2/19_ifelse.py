age = 18

# Если возраст больше или равен 18
if age >= 18:
    print("Вы совершеннолетний")


age = 16

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")


score = 75

if score >= 90:
    print("Оценка: A")
elif score >= 80:
    print("Оценка: B")
elif score >= 70:
    print("Оценка: C")
else:
    print("Оценка: D")


age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Доступ разрешён")
    else:
        print("Нужен документ")
else:
    print("Доступ запрещён")


age = 21

message = "Вход разрешён" if age >= 18 else "Вход запрещён"
print(message)
