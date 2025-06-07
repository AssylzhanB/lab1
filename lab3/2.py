
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# список чисел
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# используем filter и lambda для выбора только простых чисел
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# выводим результат
print("Простые числа из списка:", prime_numbers)
