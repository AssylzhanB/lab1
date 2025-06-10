def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Пример использования
for num in div_by_3_and_4(50):
    print(num)
