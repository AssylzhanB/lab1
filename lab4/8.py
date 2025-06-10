def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Тест:
for square in squares(2, 5):
    print(square)
