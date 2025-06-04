colors = ("red", "green", "blue")

print(colors[0])  # 'red'
print(colors[-1]) # 'blue'


for color in colors:
    print(color)


print(len(colors))  # 3


num = (5,)      # Это кортеж
print(type(num))  # <class 'tuple'>

num2 = (5)      # Это просто число
print(type(num2))  # <class 'int'>


points = [(1, 2), (3, 4), (5, 6)]
print(points[0])      # (1, 2)
print(points[0][1])   # 2

