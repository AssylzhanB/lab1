# Создание множества (set)
# Множество — это неупорядоченная коллекция уникальных элементов
fruits = {"apple", "banana", "cherry", "apple"}  

print(fruits)  
# Вывод: {'apple', 'banana', 'cherry'}
# Повторяющийся элемент "apple" будет удалён автоматически

# Добавление элемента
fruits.add("orange")
print(fruits)
# Теперь в множестве есть "orange"

# Удаление элемента
fruits.remove("banana")
print(fruits)
# Удалили "banana"

# Проверка наличия элемента
print("cherry" in fruits)  # True
print("banana" in fruits)  # False — мы её удалили

# Объединение двух множеств
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  
# Вывод: {1, 2, 3, 4, 5}

# Пересечение множеств (общие элементы)
intersection = set1.intersection(set2)
print(intersection)  
# Вывод: {3}

#
