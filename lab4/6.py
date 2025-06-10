def even_gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Получаем n от пользователя
n = int(input("Введите число: "))
evens = list(even_gen(n))
print(",".join(map(str, evens)))  # превращаем в строку с запятыми
