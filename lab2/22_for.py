fruits = ["apple", "banana", "cherry"]

# Проходим по каждому элементу списка
for fruit in fruits:
    print(fruit)

# Вывод:
# apple
# banana
# cherry


# range(5) — числа от 0 до 4
for i in range(5):
    print(i)

# Вывод:
# 0
# 1
# 2
# 3
# 4




# От 1 до 10, с шагом 2
for i in range(1, 11, 2):
    print(i)

# Вывод:
# 1
# 3
# 5
# 7
# 9



word = "hello"

for letter in word:
    print(letter)

# Вывод:
# h
# e
# l
# l
# o




person = {"name": "Aruzhan", "age": 25}

# Перебираем ключи и значения
for key, value in person.items():
    print(key, ":", value)

# Вывод:
# name : Aruzhan
# age : 25





for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
