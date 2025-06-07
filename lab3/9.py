def reverse_words(sentence):
    # разбиваем строку на слова по пробелам
    words = sentence.split()
    
    # переворачиваем список слов
    reversed_words = words[::-1]
    
    # соединяем обратно в строку через пробел
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# пример использования
user_input = input("Введите предложение: ")
result = reverse_words(user_input)
print("Перевернутое предложение:", result)
