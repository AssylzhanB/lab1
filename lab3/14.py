def is_palindrome(text):
    # Убираем пробелы и приводим к нижнему регистру для честной проверки
    clean_text = text.replace(" ", "").lower()
    # Проверяем, равна ли строка сама себе в обратном порядке
    return clean_text == clean_text[::-1]

# Пример использования
user_input = input("Введите слово или фразу: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")
