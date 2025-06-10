def square_gen(n):
    for i in range(n + 1):
        yield i * i  # возвращаем квадрат числа

# Пример использования:
for num in square_gen(5):
    print(num)
