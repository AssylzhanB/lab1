def is_prime(n):
    # простое число — это больше 1 и делится только на 1 и само себя
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    # используем list comprehension для фильтрации
    return [num for num in numbers if is_prime(num)]

# пример использования
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
prime_list = filter_prime(input_list)

print("Простые числа:", prime_list)
