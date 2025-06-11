import re

# Открываем файл и читаем содержимое
with open("row.txt", encoding="utf-8") as file:
    text = file.read()

# 1. Названия товаров (после номеров типа 1., 2., 3.)
product_names = re.findall(r'\d+\.\n(.+)', text)
print("Названия товаров:")
for name in product_names[:5]:  # покажем только первые 5
    print("-", name)

# 2. Все суммы в чеке
prices = re.findall(r'\d[\d ]*,\d{2}', text)
print("\nЦены (первые 5):")
for price in prices[:5]:
    print("-", price)

# 3. Итоговая сумма
total = re.search(r'ИТОГО:\s*\n([0-9 ,]+)', text)
if total:
    print("\nИтоговая сумма:", total.group(1))

# 4. Дата и время
datetime = re.search(r'Время:\s*([\d:. ]+)', text)
if datetime:
    print("Дата и время покупки:", datetime.group(1))
