# Словарь (dictionary) — это коллекция пар "ключ: значение"
# Удобно для хранения связанных данных (например, имя и возраст)

person = {
    "name": "Alice",
    "age": 25,
    "city": "Almaty"
}

# Доступ к значениям по ключу
print(person["name"])  # Выведет: Alice
print(person["age"])   # Выведет: 25

# Добавление новой пары
person["email"] = "alice@example.com"
print(person)
# Теперь в словаре есть новый ключ "email"

# Изменение значения
person["age"] = 26
print(person["age"])  # Выведет: 26

# Удаление пары по ключу
del person["city"]
print(person)
# Ключ "city" и его значение удалены

# Перебор всех ключей и значений
for key, value in person.items():
    print(key, ":", value)

# Проверка, есть ли ключ в словаре
print("name" in person)   # True
print("city" in person)   # False — мы его удалили

# Получение только ключей или только значений
print(person.keys())      # dict_keys(['name', 'age', 'email'])
print(person.values())    # dict_values(['Alice', 26, 'alice@example.com'])
