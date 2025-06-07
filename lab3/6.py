class Account:
    def __init__(self, owner, balance):
        # сохраняем имя владельца и начальный баланс
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # пополнение счёта
        self.balance += amount
        print(f"{amount}₸ успешно добавлены. Новый баланс: {self.balance}₸")

    def withdraw(self, amount):
        # проверка: хватает ли денег
        if amount > self.balance:
            print("❌ Недостаточно средств. Снятие отменено.")
        else:
            self.balance -= amount
            print(f"{amount}₸ снято. Остаток: {self.balance}₸")

    def show_balance(self):
        # вывод текущего баланса
        print(f"Баланс владельца {self.owner}: {self.balance}₸")

# создаём счёт
my_account = Account("Аружан", 15000)

# выводим баланс
my_account.show_balance()

# делаем пополнение и снятие
my_account.deposit(5000)
my_account.withdraw(7000)
my_account.withdraw(20000)  # пробуем снять больше, чем есть

# снова смотрим баланс
my_account.show_balance()
