import random  # импортируем модуль для случайных чисел

def guess_the_number():
    secret_number = random.randint(1, 20)  # загадали число от 1 до 20
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Пожалуйста, вводи числа!")
            continue
        
        guesses_taken += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Запуск игры
guess_the_number()
