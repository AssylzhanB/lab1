def unique_elements(lst):
    unique = []  # создаём пустой список для уникальных элементов
    for item in lst:
        if item not in unique:
            unique.append(item)  # добавляем только если ещё нет в списке
    return unique

# Пример использования
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Уникальные элементы:", unique_elements(numbers))
