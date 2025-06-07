from itertools import permutations

def print_permutations(s):
    # itertools.permutations возвращает все перестановки строки s
    perms = permutations(s)
    
    # выводим каждую перестановку в виде строки
    for p in perms:
        print(''.join(p))

# пример использования
user_input = input("Введите строку: ")
print("Все перестановки строки:")
print_permutations(user_input)
