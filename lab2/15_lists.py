fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']


fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # 'apple' — нумерация начинается с 0
print(fruits[-1]) # 'cherry' — последний элемент


fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']


fruits.append("grape")     # добавить в конец
print(fruits)              # ['apple', 'orange', 'cherry', 'grape']

fruits.remove("orange")    # удалить по значению
print(fruits)              # ['apple', 'cherry', 'grape']


for fruit in fruits:
    print(fruit)
#output


print(len(fruits))  # 3 — количество элементов

