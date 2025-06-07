# создаём класс Account (Счёт)
class Account:
    def __init__(self, owner, balance):
        # когда создаётся счёт, мы указываем владельца и сумму на счёте
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # метод для пополнения баланса
        self.balance += amount
        print("Баланс пополнен на", amount)

    def withdraw(self, amount):
        # метод для снятия денег
        if amount > self.balance:
            print("Недостаточно денег на счёте!")
        else:
            self.balance -= amount
            print("Вы сняли", amount)

    def show_balance(self):
        # метод, чтобы показать текущий баланс
        print("Ваш текущий баланс:", self.balance)

# создаём объект (счёт)
my_account = Account("Аружан", 10000)

# смотрим баланс
my_account.show_balance()

# пополняем
my_account.deposit(5000)
my_account.show_balance()

# пробуем снять слишком много
my_account.withdraw(20000)
my_account.show_balance()

# снимаем нормальную сумму
my_account.withdraw(3000)
my_account.show_balance()
