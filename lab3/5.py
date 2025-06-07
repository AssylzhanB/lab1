import math  # модуль нужен для вычисления расстояния

class Point:
    def __init__(self, x, y):
        # создаём точку с координатами x и y
        self.x = x
        self.y = y

    def show(self):
        # показываем координаты
        print("Точка находится в координатах:", (self.x, self.y))

    def move(self, new_x, new_y):
        # меняем координаты точки
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        # считаем расстояние до другой точки
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

# создаём две точки
point1 = Point(2, 3)
point2 = Point(5, 7)

# показываем координаты
point1.show()
point2.show()

# считаем расстояние между ними
distance = point1.dist(point2)
print("Расстояние между точками:", distance)

# перемещаем первую точку
point1.move(10, 10)
point1.show()
