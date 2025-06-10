def countdown(n):
    for i in range(n, -1, -1):  # идём назад
        yield i

# Тест:
for num in countdown(5):
    print(num)
